# Esempio 181 — unittest è incluso in Python per test ripetibili.
import unittest
class TestSomma(unittest.TestCase):
    def test_somma(self):
        self.assertEqual(2 + 3, 5)
if __name__ == "__main__":
    unittest.main()
