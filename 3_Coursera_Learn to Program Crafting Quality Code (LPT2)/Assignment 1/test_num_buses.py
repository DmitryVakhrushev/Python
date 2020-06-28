import a1 # it's a file name
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

# Add your test methods for a1.num_buses here.

# actual = fileName.functionName(parameters)
# fileName -- the name of the file that has a function itself.
    def test_numBuses_t1(self):
        ''' Test  num_buses with 0'''
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_numBuses_t2(self):
        ''' Test num_buses with 49 '''
        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(actual, expected)

    def test_numBuses_t3(self):
        ''' Test num_buses with 50 '''
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_numBuses_t4(self):
        ''' Test num_buses with 51 '''
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_numBuses_t5(self):
        ''' Test num_buses with 100 '''
        actual = a1.num_buses(100)
        expected = 2
        self.assertEqual(actual, expected)

    def test_numBuses_t6(self):
        ''' Test num_buses with 101 '''
        actual = a1.num_buses(101)
        expected = 3
        self.assertEqual(actual, expected)
        
if __name__ == '__main__':
    unittest.main(exit=False)
