import UIKit

protocol CartItemCellDelegate: AnyObject {
    func cartItemCell(_ cell: CartItemCell, didUpdateQuantity quantity: Int)
}

class CartItemCell: UITableViewCell {

    weak var delegate: CartItemCellDelegate?

    private let productNameLabel = UILabel()
    private let priceLabel = UILabel()
    private let quantityLabel = UILabel()
    private let minusButton = UIButton(type: .system)
    private let plusButton = UIButton(type: .system)

    private var quantity: Int = 1

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    private func setupUI() {
        contentView.addSubview(productNameLabel)
        contentView.addSubview(priceLabel)
        contentView.addSubview(quantityLabel)
        contentView.addSubview(minusButton)
        contentView.addSubview(plusButton)

        productNameLabel.translatesAutoresizingMaskIntoConstraints = false
        priceLabel.translatesAutoresizingMaskIntoConstraints = false
        quantityLabel.translatesAutoresizingMaskIntoConstraints = false
        minusButton.translatesAutoresizingMaskIntoConstraints = false
        plusButton.translatesAutoresizingMaskIntoConstraints = false

        NSLayoutConstraint.activate([
            productNameLabel.leadingAnchor.constraint(equalTo: contentView.leadingAnchor, constant: 16),
            productNameLabel.topAnchor.constraint(equalTo: contentView.topAnchor, constant: 16),

            priceLabel.leadingAnchor.constraint(equalTo: productNameLabel.leadingAnchor),
            priceLabel.topAnchor.constraint(equalTo: productNameLabel.bottomAnchor, constant: 8),
            priceLabel.bottomAnchor.constraint(equalTo: contentView.bottomAnchor, constant: -16),

            plusButton.trailingAnchor.constraint(equalTo: contentView.trailingAnchor, constant: -16),
            plusButton.centerYAnchor.constraint(equalTo: contentView.centerYAnchor),

            quantityLabel.trailingAnchor.constraint(equalTo: plusButton.leadingAnchor, constant: -8),
            quantityLabel.centerYAnchor.constraint(equalTo: contentView.centerYAnchor),

            minusButton.trailingAnchor.constraint(equalTo: quantityLabel.leadingAnchor, constant: -8),
            minusButton.centerYAnchor.constraint(equalTo: contentView.centerYAnchor),

            quantityLabel.widthAnchor.constraint(equalToConstant: 40)
        ])

        minusButton.setTitle("-", for: .normal)
        plusButton.setTitle("+", for: .normal)

        minusButton.addTarget(self, action: #selector(decreaseQuantity), for: .touchUpInside)
        plusButton.addTarget(self, action: #selector(increaseQuantity), for: .touchUpInside)

        quantityLabel.textAlignment = .center
    }


    func configure(with cartItem: CartItem) {
        productNameLabel.text = cartItem.product.name
        priceLabel.text = String(format: "$%.2f", cartItem.product.price)
        quantity = cartItem.quantity
        quantityLabel.text = "\(quantity)"
    }

    @objc private func decreaseQuantity() {
        if quantity > 1 {
            quantity -= 1
            quantityLabel.text = "\(quantity)"
            delegate?.cartItemCell(self, didUpdateQuantity: quantity)
        }
    }

    @objc private func increaseQuantity() {
        quantity += 1
        print(quantity)
        quantityLabel.text = "\(quantity)"
        delegate?.cartItemCell(self, didUpdateQuantity: quantity)
    }
    
}
