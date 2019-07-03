import pytest


# conftest文件名是不能换的，这个文件是全局的数据共享的地方，全局的配置和前期工作都可以写在这里
@pytest.fixture()
def login():
    print("\n输入用户名密码登陆！C")

