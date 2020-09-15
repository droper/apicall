"""
Nirvana Health Test.

The test solution is composed of:

1. The API mocked functions.

2. The selection function that chooses between the apis responses.

3. Tests for each function.
"""


class Api:
    """
    Mocked api functions.
    """

    __instance = None

    def func_api1(self, memberId):
        return {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000}

    def func_api2(self, memberId):
        return {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000}

    def func_api3(self, memberId):
        return {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000}

    def __new__(cls):
        if Api.__instance is None:
            Api.__instance = object.__new__(cls)
        return Api.__instance




