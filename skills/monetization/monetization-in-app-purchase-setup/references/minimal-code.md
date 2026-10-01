# Minimal purchase code (route A: code it yourself)

A starting point for a single "Pro" unlock, not a finished library. APIs change every year, so check each call
against the official docs linked in [iap-platform-facts.md](iap-platform-facts.md) before you ship.
Product IDs here (`pro_lifetime`) are placeholders.

## iOS / macOS: StoreKit 2 + SwiftUI (iOS 17+ for the `purchase` environment action)

```swift
import StoreKit
import SwiftUI

@MainActor
final class Store: ObservableObject {
    @Published private(set) var products: [Product] = []
    @Published private(set) var isPro = false
    private var updates: Task<Void, Never>?

    init() {
        // 1. Start at launch: renewals, Ask to Buy, offer codes and purchases on other devices arrive here.
        updates = Task { [weak self] in
            for await result in Transaction.updates {
                await self?.handle(result)
            }
        }
        Task { await load(); await refresh() }
    }

    func load() async {
        // An empty array usually means a wrong ID or an unsigned Paid Apps Agreement.
        products = (try? await Product.products(for: ["pro_lifetime"])) ?? []
    }

    // 2. Call this with the result of the SwiftUI `purchase` action.
    func handle(_ result: Product.PurchaseResult) async {
        if case .success(let verification) = result { await handle(verification) }
        // .pending (Ask to Buy) and .userCancelled: do nothing; .pending arrives later via Transaction.updates.
    }

    private func handle(_ verification: VerificationResult<Transaction>) async {
        guard case .verified(let transaction) = verification else { return } // failed verification: don't unlock
        // Optional: send verification.jwsRepresentation to your server here.
        await transaction.finish()
        await refresh()
    }

    // 3. One source of truth. Refunded purchases disappear from currentEntitlements.
    func refresh() async {
        var pro = false
        for await result in Transaction.currentEntitlements {
            if case .verified(let t) = result, t.productID == "pro_lifetime" { pro = true }
        }
        isPro = pro
    }

    // 4. Restore button (required by App Review).
    func restore() async {
        try? await AppStore.sync()
        await refresh()
    }
}

struct BuyButton: View {
    @EnvironmentObject var store: Store
    @Environment(\.purchase) private var purchase
    let product: Product

    var body: some View {
        Button("Unlock Pro · \(product.displayPrice)") {
            Task {
                if let result = try? await purchase(product) { await store.handle(result) }
            }
        }
    }
}
```

Test it before touching App Store Connect: File → New → StoreKit Configuration File, add `pro_lifetime`,
then Scheme → Run → Options → StoreKit Configuration.

## Android: Play Billing Library 8+ (Kotlin, `billing-ktx`)

```kotlin
// build.gradle: implementation("com.android.billingclient:billing-ktx:<latest 8.x or 9.x>")

class Billing(context: Context, private val scope: CoroutineScope, private val onPro: (Boolean) -> Unit) {

    private val client = BillingClient.newBuilder(context)
        .setListener { result, purchases ->
            if (result.responseCode == BillingClient.BillingResponseCode.OK) {
                purchases?.forEach { scope.launch { handle(it) } }
            }
        }
        .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
        .enableAutoServiceReconnection()
        .build()

    // Call startConnection once (e.g. in Application/Activity onCreate) and wait for onBillingSetupFinished.
    fun connect(onReady: () -> Unit) = client.startConnection(object : BillingClientStateListener {
        override fun onBillingSetupFinished(result: BillingResult) {
            if (result.responseCode == BillingClient.BillingResponseCode.OK) onReady()
        }
        override fun onBillingServiceDisconnected() { /* auto reconnection is enabled */ }
    })

    suspend fun proDetails(): ProductDetails? {
        val params = QueryProductDetailsParams.newBuilder().setProductList(listOf(
            QueryProductDetailsParams.Product.newBuilder()
                .setProductId("pro_lifetime")
                .setProductType(BillingClient.ProductType.INAPP)
                .build()
        )).build()
        return client.queryProductDetails(params).productDetailsList?.firstOrNull()
    }

    fun buy(activity: Activity, details: ProductDetails) {
        val params = BillingFlowParams.newBuilder().setProductDetailsParamsList(listOf(
            BillingFlowParams.ProductDetailsParams.newBuilder()
                .setProductDetails(details)
                // Subscriptions (and one-time products with several offers) also need .setOfferToken(...)
                .build()
        )).build()
        client.launchBillingFlow(activity, params)
    }

    // Restore / sync: call on every onResume.
    suspend fun refresh() {
        val params = QueryPurchasesParams.newBuilder().setProductType(BillingClient.ProductType.INAPP).build()
        val purchases = client.queryPurchasesAsync(params).purchasesList
        onPro(purchases.any { it.products.contains("pro_lifetime") && it.purchaseState == Purchase.PurchaseState.PURCHASED })
        purchases.forEach { handle(it) }
    }

    private suspend fun handle(p: Purchase) {
        if (p.purchaseState != Purchase.PurchaseState.PURCHASED) return  // never unlock PENDING
        // Recommended: verify p.purchaseToken on your server (purchases.products.get) before unlocking.
        onPro(true)
        if (!p.isAcknowledged) {  // must happen within 3 days or Google refunds it
            client.acknowledgePurchase(
                AcknowledgePurchaseParams.newBuilder().setPurchaseToken(p.purchaseToken).build()
            )
        }
    }
}
```

Test it: upload the AAB to internal testing, create `pro_lifetime` in Play Console, add yourself as a license
tester, install from the internal testing link, and buy with the "Test card, always approves".

## Where the server goes (optional for a lifetime unlock, recommended for subscriptions)

```text
App ──purchase──▶ Store
App ──JWS / purchaseToken──▶ Your server ──verify──▶ App Store Server API / Play Developer API
Store ──App Store Server Notifications V2 / RTDN (Pub/Sub)──▶ Your server ──▶ update the user's entitlement
App ──"is Pro?"──▶ Your server (or the device check above if you have no server)
```
