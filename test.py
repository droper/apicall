"""
Tests
"""

import unittest

from api import Api


class ApiTest(unittest.TestCase):

    def test_api1(self):
        a = Api()
        self.assertEqual(a.func_api1(1), {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000})

    def test_api2(self):
        a = Api()
        self.assertEqual(a.func_api2(1), {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000})

    def test_api3(self):
        a = Api()
        self.assertEqual(a.func_api3(1), {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000})

if __name__ == '__main__':
    unittest.main()