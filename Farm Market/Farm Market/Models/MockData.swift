//
//  MockData.swift
//  Farm Market
//
//  Created by Nurgali on 19.11.2024.
//

import Foundation
import UIKit


class MockData {
    static let shared = MockData()
    
    func getFarmerProducts() -> [Product] {
        // Return an array of Product instances
        return [
            Product(id: "1", name: "Apple", category: "Fruits", price: 1.5, quantity: 100, description: "Fresh apples", imageURLs: "https://assets.bonappetit.com/photos/57daf2c35a14a530086efae5/master/pass/green-apple-640.jpg"),
            Product(id: "2", name: "Carrot", category: "Vegetables", price: 0.5, quantity: 200, description: "Organic carrots", imageURLs: "https://t4.ftcdn.net/jpg/02/28/90/67/360_F_228906712_r4bb71gSmKvyDHq54JvjXAhKWpQiqWvX.jpg")
        ]
    }
    
    func getAllProducts() -> [Product] {
        // Return an array of Product instances available in the marketplace
        return [
            // Products from various farmers
            Product(id: "1", name: "Apples", category: "Fruits", price: 1.5, quantity: 100, description: "Fresh apples from Farm A", imageURLs: "https://assets.bonappetit.com/photos/57daf2c35a14a530086efae5/master/pass/green-apple-640.jpg"),
            Product(id: "2", name: "Bananas", category: "Fruits", price: 0.8, quantity: 150, description: "Organic bananas", imageURLs: "https://t4.ftcdn.net/jpg/02/28/90/67/360_F_228906712_r4bb71gSmKvyDHq54JvjXAhKWpQiqWvX.jpg"),
            Product(id: "3", name: "Carrots", category: "Vegetables", price: 0.5, quantity: 200, description: "Crunchy carrots from Farm B", imageURLs: "https://images.seattletimes.com/wp-content/uploads/2024/04/04082024_OpEd-Potatoes_124536.jpg?d=2040x1488"),
            
        ]
    }
    
    
}
