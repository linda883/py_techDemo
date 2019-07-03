# 参数化与数据驱动相同
import pytest


@pytest.fixture(params=[1, 2, 3])
def test_data(request):
    return request.param


def test_one(test_data):
    print('\ntest data: %s' % test_data)

