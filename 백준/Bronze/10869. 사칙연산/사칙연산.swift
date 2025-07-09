//
//  main.swift
//  swift_Algorithm
//
//  Created by SeongYongSong on 7/8/25.
//

import Foundation

let numbers = readLine()!.split(separator: " ").map { Int($0)! }
let a = numbers[0]
let b = numbers[1]

print("\(a+b)")
print("\(a-b)")
print("\(a*b)")
print("\(a/b)")
print("\(a%b)")

