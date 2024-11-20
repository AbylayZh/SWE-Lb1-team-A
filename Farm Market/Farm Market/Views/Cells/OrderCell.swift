import UIKit

class OrderCell: UITableViewCell {

    private let productNameLabel = UILabel()
    private let quantityLabel = UILabel()

    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupUI()
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    private func setupUI() {
        addSubview(productNameLabel)
        addSubview(quantityLabel)

        productNameLabel.translatesAutoresizingMaskIntoConstraints = false
        quantityLabel.translatesAutoresizingMaskIntoConstraints = false

        NSLayoutConstraint.activate([
            productNameLabel.leadingAnchor.constraint(equalTo: leadingAnchor, constant: 16),
            productNameLabel.centerYAnchor.constraint(equalTo: centerYAnchor),

            quantityLabel.trailingAnchor.constraint(equalTo: trailingAnchor, constant: -16),
            quantityLabel.centerYAnchor.constraint(equalTo: centerYAnchor)
        ])
    }

    func configure(with productOrder: ProductOrder) {
        productNameLabel.text = productOrder.productName
        quantityLabel.text = "Qty: \(productOrder.quantity)"
    }
}
