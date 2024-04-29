from Lab2.bmi import calculate_bmi

def test_bmi_under_weight():
     assert calculate_bmi(height=1.73, weight=43) == -1


def test_bmi_normal_weight():
     assert calculate_bmi(height=1.73, weight=70) == 0


def test_bmi_over_weight():
     assert calculate_bmi(height=1.73, weight=85) == 1