import UIKit

class ProductDetailViewController: UIViewController {
    
    // MARK: - Properties
    
    var product: Product
    
    // MARK: - UI Elements
    
    private let imageView = UIImageView()
    private let nameLabel = UILabel()
    private let priceLabel = UILabel()
    private let descriptionLabel = UILabel()
    private let addToCartButton = UIButton(type: .system)
    
    // MARK: - Initialization
    
    init(product: Product) {
        self.product = product
        super.init(nibName: nil, bundle: nil)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // MARK: - Lifecycle Methods
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        setupUI()
        configureView()
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        // Configure UI elements
        imageView.contentMode = .scaleAspectFit
        imageView.clipsToBounds = true
        
        nameLabel.font = UIFont.boldSystemFont(ofSize: 24)
        nameLabel.textAlignment = .center
        
        priceLabel.font = UIFont.systemFont(ofSize: 20)
        priceLabel.textColor = .systemGreen
        priceLabel.textAlignment = .center
        
        descriptionLabel.font = UIFont.systemFont(ofSize: 16)
        descriptionLabel.numberOfLines = 0
        
        addToCartButton.setTitle("Add to Cart", for: .normal)
        addToCartButton.backgroundColor = UIColor.systemBlue
        addToCartButton.tintColor = .white
        addToCartButton.layer.cornerRadius = 8
        addToCartButton.addTarget(self, action: #selector(addToCartTapped), for: .touchUpInside)
        
        // Add subviews
        view.addSubview(imageView)
        view.addSubview(nameLabel)
        view.addSubview(priceLabel)
        view.addSubview(descriptionLabel)
        view.addSubview(addToCartButton)
        
        // Layout constraints using SnapKit
        let padding = 20
        
        imageView.snp.makeConstraints { make in
            make.top.equalTo(view.safeAreaLayoutGuide.snp.top).offset(padding)
            make.centerX.equalToSuperview()
            make.width.height.equalTo(200)
        }
        
        nameLabel.snp.makeConstraints { make in
            make.top.equalTo(imageView.snp.bottom).offset(10)
            make.leading.trailing.equalToSuperview().inset(padding)
        }
        
        priceLabel.snp.makeConstraints { make in
            make.top.equalTo(nameLabel.snp.bottom).offset(5)
            make.leading.trailing.equalToSuperview().inset(padding)
        }
        
        descriptionLabel.snp.makeConstraints { make in
            make.top.equalTo(priceLabel.snp.bottom).offset(10)
            make.leading.trailing.equalToSuperview().inset(padding)
        }
        
        addToCartButton.snp.makeConstraints { make in
            make.top.equalTo(descriptionLabel.snp.bottom).offset(20)
            make.leading.trailing.equalToSuperview().inset(padding)
            make.height.equalTo(50)
        }
    }
    
    // MARK: - Configuration
    
    private func configureView() {
        if let imageURL = URL(string: product.imageURLs) {
            imageView.kf.setImage(with: imageURL, placeholder: UIImage(systemName: "Cloud"))
        } else {
            imageView.image = UIImage(systemName: "Cloud")
        }
        nameLabel.text = product.name
        priceLabel.text = "$\(product.price)"
        descriptionLabel.text = product.description
    }
    
    // MARK: - Actions
    
    @objc private func addToCartTapped() {
        CartManager.shared.addProduct(product)
        let alert = UIAlertController(title: "Added to Cart", message: "\(product.name) has been added to your cart.", preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alert, animated: true, completion: nil)
    }
    
    private func showAlert(title: String = "Info", message: String) {
        let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)
        alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
        present(alertController, animated: true, completion: nil)
    }
}
