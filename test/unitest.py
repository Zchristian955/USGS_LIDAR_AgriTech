import unittest
import sys, os

class TestCountOccurence(unittest.TestCase):
    def test_count_occurence(self):
        """
        Test that it returns the count of each unique values in the given list
        """
        data = [0,0,9,0,8,9,0,7]
        result = count_occurence(data)
        output = {0: 4, 9: 2, 8: 1, 7: 1}
        self.assertAlmostEqual(result, output)
