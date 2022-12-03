from  main import main
import unittest


class TestReverse(unittest.TestCase):
    def testcheck(self):
        self.assertEqual(main("..."), "")


if __name__ == '__main__':
    unittest.main()