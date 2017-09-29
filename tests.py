""" Tests for freeCodeCamp intermediate algorithm scripting solutions
contained in fcc_algs_intermediate.py """

import unittest

import fcc_algs_intermediate as fai


class TestIntermediateAlgs(unittest.TestCase):

    def test_sum_all(self):
        """Test sum all numbers in range function."""
        self.assertEqual(10, fai.sum_all([1, 4]))
        self.assertEqual(10, fai.sum_all([4, 1]))
        self.assertEqual(45, fai.sum_all([5, 10]))
        self.assertEqual(45, fai.sum_all([10, 5]))

    def test_diff_array(self):
        """Test diff two arrays function."""
        diff_array_type = type(fai.diff_array([1, 2, 3, 5], [1, 2, 3, 4, 5]))
        self.assertTrue(diff_array_type == list)

        self.assertEqual(["pink wool"],
                         fai.diff_array(["diorite",
                                         "andesite",
                                         "grass",
                                         "dirt",
                                         "pink wool",
                                         "dead shrub"],
                                        ["diorite",
                                         "andesite",
                                         "grass",
                                         "dirt",
                                         "dead shrub"]))

        self.assertEqual(sorted(["diorite",
                                 "pink wool"]),
                         sorted(fai.diff_array(["andesite",
                                                "grass",
                                                "dirt",
                                                "pink wool",
                                                "dead shrub"],
                                               ["diorite",
                                                "andesite",
                                                "grass",
                                                "dirt",
                                                "dead shrub"])))

        self.assertEqual([],
                         fai.diff_array(["andesite",
                                         "grass",
                                         "dirt",
                                         "dead shrub"],
                                        ["andesite",
                                         "grass",
                                         "dirt",
                                         "dead shrub"]))

        self.assertEqual([4],
                         fai.diff_array([1, 2, 3, 5],
                                        [1, 2, 3, 4, 5]))

        self.assertEqual(sorted(["piglet",
                                 4]),
                         sorted(fai.diff_array([1,
                                                "calf",
                                                3,
                                                "piglet"],
                                               [1,
                                                "calf",
                                                3,
                                                4])))

        self.assertEqual(sorted(["snuffleupagus",
                                 "cookie monster",
                                 "elmo"]),
                         sorted(fai.diff_array([],
                                               ["snuffleupagus",
                                                "cookie monster",
                                                "elmo"])))

        self.assertEqual(sorted([1,
                                 "calf",
                                 3,
                                 "piglet",
                                 7,
                                 "filly"]),
                         sorted(fai.diff_array([1,
                                                "calf",
                                                3,
                                                "piglet"],
                                               [7,
                                                "filly"])))


if __name__ == '__main__':
    unittest.main()
