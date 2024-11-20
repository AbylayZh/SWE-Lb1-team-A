//
//  FarmerHomeViewController.swift
//  Farm Market
//
//  Created by Nurgali on 19.11.2024.
//

import UIKit
import Kingfisher

class FarmerHomeViewController: UIViewController {
    
    // MARK: - Properties
    
    var products: [Product] = []
    let tableView = UITableView()
    
    // MARK: - Lifecycle Methods
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemRed
        setupUI()
        loadProducts()
    }
    
    private func setupUI() {
        setupNavigationBar()
        setupTableView()
    }
    
    private func setupNavigationBar() {
        print("asd")
        navigationItem.title = "My Products"
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .add, target: self, action: #selector(addProductTapped))
    }
    
    private func setupTableView() {
        view.addSubview(tableView)
        tableView.register(ProductCell.self, forCellReuseIdentifier: "ProductCell")
        tableView.delegate = self
        tableView.dataSource = self
        
        // Layout using SnapKit
        tableView.snp.makeConstraints { make in
            make.edges.equalToSuperview()
        }
    }
    
    private func loadProducts() {
        // For now, load products from mock data
        products = MockData.shared.getFarmerProducts()
        tableView.reloadData()
    }
    
    @objc private func addProductTapped() {
        let addProductVC = AddProductViewController()
        addProductVC.delegate = self
        let navController = UINavigationController(rootViewController: addProductVC)
        present(navController, animated: true, completion: nil)
    }
}

extension FarmerHomeViewController: UITableViewDelegate {
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "ProductCell", for: indexPath) as? ProductCell else {
            return UITableViewCell()
        }
        
        let product = products[indexPath.row]
        cell.configure(with: product)
        return cell
    }
    
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle,
                   forRowAt indexPath: IndexPath) {
        
        if editingStyle == .delete {
            // Remove product from data source
            products.remove(at: indexPath.row)
            // Update table view
            tableView.deleteRows(at: [indexPath], with: .fade)
            // Optionally, update backend or local storage
        }
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let editProductVC = EditProductViewController(product: products[indexPath.row])
        editProductVC.delegate = self
        let navController = UINavigationController(rootViewController: editProductVC)
        present(navController, animated: true, completion: nil)
    }
}

extension FarmerHomeViewController: UITableViewDataSource {
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return products.count
    }
}

extension FarmerHomeViewController: AddProductViewControllerDelegate, EditProductViewControllerDelegate {
    func didAddProduct(_ product: Product) {
        products.append(product)
        tableView.reloadData()
    }
    
    func didEditProduct(_ product: Product) {
        if let index = products.firstIndex(where: { $0.id == product.id }) {
            products[index] = product
            tableView.reloadData()
        }
    }
}
