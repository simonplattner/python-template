import unittest

from src.template.template import increment


class TestTemplate(unittest.TestCase):
    def test_increment(self):
        self.assertEqual(increment(1), 2)


if __name__ == '__main__':
    unittest.main()
