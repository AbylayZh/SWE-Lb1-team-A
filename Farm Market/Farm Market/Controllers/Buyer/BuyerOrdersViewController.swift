//
//  BuyerOrdersViewController.swift
//  Farm Market
//
//  Created by Nurgali on 19.11.2024.
//

import UIKit

class BuyerOrdersViewController: UIViewController {
    
    // MARK: - Properties
    
    //    private var cartItems: [CartItem] = []
    
    private let tableView = UITableView()
    private let totalPriceLabel = UILabel()
    private let orderButton = UIButton(type: .system)
    
    private var cartItems: [CartItem] {
        return CartManager.shared.cartItems
    }
    
    // MARK: - Lifecycle Methods
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        configureNavigationBar()
        setupTableView()
        setupBottomView()
        loadCartItems()
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        tableView.reloadData()
        calculateTotalPrice()
    }
    
    // MARK: - UI Setup
    
    private func configureNavigationBar() {
        navigationItem.title = "My Cart"
    }
    
    private func setupTableView() {
        view.addSubview(tableView)
        tableView.frame = view.bounds
        
        tableView.delegate = self
        tableView.dataSource = self
        
        tableView.register(CartItemCell.self, forCellReuseIdentifier: "CartItemCell")
    }
    
    private func setupBottomView() {
        let bottomView = UIView()
        bottomView.backgroundColor = .white
        bottomView.layer.shadowColor = UIColor.black.cgColor
        bottomView.layer.shadowOpacity = 0.1
        bottomView.layer.shadowOffset = CGSize(width: 0, height: -2)
        bottomView.layer.shadowRadius = 4
        
        view.addSubview(bottomView)
        
        bottomView.translatesAutoresizingMaskIntoConstraints = false
        totalPriceLabel.translatesAutoresizingMaskIntoConstraints = false
        orderButton.translatesAutoresizingMaskIntoConstraints = false
        
        bottomView.addSubview(totalPriceLabel)
        bottomView.addSubview(orderButton)
        
        NSLayoutConstraint.activate([
            bottomView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            bottomView.trailingAnchor.constraint(equalTo: view.trailingAnchor),
            bottomView.bottomAnchor.constraint(equalTo: view.safeAreaLayoutGuide.bottomAnchor),
            bottomView.heightAnchor.constraint(equalToConstant: 80),
            
            totalPriceLabel.leadingAnchor.constraint(equalTo: bottomView.leadingAnchor, constant: 16),
            totalPriceLabel.centerYAnchor.constraint(equalTo: bottomView.centerYAnchor),
            
            orderButton.trailingAnchor.constraint(equalTo: bottomView.trailingAnchor, constant: -16),
            orderButton.centerYAnchor.constraint(equalTo: bottomView.centerYAnchor),
            orderButton.widthAnchor.constraint(equalToConstant: 120),
            orderButton.heightAnchor.constraint(equalToConstant: 44)
        ])
        
        totalPriceLabel.font = UIFont.boldSystemFont(ofSize: 18)
        totalPriceLabel.text = "Total: $0.00"
        
        orderButton.setTitle("Place Order", for: .normal)
        orderButton.backgroundColor = UIColor.systemBlue
        orderButton.tintColor = .white
        orderButton.layer.cornerRadius = 8
        orderButton.addTarget(self, action: #selector(placeOrderTapped), for: .touchUpInside)
    }
    
    // MARK: - Data Loading
    
    private func loadCartItems() {
        // Simulate loading cart items (Replace with actual data fetching)
        //        cartItems = [
        //            CartItem(product: Product(id: "1", name: "Apples", category: "Fruits", price: 1.5, quantity: 100, description: "Fresh apples", imageURLs: "https://example.com/apple.jpg"), quantity: 2),
        //            CartItem(product: Product(id: "2", name: "Bananas", category: "Fruits", price: 0.8, quantity: 200, description: "Organic bananas", imageURLs: "https://example.com/banana.jpg"), quantity: 5)
        //        ]
        
        calculateTotalPrice()
        tableView.reloadData()
    }
    
    // MARK: - Actions
    
    @objc private func placeOrderTapped() {
        let alert = UIAlertController(title: "Order Placed", message: "Your order has been placed successfully.", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: { _ in
            CartManager.shared.clearCart()
            self.tableView.reloadData()
            self.calculateTotalPrice()
        }))
        present(alert, animated: true, completion: nil)
    }
    
    private func calculateTotalPrice() {
        let total = cartItems.reduce(0.0) { $0 + ($1.product.price * Double($1.quantity)) }
        totalPriceLabel.text = String(format: "Total: $%.2f", total)
    }
    
}

extension BuyerOrdersViewController: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return cartItems.count
    }
    
}

// MARK: - UITableViewDelegate

extension BuyerOrdersViewController: UITableViewDelegate {
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        
        let cartItem = cartItems[indexPath.row]
        
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "CartItemCell", for: indexPath) as? CartItemCell else {
            return UITableViewCell()
        }
        
        cell.configure(with: cartItem)
        cell.delegate = self
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
    }
    
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if editingStyle == .delete {
            let cartItem = cartItems[indexPath.row]
            CartManager.shared.removeProduct(cartItem.product)
            tableView.deleteRows(at: [indexPath], with: .automatic)
            calculateTotalPrice()
        }
    }
    
}

// MARK: - CartItemCellDelegate

extension BuyerOrdersViewController: CartItemCellDelegate {
    
    func cartItemCell(_ cell: CartItemCell, didUpdateQuantity quantity: Int) {
        if let indexPath = tableView.indexPath(for: cell) {
            let cartItem = cartItems[indexPath.row]
            CartManager.shared.updateQuantity(for: cartItem.product, quantity: quantity)
            calculateTotalPrice()
        }
    }
}
