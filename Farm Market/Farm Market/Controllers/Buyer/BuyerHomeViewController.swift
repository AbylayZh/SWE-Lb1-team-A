import UIKit

class BuyerHomeViewController: UIViewController {
    
    // MARK: - Properties
    
    var products: [Product] = []
    var filteredProducts: [Product] = []
    let collectionView: UICollectionView
    let searchController = UISearchController(searchResultsController: nil)
    
    // MARK: - Initialization
    
    init() {
        // Initialize collectionView with a flow layout
        let layout = UICollectionViewFlowLayout()
        let itemWidth = (UIScreen.main.bounds.width - 30) / 2
        layout.itemSize = CGSize(width: itemWidth, height: itemWidth + 60)
        layout.sectionInset = UIEdgeInsets(top: 10, left: 10, bottom: 10, right: 10)
        collectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)
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
        loadProducts()
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        setupNavigationBar()
        setupCollectionView()
        setupSearchController()
    }
    
    private func setupNavigationBar() {
        navigationItem.title = "Marketplace"
        navigationItem.searchController = searchController
        navigationItem.hidesSearchBarWhenScrolling = false
    }
    
    private func setupCollectionView() {
        view.addSubview(collectionView)
        collectionView.register(ProductCollectionCell.self, forCellWithReuseIdentifier: "ProductCollectionCell")
        collectionView.delegate = self
        collectionView.dataSource = self
        
        // Layout constraints
        collectionView.snp.makeConstraints { make in
            make.edges.equalToSuperview()
        }
    }
    
    private func setupSearchController() {
        searchController.searchResultsUpdater = self
        searchController.obscuresBackgroundDuringPresentation = false
        searchController.searchBar.placeholder = "Search Products"
        definesPresentationContext = true
    }
    
    // MARK: - Data Loading
    
    private func loadProducts() {
        // For now, load products from mock data
        products = MockData.shared.getAllProducts()
        filteredProducts = products
        collectionView.reloadData()
    }
}

// MARK: - UICollectionViewDelegate and UICollectionViewDataSource

extension BuyerHomeViewController: UICollectionViewDelegate, UICollectionViewDataSource {
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return filteredProducts.count
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {

        guard let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "ProductCollectionCell", for: indexPath) as? ProductCollectionCell else {
            return UICollectionViewCell()
        }

        let product = filteredProducts[indexPath.item]
        cell.configure(with: product)
        return cell
    }
    
    func collectionView(_ collectionView: UICollectionView, didSelectItemAt indexPath: IndexPath) {
        let productDetailVC = ProductDetailViewController(product: filteredProducts[indexPath.item])
        navigationController?.pushViewController(productDetailVC, animated: true)
    }
}

// MARK: - UISearchResultsUpdating

extension BuyerHomeViewController: UISearchResultsUpdating {
    func updateSearchResults(for searchController: UISearchController) {
        filterProducts(for: searchController.searchBar.text)
    }
    
    private func filterProducts(for query: String?) {
        if let query = query, !query.isEmpty {
            filteredProducts = products.filter { $0.name.lowercased().contains(query.lowercased()) }
        } else {
            filteredProducts = products
        }
        collectionView.reloadData()
    }
}
