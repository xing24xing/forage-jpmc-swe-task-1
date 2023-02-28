import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_results = [
      ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2),
      ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    ]
    for quote, expected in zip(quotes, expected_results):
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual((stock, bid_price, ask_price, price), expected)

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    expected_results = [
      ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2),
      ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2)
    ]

    for quote, expected in zip(quotes, expected_results):
      stock, bid_price, ask_price, price = getDataPoint(quote)
      self.assertEqual((stock, bid_price, ask_price, price), expected)

  """ ------------ Add more unit tests ------------ """

  def test_getRatio(self):
    self.assertEqual(getRatio(100, 200), 0.5)
    self.assertEqual(getRatio(200, 100), 2)
    self.assertEqual(getRatio(0, 100), 0)
    self.assertEqual(getRatio(100, 0), float('inf'))
if __name__ == '__main__':
    unittest.main()
