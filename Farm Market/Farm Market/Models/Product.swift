//
//  Product.swift
//  Farm Market
//
//  Created by Nurgali on 19.11.2024.
//

import UIKit
import Foundation

struct Product: Codable {
    var id: String
    var name: String
    var category: String
    var price: Double
    var quantity: Int
    var description: String
    var imageURLs: String
}

