class CartManager {
    static let shared = CartManager()
    private init() {}

    private(set) var cartItems: [CartItem] = []

    func addProduct(_ product: Product, quantity: Int = 1) {
        if let index = cartItems.firstIndex(where: { $0.product.id == product.id }) {
            // Product already in cart, update quantity
            cartItems[index].quantity += quantity
        } else {
            // New product, add to cart
            let cartItem = CartItem(product: product, quantity: quantity)
            cartItems.append(cartItem)
        }
    }

    func updateQuantity(for product: Product, quantity: Int) {
        if let index = cartItems.firstIndex(where: { $0.product.id == product.id }) {
            cartItems[index].quantity = quantity
        }
    }

    func removeProduct(_ product: Product) {
        cartItems.removeAll { $0.product.id == product.id }
    }

    func clearCart() {
        cartItems.removeAll()
    }
}
