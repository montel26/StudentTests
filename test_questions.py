import unittest

class TestPythonProblems(unittest.TestCase):
    
    # Test for Two Sum Problem
    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])
    
    # Test for Remove Duplicates from Sorted Array
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([1, 1, 2]), 2)
        self.assertEqual(remove_duplicates([0, 0, 1, 1, 2, 3, 3]), 4)
    
    # Test for Reverse an Array
    def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
    
    # Test for Find Maximum in an Array
    def test_find_max(self):
        self.assertEqual(find_max([2, 4, 1, 6, 8, 5]), 8)
    
    # Test for Find Minimum in an Array
    def test_find_min(self):
        self.assertEqual(find_min([2, 4, 1, 6, 8, 5]), 1)
    
    # Test for Check for Palindrome
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertFalse(is_palindrome("hello"))
    
    # Test for Find First Unique Character in a String
    def test_first_unique_char(self):
        self.assertEqual(first_unique_char("leetcode"), 0)
        self.assertEqual(first_unique_char("loveleetcode"), 2)
        self.assertEqual(first_unique_char("aabb"), -1)
    
    # Test for Fibonacci Sequence
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(6), 8)
    
    # Test for Find Common Elements in Two Arrays
    def test_find_common_elements(self):
        self.assertEqual(find_common_elements([1, 2, 3, 4], [3, 4, 5, 6]), [3, 4])
    
    # Test for Move Zeroes to End
    def test_move_zeroes(self):
        self.assertEqual(move_zeroes([0, 1, 0, 3, 12]), [1, 3, 12, 0, 0])
    
    # Test for Count Vowels in a String
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels("HELLO WORLD"), 3)
    
    # Test for Merge Two Sorted Arrays
    def test_merge_sorted_arrays(self):
        self.assertEqual(merge_sorted_arrays([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    unittest.main()
