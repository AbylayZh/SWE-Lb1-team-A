struct Order {
    let id: String
    let buyerName: String
    let products: [ProductOrder]
}

struct ProductOrder {
    let productName: String
    let quantity: Int
}
