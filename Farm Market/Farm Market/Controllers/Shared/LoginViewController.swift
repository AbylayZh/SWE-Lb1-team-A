import UIKit

class LoginViewController: UIViewController {
    
    // MARK: - UI Elements
    
    private let emailTextField = UITextField()
    private let passwordTextField = UITextField()
    private let loginButton = UIButton(type: .system)
    private let registerButton = UIButton(type: .system)
    
    // MARK: - Lifecycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        view.backgroundColor = .white
        setupTextFields()
        setupButtons()
        layoutUI()
    }
    
    private func setupTextFields() {
        emailTextField.placeholder = "Email"
        emailTextField.borderStyle = .roundedRect
        emailTextField.autocapitalizationType = .none
        emailTextField.keyboardType = .emailAddress
        
        passwordTextField.placeholder = "Password"
        passwordTextField.borderStyle = .roundedRect
        passwordTextField.isSecureTextEntry = true
    }
    
    private func setupButtons() {
        loginButton.setTitle("Login", for: .normal)
        loginButton.titleLabel?.font = UIFont.boldSystemFont(ofSize: 18)
        loginButton.backgroundColor = UIColor.systemBlue
        loginButton.tintColor = .white
        loginButton.layer.cornerRadius = 8
        loginButton.addTarget(self, action: #selector(loginButtonTapped), for: .touchUpInside)
        
        registerButton.setTitle("Don't have an account? Register", for: .normal)
        registerButton.setTitleColor(.systemBlue, for: .normal)
        registerButton.addTarget(self, action: #selector(registerButtonTapped), for: .touchUpInside)
    }
    
    private func layoutUI() {
        let stackView = UIStackView(arrangedSubviews: [emailTextField, passwordTextField, loginButton, registerButton])
        stackView.axis = .vertical
        stackView.spacing = 15
        
        view.addSubview(stackView)
        
        stackView.snp.makeConstraints { make in
            make.center.equalToSuperview()
            make.leading.trailing.equalToSuperview().inset(30)
        }
        
        loginButton.snp.makeConstraints { make in
            make.height.equalTo(50)
        }
    }
    
    // MARK: - Actions
    
    @objc private func loginButtonTapped() {
        // Handle login logic
        guard let email = emailTextField.text, !email.isEmpty,
              let password = passwordTextField.text, !password.isEmpty else {
            showAlert(message: "Please enter your email and password.")
            return
        }
        
        loginUser(email: email, password: password)
    }
    
    @objc private func registerButtonTapped() {
        let registrationVC = RegistrationViewController()
        navigationController?.pushViewController(registrationVC, animated: true)
    }
    
    // MARK: - Networking
    
    private func loginUser(email: String, password: String) {
        let url = URL(string: "https://your-api-base-url/login")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        
        let requestBody = ["email": email, "password": password]
        
        do {
            request.httpBody = try JSONSerialization.data(withJSONObject: requestBody, options: [])
        } catch {
            showAlert(message: "Failed to encode request.")
            return
        }
        
        request.addValue("application/json", forHTTPHeaderField: "Content-Type")
        
        // Perform the request
        let task = URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                self.showAlert(message: "Network error: \(error.localizedDescription)")
                return
            }
            
            guard let httpResponse = response as? HTTPURLResponse else {
                self.showAlert(message: "Invalid server response.")
                return
            }
            
            switch httpResponse.statusCode {
            case 303:
                // Success
                self.navigateToMainInterface()
            case 401:
                self.showAlert(message: "Invalid email or password.")
            default:
                self.showAlert(message: "Unexpected error: \(httpResponse.statusCode)")
            }
        }
        task.resume()
    }
    
    // MARK: - Helper Methods
    
    private func navigateToMainInterface() {
        DispatchQueue.main.async {
            // Save authentication state if needed
            UserDefaults.standard.set(true, forKey: "isLoggedIn")
            
            // Transition to the main interface
            let mainTabBarController = MainTabBarController()
            if let window = UIApplication.shared.windows.first {
                window.rootViewController = mainTabBarController
                UIView.transition(with: window, duration: 0.5, options: .transitionCrossDissolve, animations: nil, completion: nil)
            }
        }
    }
    
    private func showAlert(title: String = "Error", message: String) {
        DispatchQueue.main.async {
            let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)
            alertController.addAction(UIAlertAction(title: "OK", style: .default, handler: nil))
            self.present(alertController, animated: true, completion: nil)
        }
    }
}
