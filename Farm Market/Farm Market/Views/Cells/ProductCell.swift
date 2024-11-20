//
//  ProductCell.swift
//  Farm Market
//
//  Created by Nurgali on 19.11.2024.
//

import UIKit
import Kingfisher

class ProductCell: UITableViewCell {
    
    // MARK: - UI Elements
    
    private let productImageView = UIImageView()
    private let nameLabel = UILabel()
    private let priceLabel = UILabel()
    private let quantityLabel = UILabel()
    
    // MARK: - Initialization
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        // Add subviews
        contentView.addSubview(productImageView)
        contentView.addSubview(nameLabel)
        contentView.addSubview(priceLabel)
        contentView.addSubview(quantityLabel)
        
        // Configure subviews
        productImageView.contentMode = .scaleAspectFill
        productImageView.clipsToBounds = true
        
        nameLabel.font = UIFont.boldSystemFont(ofSize: 16)
        priceLabel.font = UIFont.systemFont(ofSize: 14)
        quantityLabel.font = UIFont.systemFont(ofSize: 14)
        quantityLabel.textColor = .gray
        
        // Layout constraints
        productImageView.snp.makeConstraints { make in
            make.left.equalToSuperview().offset(10)
            make.centerY.equalToSuperview()
            make.width.height.equalTo(60)
        }
        
        nameLabel.snp.makeConstraints { make in
            make.top.equalToSuperview().offset(10)
            make.left.equalTo(productImageView.snp.right).offset(10)
            make.right.equalToSuperview().offset(-10)
        }
        
        priceLabel.snp.makeConstraints { make in
            make.top.equalTo(nameLabel.snp.bottom).offset(5)
            make.left.equalTo(nameLabel)
        }
        
        quantityLabel.snp.makeConstraints { make in
            make.top.equalTo(priceLabel.snp.bottom).offset(5)
            make.left.equalTo(nameLabel)
            make.bottom.equalToSuperview().offset(-10)
        }
    }
    
    // MARK: - Configuration
    
    func configure(with product: Product) {
        let url = URL(string: product.imageURLs)
        self.productImageView.kf.setImage(with: url)
//        productImageView.text = product.imageURLs[0]
        nameLabel.text = product.name
        priceLabel.text = "Price: $\(product.price)"
        quantityLabel.text = "Quantity: \(product.quantity)"
    }
    
}
