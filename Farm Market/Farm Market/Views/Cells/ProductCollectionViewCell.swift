import UIKit

class ProductCollectionCell: UICollectionViewCell {
    
    // MARK: - UI Elements
    
    private let imageView = UIImageView()
    private let nameLabel = UILabel()
    private let priceLabel = UILabel()
    
    // MARK: - Initialization
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }
        
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    // MARK: - UI Setup
    
    private func setupUI() {
        // Add subviews
        contentView.addSubview(imageView)
        contentView.addSubview(nameLabel)
        contentView.addSubview(priceLabel)
        
        // Configure subviews
        imageView.contentMode = .scaleAspectFill
        imageView.clipsToBounds = true
        
        nameLabel.font = UIFont.boldSystemFont(ofSize: 14)
        nameLabel.textAlignment = .center
        nameLabel.numberOfLines = 2
        
        priceLabel.font = UIFont.systemFont(ofSize: 12)
        priceLabel.textAlignment = .center
        priceLabel.textColor = .gray
        
        // Layout constraints
        imageView.snp.makeConstraints { make in
            make.top.leading.trailing.equalToSuperview()
            make.height.equalTo(contentView.snp.width)
        }
        
        nameLabel.snp.makeConstraints { make in
            make.top.equalTo(imageView.snp.bottom).offset(5)
            make.leading.trailing.equalToSuperview().inset(5)
        }
        
        priceLabel.snp.makeConstraints { make in
            make.top.equalTo(nameLabel.snp.bottom).offset(2)
            make.leading.trailing.bottom.equalToSuperview().inset(5)
        }
    }
    
    // MARK: - Configuration
    
    func configure(with product: Product) {
        let url = URL(string: product.imageURLs)
        self.imageView.kf.setImage(with: url)
//        imageView.image =  /*product.imageURLs ?? */UIImage(named: "placeholder")
        nameLabel.text = product.name
        priceLabel.text = "$\(product.price)"
    }
}
