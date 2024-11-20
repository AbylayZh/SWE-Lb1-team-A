//
//  AddProductViewController.swift
//  Farm Market
//
//  Created by Nurgali on 19.11.2024.
//

import UIKit

protocol AddProductViewControllerDelegate: AnyObject {
    func didAddProduct(_ product: Product)
}

class AddProductViewController: UIViewController {
    
    // MARK: - UI Elements
    
    private let nameTextField = UITextField()
    private let categoryTextField = UITextField()
    private let priceTextField = UITextField()
    private let quantityTextField = UITextField()
    private let descriptionTextView = UITextView()
    private let addImageButton = UIButton(type: .system)
    private let saveButton = UIButton(type: .system)
    
    // MARK: - Properties
    
    weak var delegate: AddProductViewControllerDelegate?
    var selectedImages: String = ""
    
    // MARK: - Lifecycle Methods
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        setupUI()
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        navigationItem.title = "Add Product"
        navigationItem.leftBarButtonItem = UIBarButtonItem(barButtonSystemItem: .cancel, target: self, action: #selector(cancelTapped))
        
        // Configure text fields and text view
        nameTextField.placeholder = "Product Name"
        categoryTextField.placeholder = "Category"
        priceTextField.placeholder = "Price"
        priceTextField.keyboardType = .decimalPad
        quantityTextField.placeholder = "Quantity"
        quantityTextField.keyboardType = .numberPad
        descriptionTextView.layer.borderWidth = 1
        descriptionTextView.layer.borderColor = UIColor.lightGray.cgColor
        descriptionTextView.layer.cornerRadius = 5
        
        // Configure buttons
        addImageButton.setTitle("Add Images", for: .normal)
        addImageButton.addTarget(self, action: #selector(addImageTapped), for: .touchUpInside)
        
        saveButton.setTitle("Save Product", for: .normal)
        saveButton.backgroundColor = UIColor.systemBlue
        saveButton.tintColor = .white
        saveButton.layer.cornerRadius = 8
        saveButton.addTarget(self, action: #selector(saveButtonTapped), for: .touchUpInside)
        
        // Add subviews
        view.addSubview(nameTextField)
        view.addSubview(categoryTextField)
        view.addSubview(priceTextField)
        view.addSubview(quantityTextField)
        view.addSubview(descriptionTextView)
        view.addSubview(addImageButton)
        view.addSubview(saveButton)
        
        // Layout constraints using SnapKit
        let padding = 20
        
        nameTextField.snp.makeConstraints { make in
            make.top.equalTo(view.safeAreaLayoutGuide.snp.top).offset(padding)
            make.leading.trailing.equalToSuperview().inset(padding)
            make.height.equalTo(40)
        }
        
        categoryTextField.snp.makeConstraints { make in
            make.top.equalTo(nameTextField.snp.bottom).offset(10)
            make.leading.trailing.equalToSuperview().inset(padding)
            make.height.equalTo(40)
        }
        
        priceTextField.snp.makeConstraints { make in
            make.top.equalTo(categoryTextField.snp.bottom).offset(10)
            make.leading.trailing.equalToSuperview().inset(padding)
            make.height.equalTo(40)
        }
        
        quantityTextField.snp.makeConstraints { make in
            make.top.equalTo(priceTextField.snp.bottom).offset(10)
            make.leading.trailing.equalToSuperview().inset(padding)
            make.height.equalTo(40)
        }
        
        descriptionTextView.snp.makeConstraints { make in
            make.top.equalTo(quantityTextField.snp.bottom).offset(10)
            make.leading.trailing.equalToSuperview().inset(padding)
            make.height.equalTo(100)
        }
        
        addImageButton.snp.makeConstraints { make in
            make.top.equalTo(descriptionTextView.snp.bottom).offset(10)
            make.leading.equalToSuperview().inset(padding)
            make.height.equalTo(40)
            make.width.equalTo(120)
        }
        
        saveButton.snp.makeConstraints { make in
            make.top.equalTo(addImageButton.snp.bottom).offset(20)
            make.leading.trailing.equalToSuperview().inset(padding)
            make.height.equalTo(50)
        }
    }
    
    // MARK: - Actions
    
    @objc private func cancelTapped() {
        dismiss(animated: true, completion: nil)
    }
    
    @objc private func addImageTapped() {
        // Present image picker to select images
        let imagePicker = UIImagePickerController()
        imagePicker.delegate = self
        imagePicker.allowsEditing = false
        imagePicker.sourceType = .photoLibrary
        present(imagePicker, animated: true, completion: nil)
    }
    
    @objc private func saveButtonTapped() {
        // Validate inputs
        guard let name = nameTextField.text, !name.isEmpty,
              let category = categoryTextField.text, !category.isEmpty,
              let priceText = priceTextField.text, let price = Double(priceText),
              let quantityText = quantityTextField.text, let quantity = Int(quantityText),
              !descriptionTextView.text.isEmpty else {
            showAlert(message: "Please fill in all fields.")
            return
        }
        
        // Create new product
        let newProduct = Product(
            id: UUID().uuidString,
            name: name,
            category: category,
            price: price,
            quantity: quantity,
            description: descriptionTextView.text,
            imageURLs: descriptionTextView.text
        )
        
        // Inform delegate
        delegate?.didAddProduct(newProduct)
        
        // Dismiss view controller
        dismiss(animated: true, completion: nil)
    }
    
    private func showAlert(title: String = "Error", message: String) {
        let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alertController, animated: true, completion: nil)
    }
}

// MARK: - UIImagePickerControllerDelegate and UINavigationControllerDelegate

extension AddProductViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey: Any]) {
        
//        if let image = info[.originalImage] as? UIImage {
//            selectedImages.append(image)
//        }
        // MARK: FIX IT

        picker.dismiss(animated: true, completion: nil)
    }
}
