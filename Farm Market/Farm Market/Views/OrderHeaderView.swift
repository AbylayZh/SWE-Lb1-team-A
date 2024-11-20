import UIKit

class OrderHeaderView: UIView {

    private let buyerNameLabel = UILabel()

    override init(frame: CGRect) {
        super.init(frame: frame)
        setupUI()
    }

    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    private func setupUI() {
        addSubview(buyerNameLabel)

        buyerNameLabel.translatesAutoresizingMaskIntoConstraints = false

        NSLayoutConstraint.activate([
            buyerNameLabel.leadingAnchor.constraint(equalTo: leadingAnchor, constant: 16),
            buyerNameLabel.trailingAnchor.constraint(equalTo: trailingAnchor, constant: -16),
            buyerNameLabel.centerYAnchor.constraint(equalTo: centerYAnchor)
        ])

        backgroundColor = UIColor.systemGray6
    }

    func configure(with order: Order) {
        buyerNameLabel.text = "Buyer: \(order.buyerName)"
    }
}
