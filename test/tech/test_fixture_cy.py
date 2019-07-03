import pytest
import pytest_sugar

# 在整个模块只做一次的事，范围是模块级别的。
# yield是调用第一次返回结果，第二次执行它下面的语句返回。


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，打开百度首页")

    yield

    print('执行teardown')
    print('最后关闭浏览器')


def test_s7(open):
    print('用例7，')


def test_s8(open):
    print('用例8，')


def test_s9(open):
    print('用例9，')


if __name__ == '__main__':
    pytest.main()
