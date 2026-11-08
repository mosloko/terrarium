# Esempio 187 — logging catturabile nei test con assertLogs.
import logging
import unittest
class TestLog(unittest.TestCase):
    def test_info(self):
        with self.assertLogs(level="INFO") as registri:
            logging.info("evento demo")
        self.assertIn("evento demo", registri.output[0])
if __name__ == "__main__":
    unittest.main()
