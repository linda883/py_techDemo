import pytest


# 不带参数时scope="function"
# 有个依赖关系，先登陆，与其他功能有依赖。
@pytest.fixture()
def login():
    print("\n输入用户名密码登陆！")

def test_s1(login):
    print('用例1，登陆后执行其它功能操作1')

def test_s2():
    print('用例2，不登陆后执行其它功能操作2')

def test_s3(login):
    print('用例3，登陆后执行其它功能操作3')


if __name__ == '__main__':
    pytest.main
