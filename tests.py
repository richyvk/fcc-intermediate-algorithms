""" Tests for freeCodeCamp intermediate algorithm scripting solutions contained in fcc_algs_intermediate.py """

import unittest


class TestIntermediateAlgs(unittest.TestCase):

    def test_sum_all(self):
	    """Test sum all numbers in range function."""
		self.assertEqual(10, sum_all([1, 4])
		self.assertEqual(10, sum_all([4, 1])
		self.assertEqual(45, sum_all([5, 10])
		self.assertEqual(45, sum_all([10, 5])
	
	
	def test_diff_array(self):
        """Test diff two arrays function."""
        self.assertTrue(type(diff_array([1, 2, 3, 5], [1, 2, 3, 4, 5])) == list)
        self.assertEqual(["pink wool"], 
                         diff_array(["diorite", "andesite", "grass",
                                     "dirt", "pink wool", "dead shrub"],
                                    ["diorite", "andesite", "grass",
                                     "dirt", "dead shrub"])
        self.assertEqual(sorted(["diorite", "pink wool"]),
                         sorted(diff_array(["andesite", "grass", "dirt",
                                            "pink wool", "dead shrub"],
                                           ["diorite", "andesite", "grass",
                                            "dirt", "dead shrub"]))
