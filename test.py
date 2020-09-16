"""
Tests
"""

import unittest

from api import Api
from main import api_call, select_response


class ApiTest(unittest.TestCase):

    def test_api1(self):
        a = Api()
        self.assertDictEqual(a.func_api1(1), {"deductible": 1000, "stop_loss": 10000,
                                              "oop_max": 5000})

    def test_api2(self):
        a = Api()
        self.assertDictEqual(a.func_api2(1), {"deductible": 1200, "stop_loss": 13000,
                                              "oop_max": 6000})

    def test_api3(self):
        a = Api()
        self.assertDictEqual(a.func_api3(1), {"deductible": 1000, "stop_loss": 10000,
                                              "oop_max": 6000})

    def test_select(self):
        a = Api()
        self.assertDictEqual(select_response([a.func_api1(1), a.func_api2(1), a.func_api3(1)]),
                             {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000})

    def test_call(self):
        a = Api()
        self.assertEqual(api_call(a), [{"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                                       {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                                       {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}])


if __name__ == '__main__':
    unittest.main()
