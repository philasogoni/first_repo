import unittest
from challenge1 import FirstReverse

class TestFirstReverse(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(FirstReverse(""), "")
        
    def test_single_character(self):
        self.assertEqual(FirstReverse("a"), "a")
    
    def test_palindrome(self):
        self.assertEqual(FirstReverse("racecar"), "racecar")
        
    def test_regular_string(self):
        self.assertEqual(FirstReverse("hello"), "olleh")
    
    def test_string_with_spaces(self):
        self.assertEqual(FirstReverse("hello world"), "dlrow olleh")
    
    def test_string_with_special_characters(self):
        self.assertEqual(FirstReverse("12345!"), "!54321")
    
    def test_mixed_case_string(self):
        self.assertEqual(FirstReverse("HelloWorld"), "dlroWolleH")
    
    def test_string_with_numbers(self):
        self.assertEqual(FirstReverse("12345"), "54321")
    
if __name__ == '__main__':
    unittest.main()