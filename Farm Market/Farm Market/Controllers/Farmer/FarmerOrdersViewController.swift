import UIKit

class FarmerOrdersViewController: UIViewController {

    // MARK: - Properties

    private var orders: [Order] = []

    private let tableView = UITableView()

    // MARK: - Lifecycle Methods

    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        configureNavigationBar()
        setupTableView()
        loadOrders()
    }

    // MARK: - UI Setup

    private func configureNavigationBar() {
        navigationItem.title = "Orders"
    }

    private func setupTableView() {
        view.addSubview(tableView)
        tableView.frame = view.bounds

        tableView.delegate = self
        tableView.dataSource = self

        tableView.register(OrderCell.self, forCellReuseIdentifier: "OrderCell")
    }

    // MARK: - Data Loading

    private func loadOrders() {
        // Simulate loading orders (Replace with actual data fetching)
        orders = [
            Order(id: "1", buyerName: "John Doe", products: [
                ProductOrder(productName: "Apples", quantity: 10),
                ProductOrder(productName: "Bananas", quantity: 5)
            ]),
            Order(id: "2", buyerName: "Jane Smith", products: [
                ProductOrder(productName: "Oranges", quantity: 8)
            ])
        ]

        tableView.reloadData()
    }
}

// MARK: - UITableViewDataSource

extension FarmerOrdersViewController: UITableViewDataSource {

    func numberOfSections(in tableView: UITableView) -> Int {
        return orders.count
    }

    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
         return orders[section].products.count
    }

    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {

        let order = orders[indexPath.section]
        let productOrder = order.products[indexPath.row]

        guard let cell = tableView.dequeueReusableCell(withIdentifier: "OrderCell", for: indexPath) as? OrderCell else {
            return UITableViewCell()
        }

        cell.configure(with: productOrder)
        return cell
    }
}

// MARK: - UITableViewDelegate

extension FarmerOrdersViewController: UITableViewDelegate {

    func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView? {
        let order = orders[section]
        let headerView = OrderHeaderView()
        headerView.configure(with: order)
        return headerView
    }

    func tableView(_ tableView: UITableView, heightForHeaderInSection section: Int) -> CGFloat {
        return 50
    }
}
