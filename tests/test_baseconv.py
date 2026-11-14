import unittest

from baseconv import parse, render


class BaseTest(unittest.TestCase):
    def test_hex(self):
        self.assertEqual(parse("0xff"), 255)
        self.assertEqual(render(255, 16), "ff")

    def test_round_trip(self):
        for n in (0, 1, -42, 4096):
            self.assertEqual(parse(render(n, 36), 36), n)

    def test_bad_base(self):
        with self.assertRaises(ValueError):
            render(1, 40)


if __name__ == "__main__":
    unittest.main()
