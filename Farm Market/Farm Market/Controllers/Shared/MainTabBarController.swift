//
//  MainTabBarController.swift
//  Farm Market
//
//  Created by Nurgali on 19.11.2024.
//

import UIKit

final class MainTabBarController: UITabBarController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .systemBrown
        setupViewControllers()
    }
    
    
    func setupViewControllers() {
        let userRole = UserDefaults.standard.string(forKey: "userRole") ?? "Buyer"
        
        let homeVC: UIViewController
        let ordersVC: UIViewController
        let settingsVC =  SettingsViewController()
        
        if userRole == "Farmer" {
            print("FARMEER")
            homeVC = FarmerHomeViewController()
            ordersVC = FarmerOrdersViewController()
        } else {
            print("BUYERRR")
            homeVC = BuyerHomeViewController()
            ordersVC = BuyerOrdersViewController()
        }
        
        let homeNavController = UINavigationController(rootViewController: homeVC)
        let ordersNavController = UINavigationController(rootViewController: ordersVC)
        let settingsNavController = UINavigationController(rootViewController: settingsVC)
        
        
        homeNavController.tabBarItem = UITabBarItem(title: "Home", image: UIImage(systemName: "house"), tag: 0)
        ordersNavController.tabBarItem = UITabBarItem(title: "Orders", image: UIImage(systemName: "cart"), tag: 1)
        settingsNavController.tabBarItem = UITabBarItem(title: "Settings", image: UIImage(systemName: "gear"), tag: 2)
        
        viewControllers = [homeNavController, ordersNavController, settingsNavController]
        
    }
    
}
