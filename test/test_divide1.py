import pytest
from src.caculate import *


class TestDivide():
    def test_divide(self):
        assert divide(10,5) == 2
        # divide(10,0)


