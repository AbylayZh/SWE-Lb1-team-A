import UIKit

class SettingsViewController: UIViewController {

    private let logoutButton = UIButton(type: .system)

    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }

    private func setupUI() {
        view.backgroundColor = .white
        navigationItem.title = "Settings"

        // Configure logout button
        logoutButton.setTitle("Log Out", for: .normal)
        logoutButton.titleLabel?.font = UIFont.boldSystemFont(ofSize: 18)
        logoutButton.backgroundColor = UIColor.systemRed
        logoutButton.tintColor = .white
        logoutButton.layer.cornerRadius = 8
        logoutButton.addTarget(self, action: #selector(logoutButtonTapped), for: .touchUpInside)

        // Add to view and set constraints
        view.addSubview(logoutButton)
        logoutButton.snp.makeConstraints { make in
            make.center.equalToSuperview()
            make.leading.trailing.equalToSuperview().inset(50)
            make.height.equalTo(50)
        }
    }

    @objc private func logoutButtonTapped() {
        // Handle logout logic
        logoutUser()
    }

    private func logoutUser() {
        // Clear authentication state
        UserDefaults.standard.set(false, forKey: "isLoggedIn")
        UserDefaults.standard.removeObject(forKey: "userRole")

        // Optionally, clear any stored tokens or user data

        // Navigate back to LoginViewController
        if let window = UIApplication.shared.windows.first {
            let loginVC = LoginViewController()
            let navController = UINavigationController(rootViewController: loginVC)
            window.rootViewController = navController
            UIView.transition(with: window, duration: 0.5, options: .transitionFlipFromLeft, animations: nil, completion: nil)
        }
    }
}
