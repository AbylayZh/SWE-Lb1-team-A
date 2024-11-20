import UIKit

protocol EditProductViewControllerDelegate: AnyObject {
    func didEditProduct(_ product: Product)
}

class EditProductViewController: UIViewController {
    
    // MARK: - Properties
    
    var product: Product
    weak var delegate: EditProductViewControllerDelegate?
    
    // UI Elements
    private let nameTextField = UITextField()
    private let categoryTextField = UITextField()
    private let priceTextField = UITextField()
    private let quantityTextField = UITextField()
    private let descriptionTextView = UITextView()
    private let addImageButton = UIButton(type: .system)
    private let saveButton = UIButton(type: .system)
    private let imagesCollectionView: UICollectionView
    
    private var selectedImages: [UIImage] = []
    
    // MARK: - Initialization
    
    init(product: Product) {
        self.product = product
        
        // Initialize collectionView with a flow layout
        let layout = UICollectionViewFlowLayout()
        layout.scrollDirection = .horizontal
        imagesCollectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)
        
        super.init(nibName: nil, bundle: nil)
        
        // Set initial selected images from product.imageURLs
        loadProductImages()
    }
        
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // MARK: - Lifecycle Methods
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        setupUI()
        populateFields()
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        navigationItem.title = "Edit Product"
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
        
        saveButton.setTitle("Save Changes", for: .normal)
        saveButton.backgroundColor = UIColor.systemBlue
        saveButton.tintColor = .white
        saveButton.layer.cornerRadius = 8
        saveButton.addTarget(self, action: #selector(saveButtonTapped), for: .touchUpInside)
        
        // Configure collection view
        imagesCollectionView.delegate = self
        imagesCollectionView.dataSource = self
        imagesCollectionView.register(ImageCollectionViewCell.self, forCellWithReuseIdentifier: "ImageCell")
        imagesCollectionView.backgroundColor = .white
        
        // Add subviews
        view.addSubview(nameTextField)
        view.addSubview(categoryTextField)
        view.addSubview(priceTextField)
        view.addSubview(quantityTextField)
        view.addSubview(descriptionTextView)
        view.addSubview(addImageButton)
        view.addSubview(imagesCollectionView)
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
        
        imagesCollectionView.snp.makeConstraints { make in
            make.top.equalTo(addImageButton.snp.bottom).offset(10)
            make.leading.trailing.equalToSuperview()
            make.height.equalTo(100)
        }
        
        saveButton.snp.makeConstraints { make in
            make.top.equalTo(imagesCollectionView.snp.bottom).offset(20)
            make.leading.trailing.equalToSuperview().inset(padding)
            make.height.equalTo(50)
        }
    }
    
    // MARK: - Populate Fields
    
    private func populateFields() {
        nameTextField.text = product.name
        categoryTextField.text = product.category
        priceTextField.text = String(product.price)
        quantityTextField.text = String(product.quantity)
        descriptionTextView.text = product.description
    }
    
    private func loadProductImages() {
        // Load images from product.imageURLs
        // For mock data, we can simulate images
        // Since we're using UIImage placeholders, we'll need to adjust this when integrating with real image URLs
        
        // For now, we'll simulate with placeholder images
        for _ in product.imageURLs {
            if let placeholderImage = UIImage(named: "placeholder") {
                selectedImages.append(placeholderImage)
            }
        }
    }
    
    // MARK: - Actions
    
    @objc private func cancelTapped() {
        dismiss(animated: true, completion: nil)
    }
    
    @objc private func addImageTapped() {
        // Present image picker to select new images
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
        
        // Update product properties
        product.name = name
        product.category = category
        product.price = price
        product.quantity = quantity
        product.description = descriptionTextView.text
        // Handle imageURLs or images depending on your implementation
        
        // Notify delegate
        delegate?.didEditProduct(product)
        
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

extension EditProductViewController: UIImagePickerControllerDelegate, UINavigationControllerDelegate {
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey: Any]) {
        
        if let image = info[.originalImage] as? UIImage {
            selectedImages.append(image)
            imagesCollectionView.reloadData()
        }
        picker.dismiss(animated: true, completion: nil)
    }
}

// MARK: - UICollectionViewDelegate and UICollectionViewDataSource

extension EditProductViewController: UICollectionViewDelegate, UICollectionViewDataSource {
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return selectedImages.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {

        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "ImageCell", for: indexPath) as? ImageCollectionViewCell else {
            return UICollectionViewCell()
        }

        let image = selectedImages[indexPath.item]
        cell.configure(with: image)
        return cell
    }
    
    // Allow deletion of images
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        // Confirm deletion
        let alert = UIAlertController(title: "Delete Image", message: "Do you want to delete this image?", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "Delete", style: .destructive, handler: { _ in
            self.selectedImages.remove(at: indexPath.item)
            collectionView.deleteItems(at: [indexPath])
        }))
        alert.addAction(UIAlertAction(title: "Cancel", style: .cancel, handler: nil))
        present(alert, animated: true, completion: nil)
    }
}
