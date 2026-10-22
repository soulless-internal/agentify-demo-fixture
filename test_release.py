import unittest
from release import release_total_cents

class ReleaseCheck(unittest.TestCase):
    def test_empty_order(self):
        self.assertEqual(release_total_cents([]), 0)

    def test_single_unit(self):
        self.assertEqual(release_total_cents([(1250, 1)]), 1250)

    def test_quantity_is_included(self):
        self.assertEqual(release_total_cents([(1250, 3), (500, 2)]), 4750)

if __name__ == '__main__':
    unittest.main()
