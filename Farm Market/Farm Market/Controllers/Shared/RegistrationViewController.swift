import UIKit
import SnapKit

class RegistrationViewController: UIViewController {
    
    // MARK: - UI Elements
    
    private let roleSegmentedControl: UISegmentedControl = {
        let sc = UISegmentedControl(items: ["Farmer", "Buyer"])
        sc.selectedSegmentIndex = 0
        sc.addTarget(self, action: #selector(roleChanged(_:)), for: .valueChanged)
        return sc
    }()
    
    // Common fields
    private let firstNameTextField = UITextField()
    private let lastNameTextField = UITextField()
    private let emailTextField = UITextField()
    private let phoneTextField = UITextField()
    private let passwordTextField = UITextField()
    private let confirmPasswordTextField = UITextField()
    
    // Farmer-specific fields
    private let farmSizeTextField = UITextField()
    private let farmAddressTextField = UITextField()
    
    // Buyer-specific fields
    private let deliveryAddressTextField = UITextField()
    private let preferredPaymentTextField = UITextField()
    
    private let registerButton = UIButton(type: .system)
    
    // Stack views
    private let commonFieldsStackView = UIStackView()
    private let farmerFieldsStackView = UIStackView()
    private let buyerFieldsStackView = UIStackView()
    
    // MARK: - Lifecycle
    
    override func viewDidLoad() {
        super.viewDidLoad()
        setupUI()
        updateUIForSelectedRole()
    }
    
    // MARK: - UI Setup
    
    private func setupUI() {
        view.backgroundColor = .white
        setupSegmentedControl()
        setupTextFields()
        setupRegisterButton()
        setupStackViews()
        layoutUI()
    }
    
    private func setupSegmentedControl() {
        view.addSubview(roleSegmentedControl)
    }
    
    private func setupTextFields() {
        firstNameTextField.placeholder = "First Name"
        firstNameTextField.borderStyle = .roundedRect
        
        lastNameTextField.placeholder = "Last Name"
        lastNameTextField.borderStyle = .roundedRect
        
        emailTextField.placeholder = "Email"
        emailTextField.borderStyle = .roundedRect
        emailTextField.autocapitalizationType = .none
        emailTextField.keyboardType = .emailAddress
        
        phoneTextField.placeholder = "Phone"
        phoneTextField.borderStyle = .roundedRect
        phoneTextField.keyboardType = .numberPad
        
        passwordTextField.placeholder = "Password"
        passwordTextField.borderStyle = .roundedRect
        passwordTextField.textContentType = .oneTimeCode
        passwordTextField.isSecureTextEntry = true
        
        confirmPasswordTextField.placeholder = "Confirm Password"
        confirmPasswordTextField.borderStyle = .roundedRect
        confirmPasswordTextField.isSecureTextEntry = true
        
        // Farmer fields
        farmSizeTextField.placeholder = "Farm Size"
        farmSizeTextField.borderStyle = .roundedRect
        farmSizeTextField.keyboardType = .numberPad
        
        farmAddressTextField.placeholder = "Farm Address"
        farmAddressTextField.borderStyle = .roundedRect
        
        // Buyer fields
        deliveryAddressTextField.placeholder = "Delivery Address"
        deliveryAddressTextField.borderStyle = .roundedRect
        
        preferredPaymentTextField.placeholder = "Preferred Payment"
        preferredPaymentTextField.borderStyle = .roundedRect
        preferredPaymentTextField.keyboardType = .numberPad
    }
    
    private func setupRegisterButton() {
        registerButton.setTitle("Register", for: .normal)
        registerButton.titleLabel?.font = UIFont.boldSystemFont(ofSize: 18)
        registerButton.backgroundColor = UIColor.systemBlue
        registerButton.tintColor = .white
        registerButton.layer.cornerRadius = 8
        registerButton.addTarget(self, action: #selector(registerButtonTapped), for: .touchUpInside)
    }
    
    private func setupStackViews() {
        commonFieldsStackView.axis = .vertical
        commonFieldsStackView.spacing = 10
        commonFieldsStackView.addArrangedSubview(firstNameTextField)
        commonFieldsStackView.addArrangedSubview(lastNameTextField)
        commonFieldsStackView.addArrangedSubview(emailTextField)
        commonFieldsStackView.addArrangedSubview(phoneTextField)
        commonFieldsStackView.addArrangedSubview(passwordTextField)
        commonFieldsStackView.addArrangedSubview(confirmPasswordTextField)
        
        farmerFieldsStackView.axis = .vertical
        farmerFieldsStackView.spacing = 10
        farmerFieldsStackView.addArrangedSubview(farmSizeTextField)
        farmerFieldsStackView.addArrangedSubview(farmAddressTextField)
        
        buyerFieldsStackView.axis = .vertical
        buyerFieldsStackView.spacing = 10
        buyerFieldsStackView.addArrangedSubview(deliveryAddressTextField)
        buyerFieldsStackView.addArrangedSubview(preferredPaymentTextField)
    }
    
    private func layoutUI() {
        view.addSubview(commonFieldsStackView)
        view.addSubview(farmerFieldsStackView)
        view.addSubview(buyerFieldsStackView)
        view.addSubview(registerButton)
        
        roleSegmentedControl.snp.makeConstraints { make in
            make.top.equalTo(view.safeAreaLayoutGuide.snp.top).offset(20)
            make.leading.trailing.equalToSuperview().inset(20)
        }
        
        
        commonFieldsStackView.snp.makeConstraints { make in
            make.top.equalTo(roleSegmentedControl.snp.bottom).offset(20)
            make.leading.trailing.equalToSuperview().inset(20)
        }
        
        farmerFieldsStackView.snp.makeConstraints { make in
            make.top.equalTo(commonFieldsStackView.snp.bottom).offset(20)
            make.leading.trailing.equalToSuperview().inset(20)
        }
        
        buyerFieldsStackView.snp.makeConstraints { make in
            make.top.equalTo(commonFieldsStackView.snp.bottom).offset(20)
            make.leading.trailing.equalToSuperview().inset(20)
        }
        
        registerButton.snp.makeConstraints { make in
            make.top.equalTo(farmerFieldsStackView.snp.bottom).offset(30)
            make.leading.trailing.equalToSuperview().inset(50)
            make.height.equalTo(50)
        }
    }
    
    // MARK: - Actions
    
    @objc private func roleChanged(_ sender: UISegmentedControl) {
        updateUIForSelectedRole()
    }
    
    @objc private func registerButtonTapped() {
        let role = roleSegmentedControl.selectedSegmentIndex == 0 ? "Farmer" : "Buyer"
        
        // Validate common fields
        guard let firstName = firstNameTextField.text, !firstName.isEmpty,
              let lastName = lastNameTextField.text, !lastName.isEmpty,
              let email = emailTextField.text, !email.isEmpty,
              let phoneText = phoneTextField.text, let phone = Int(phoneText),
              let password = passwordTextField.text, !password.isEmpty,
              let confirmPassword = confirmPasswordTextField.text, !confirmPassword.isEmpty else {
            showAlert(message: "Please fill in all required fields.")
            return
        }
        
        guard password == confirmPassword else {
            showAlert(message: "Passwords do not match.")
            return
        }
        
        if role == "Farmer" {
            // Validate farmer fields
            guard let farmSizeText = farmSizeTextField.text, let farmSize = Int(farmSizeText),
                  let farmAddress = farmAddressTextField.text, !farmAddress.isEmpty else {
                showAlert(message: "Please fill in all farmer-specific fields.")
                return
            }
            
            // TODO: Remove temporary login simulation code when API is ready
            
            //            let requestBody: [String: Any] = [
            //                "first_name": firstName,
            //                "last_name": lastName,
            //                "email": email,
            //                "phone": phone,
            //                "password": password,
            //                "farm_size": farmSize,
            //                "farm_address": farmAddress
            //            ]
            //
            //            registerUser(endpoint: "/signup/farmer", requestBody: requestBody)
            
            // Simulate successful registration
            UserDefaults.standard.setValue(role, forKey: "userRole")
            UserDefaults.standard.setValue(true, forKey: "isLoggedIn")
            navigateToMainInterface()
            
        } else {
            // Validate buyer fields
            guard let deliveryAddress = deliveryAddressTextField.text, !deliveryAddress.isEmpty,
                  let preferredPaymentText = preferredPaymentTextField.text, let preferredPayment = Int(preferredPaymentText) else {
                showAlert(message: "Please fill in all buyer-specific fields.")
                return
            }
            
            // TODO: Remove temporary login simulation code when API is ready

            //            let requestBody: [String: Any] = [
            //                "first_name": firstName,
            //                "last_name": lastName,
            //                "email": email,
            //                "phone": phone,
            //                "password": password,
            //                "delivery_address": deliveryAddress,
            //                "preferred_payment": preferredPayment
            //            ]
            //
            //            registerUser(endpoint: "/signup/buyer", requestBody: requestBody)
            
            // Simulate successful registration
            UserDefaults.standard.setValue(role, forKey: "userRole")
            UserDefaults.standard.setValue(true, forKey: "isLoggedIn")
            navigateToMainInterface()
        }
    }
    
    private func navigateToMainInterface() {
        DispatchQueue.main.async {
            let mainTabBarController = MainTabBarController()
            if let window = UIApplication.shared.windows.first {
                window.rootViewController = mainTabBarController
                UIView.transition(with: window, duration: 0.5, options: .transitionCrossDissolve, animations: nil, completion: nil)
            }
        }
    }

    
    // MARK: - Networking
    
    private func registerUser(endpoint: String, requestBody: [String: Any]) {
        let url = URL(string: "https://your-api-base-url\(endpoint)")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        
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
                self.showAlert(title: "Success", message: "Registration successful. Please log in.") {
                    self.navigationController?.popViewController(animated: true)
                }
            case 409:
                self.showAlert(message: "Email already registered.")
            case 422:
                self.showAlert(message: "Invalid input data.")
            default:
                self.showAlert(message: "Unexpected error: \(httpResponse.statusCode)")
            }
        }
        task.resume()
    }
    
    // MARK: - Helper Methods
    
    private func updateUIForSelectedRole() {
        let isFarmer = roleSegmentedControl.selectedSegmentIndex == 0
        farmerFieldsStackView.isHidden = !isFarmer
        buyerFieldsStackView.isHidden = isFarmer
        
        // Update constraints
        registerButton.snp.remakeConstraints { make in
            if isFarmer {
                make.top.equalTo(farmerFieldsStackView.snp.bottom).offset(30)
            } else {
                make.top.equalTo(buyerFieldsStackView.snp.bottom).offset(30)
            }
            make.leading.trailing.equalToSuperview().inset(50)
            make.height.equalTo(50)
        }
    }
    
    private func showAlert(title: String = "Error", message: String, completion: (() -> Void)? = nil) {
        DispatchQueue.main.async {
            let alertController = UIAlertController(title: title, message: message, preferredStyle: .alert)
            let actionTitle = title == "Success" ? "OK" : "OK"
            alertController.addAction(UIAlertAction(title: actionTitle, style: .default, handler: { _ in
                completion?()
            }))
            self.present(alertController, animated: true, completion: nil)
        }
    }
}
