# Esempio 182 — Testare che input errati producano l'eccezione attesa.
import unittest
class TestValidazione(unittest.TestCase):
    def test_eta_negativa(self):
        with self.assertRaises(ValueError):
            raise ValueError("demo")
if __name__ == "__main__":
    unittest.main()
