import unittest

from ..mystery_1 import mystery_1

class TestMystery1(unittest.TestCase):
    """Unit tests for the mystery_1 function  """

    def test_minimal_input(self):
        """Test that mystery_1 returns 0 when both inputs are 0"""
        self.assertEqual(mystery_1(0, 0), 0)
    def test_positive_inputs(self):
        """Test that mystery_1 works with positive numbers."""
        self.assertEqual(mystery_1(3, 5), 8)

    def test_negative_inputs(self):
        """Test that mystery_1 works with negative numbers."""
        self.assertEqual(mystery_1(-3, -5), -8)

    def test_mixed_sign_inputs(self):
        """Test that mystery_1 works with mixed sign inputs."""
        self.assertEqual(mystery_1(-3, 5), 2)
