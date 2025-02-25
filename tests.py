import unittest

from first_largest import largest_element

class FirstLargest(unittest.TestCase):

    def test_largest_is_first(self):
        #given = [1,2,3,2,1]
        given = [5,3,4,1,2]
        expect = 5
        got = largest_element(given, loc=False)
        self.assertEqual(got, expect)
   
    """ ADD MORE  """
    def test_largest_is_first_with_location(self):
        #given = [1,2,3,2,1]
        given = [5,3,4,1,2]
        expect = 5,0
        got = largest_element(given, loc=True)
        self.assertEqual(got, expect)


    def sums(a):
        vals = 0
        #something about assertions


if __name__ == '__main__':
    unittest.main()
