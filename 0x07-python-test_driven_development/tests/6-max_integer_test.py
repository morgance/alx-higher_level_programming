#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """unittest class for mat_integer"""

    def test_module_docstring(self):
        """Tests for module docsting"""
        module = __import__('6-max_integer').__doc__
        self.assertTrue(len(module) > 1)

    def test_function_docstring(self):
        """Tests for funstion docstring"""
        function = max_integer.__doc__
        self.assertTrue(len(function) > 1)

    def test_none(self):
        """Tests for passing none as argument"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == "__main__":
    unittest.main()
