import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

    def test_getDataPoint_calculatePrice(self):
        # Arrange
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        expected_results = [
            ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),  # 120.84
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)  # 119.775
        ]

        # Act & Assert
        for quote, expected in zip(quotes, expected_results):
            result = getDataPoint(quote)
            self.assertEqual(result, expected)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        # Arrange
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        expected_results = [
            ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),  # 119.84
            ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)  # 119.775
        ]

        # Act & Assert
        for quote, expected in zip(quotes, expected_results):
            result = getDataPoint(quote)
            self.assertEqual(result, expected)

    def test_getRatio(self):
        # Arrange
        test_cases = [
            (100, 200, 0.5),
            (200, 100, 2),
            (0, 100, 0),
            (100, 0, float('inf'))  # Assuming division by zero returns infinity
        ]

        # Act & Assert
        for price_a, price_b, expected_ratio in test_cases:
            result = getRatio(price_a, price_b)
            self.assertEqual(result, expected_ratio)

if __name__ == '__main__':
    unittest.main()
