import unittest

from app.square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4), 16)
        self.assertEqual(area(2.5), 6.25)

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)
        self.assertEqual(perimeter(2.5), 10)

    def test_zero_side(self):
        self.assertEqual(area(0), 0)
        self.assertEqual(perimeter(0), 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError):
            area(-4)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError):
            perimeter(-4)

    def test_invalid_type(self):
        with self.assertRaises(TypeError):
            area(None)
        with self.assertRaises(TypeError):
            perimeter(None)

    def test_string_type(self):
        with self.assertRaises(TypeError):
            area("4")
        with self.assertRaises(TypeError):
            perimeter("4")


if __name__ == "__main__":
    unittest.main()
