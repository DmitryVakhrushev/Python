import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.


    def test_swap_t1(self):
        ''' Test swap_k with an empty string'''
        actual = a1.swap_k('',0)
        expected = ''
        self.assertEqual(actual, expected)
        
    def test_swap_t2(self):
        ''' Test swap_k with a one character string'''
        actual = a1.swap_k('a',0)
        expected = 'a'
        self.assertEqual(actual, expected)

    def test_swap_t3(self):
        ''' Test swap_k with a two character string'''
        actual = a1.swap_k('ab',0)
        expected = 'ab'
        self.assertEqual(actual, expected)

    def test_swap_t4(self):
        ''' Test swap_k with a two character string'''
        actual = a1.swap_k('ab',1)
        expected = 'ba'
        self.assertEqual(actual, expected)

    def test_swap_t5(self):
        ''' Test swap_k with a three character string'''
        actual = a1.swap_k('abc',0)
        expected = 'abc'
        self.assertEqual(actual, expected)

    def test_swap_t6(self):
        ''' Test swap_k with a three character string'''
        actual = a1.swap_k('abc',1)
        expected = 'cba'
        self.assertEqual(actual, expected)

    def test_swap_t7(self):
        ''' Test swap_k with a six character string'''
        actual = a1.swap_k('abcdef', 0)
        expected = 'abcdef'
        self.assertEqual(actual, expected)

    def test_swap_t8(self):
        ''' Test swap_k with a six character string'''
        actual = a1.swap_k('abcdef', 1)
        expected = 'fbcdea'
        self.assertEqual(actual, expected)

    def test_swap_t9(self):
        ''' Test swap_k with a six character string'''
        actual = a1.swap_k('abcdef', 2)
        expected = 'efcdab'
        self.assertEqual(actual, expected)

    def test_swap_t10(self):
        ''' Test swap_k with a six character string'''
        actual = a1.swap_k('abcdef', 3)
        expected = 'defabc'
        self.assertEqual(actual, expected)

    def test_swap_t11(self):
        ''' Test swap_k with a seven character string'''
        actual = a1.swap_k('abcdefg', 1)
        expected = 'gbcdefa'
        self.assertEqual(actual, expected)

    def test_swap_t12(self):
        ''' Test swap_k with a seven character string'''
        actual = a1.swap_k('abcdefg', 2)
        expected = 'fgcdeab'
        self.assertEqual(actual, expected)

    def test_swap_t13(self):
        ''' Test swap_k with a seven character string'''
        actual = a1.swap_k('abcdefg', 3)
        expected = 'efgdabc'
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
