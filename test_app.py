import unittest
from app import greet, farewell

class TestApp(unittest.TestCase):

    def test_greet(self):
        result = greet("Naveen")
        self.assertIn("Naveen", result)
        self.assertIn("AIDI 2004", result)

    def test_farewell(self):
        result = farewell("Naveen")
        self.assertIn("Naveen", result)

if __name__ == "__main__":
    unittest.main()
