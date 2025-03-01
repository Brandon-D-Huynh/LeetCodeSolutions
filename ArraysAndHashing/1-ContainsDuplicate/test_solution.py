import unittest
from solution import Solution

class TestHasDuplicate(unittest.TestCase):
    def setUp(self):
        # Create a new Solution instance for each test
        self.sol = Solution()

    def test_empty_array(self):
        # Empty array has no duplicates
        self.assertFalse(self.sol.hasDuplicate([]))

    def test_single_element(self):
        # Single element array has no duplicates
        self.assertFalse(self.sol.hasDuplicate([5]))

    def test_no_duplicates(self):
        # Arrays with no duplicates
        self.assertFalse(self.sol.hasDuplicate([1, 2, 3, 4, 5]))
        self.assertFalse(self.sol.hasDuplicate([10, 20, 30, 40]))
        self.assertFalse(self.sol.hasDuplicate([-1, -2, -3, 0, 1, 2, 3]))

    def test_with_duplicates(self):
        # Arrays with duplicates
        self.assertTrue(self.sol.hasDuplicate([1, 2, 3, 1]))
        self.assertTrue(self.sol.hasDuplicate([1, 1, 2, 3]))
        self.assertTrue(self.sol.hasDuplicate([1, 2, 3, 4, 4]))
        self.assertTrue(self.sol.hasDuplicate([0, 0]))

    def test_negative_numbers(self):
        # Test with negative numbers
        self.assertTrue(self.sol.hasDuplicate([-1, -2, -1]))
        self.assertFalse(self.sol.hasDuplicate([-5, -4, -3, -2, -1]))

    def test_mixed_types(self):
        # While not normally used with this function, just making sure it handles mixed types
        # This could be removed if your function is strictly for integers
        self.assertTrue(self.sol.hasDuplicate([1, 1.0]))  # Note: 1 and 1.0 are considered equal in a set

    def test_large_arrays(self):
        # Test with larger arrays
        self.assertFalse(self.sol.hasDuplicate(list(range(1000))))
        self.assertTrue(self.sol.hasDuplicate(list(range(1000)) + [500]))

if __name__ == '__main__':
    unittest.main()