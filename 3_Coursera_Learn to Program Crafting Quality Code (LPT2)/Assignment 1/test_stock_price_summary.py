import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.

    def test_StockPrice_t1(self):
       ''' Test  stock_price_summary with an empty list'''
       actual = a1.stock_price_summary([])
       expected = (0, 0)
       self.assertEqual(actual, expected)

    def test_StockPrice_t2(self):
       ''' Test  stock_price_summary with 0'''
       actual = a1.stock_price_summary([0])
       expected = (0, 0)
       self.assertEqual(actual, expected)

    def test_StockPrice_t3(self):
        ''' Test  stock_price_summary with two negatives'''
        actual = a1.stock_price_summary([0, 0])
        expected = (0, 0)
        self.assertEqual(actual, expected)

    def test_StockPrice_t4(self):
        ''' Test  stock_price_summary with two negatives'''
        actual = a1.stock_price_summary([-1.05, -0.4])
        expected = (0, -1.45)
        self.assertEqual(actual, expected)

    def test_StockPrice_t5(self):
        ''' Test  stock_price_summary with two positives'''
        actual = a1.stock_price_summary([1.13, 0.2])
        expected = (1.33, 0)
        self.assertEqual(actual, expected)
        
    def test_StockPrice_t6(self):
        ''' Test  stock_price_summary with more than 2 ALL negative numbers'''
        actual = a1.stock_price_summary([-1,-5.2,-4,-0.7])
        expected = (0, -10.9)
        self.assertEqual(actual, expected)

    def test_StockPrice_t7(self):
        ''' Test  stock_price_summary with more then 2 ALL positive numbers'''
        actual = a1.stock_price_summary([3.4, 1.2, 5])
        expected = (9.6, 0)
        self.assertEqual(actual, expected)

    def test_StockPrice_t8(self):
        ''' Test  stock_price_summary with different numbers'''
        actual = a1.stock_price_summary([-1.3, 0.2, 1.5, -0.2, -0.7, 0.8])
        expected = (2.5, -2.2)
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
