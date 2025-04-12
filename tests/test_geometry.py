import unittest
from geometry.circle import area as circle_area
from geometry.rectangle import perimeter as rect_perimeter

class TestGeometry(unittest.TestCase):
    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(1.0), 3.14159, places=4)