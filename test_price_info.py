import price_info as price

def test_total_cost_shopping():
    expected_total_cost = (5 * 1.20) + (5 * 1.40) + (1 * 6.50) + (2 * 2.70) + (10 * 0.90) + (1 * 2.95) + (2 * 4.95)
    assert price.total_cost_shopping() == expected_total_cost

def test_cost_of_fruits():
    expected_cost_of_apple = 10 * 1.20
    assert price.cost_of_fruits('apple', 10) == expected_cost_of_apple

if __name__ == "__main__":
    test_total_cost_shopping()
    test_cost_of_fruits()
    print("All tests passed successfully!")
