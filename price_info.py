price_list = {'apple': 1.20, 'orange': 1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear': 0.90, 'papaya': 2.95, 'pomegranate': 4.95}
quantity_list = {'apple': 5, 'orange': 5, 'watermelon': 1, 'pineapple': 2, 'pear': 10, 'papaya': 1, 'pomegranate': 2}

def total_cost_shopping():
    total_cost = 0
    for fruit, price in price_list.items():  
        if fruit in quantity_list:  
            total_cost += quantity_list[fruit] * price  

    return total_cost

def cost_of_fruits(fruit, quantity):
    cost = 0
    for key in price_list.keys():
        if key == fruit:
            cost = quantity * price_list[key]
            break

    return cost

def main():
    cost_of_fruits('apple', 10)
    total_cost_shopping()

if __name__ == "__main__":
    main()

def test_total_cost_shopping():
    expected_total_cost = (5 * 1.20) + (5 * 1.40) + (1 * 6.50) + (2 * 2.70) + (10 * 0.90) + (1 * 2.95) + (2 * 4.95)
    assert total_cost_shopping() == expected_total_cost

def test_cost_of_fruits():
    expected_cost_of_apple = 10 * 1.20
    assert cost_of_fruits('apple', 10) == expected_cost_of_apple

if __name__ == "__main__":
    test_total_cost_shopping()
    test_cost_of_fruits()
    print("All tests passed successfully!")
