import unittest

def FibonacciFn(val):
    if val <= 0: 
        return 0
    elif val == 1:
        return 1
    else:
        return FibonacciFn(val - 1) + FibonacciFn(val - 2)

class Tests(unittest.TestCase):
    def test_right_result(self):
        rightValue = 55
        testValue = 10
        testResult = FibonacciFn(testValue)
        self.assertEqual(rightValue, testResult)

    def test_first_value_f0_is_zero(self):
        right_value = 0
        test_value = 0
        test_result = FibonacciFn(test_value)
        self.assertEqual(right_value, test_result)

    def test_first_value_f1_is_zero(self):
        right_value = 1
        test_value = 1
        test_result = FibonacciFn(test_value)
        self.assertEqual(right_value, test_result)

    def test_must_return_zero_when_negative_value_comes(self):
        right_value = 0
        test_value = -1
        test_result = FibonacciFn(test_value)
        self.assertEqual(right_value, test_result)