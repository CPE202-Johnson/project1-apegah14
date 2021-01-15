import unittest
from  base_convert import *

class TestBaseConvert(unittest.TestCase):

    def test_base2(self):
        self.assertEqual(convert(45,2),"101101")
        self.assertEqual(convert(100, 2), "1100100")

    def test_base4(self):
        self.assertEqual(convert(30,4),"132")

    def test_base16(self):
        self.assertEqual(convert(316,16),"13C")
        self.assertEqual(convert(0, 16), "0")
        self.assertEqual(convert(150, 16), "96")
        self.assertEqual(convert(13, 16), "D")

    def test_base10(self):
        self.assertEqual(convert(316, 10), "316")

if __name__ == "__main__":
        unittest.main()