import pytest
import allure


@allure.description_html("""
<h1>Test with some complicated html description</h1>
<table style="width:100%">
  <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    <th>Age</th>
  </tr>
  <tr align="center">
    <td>linda</td>
    <td>Smith</td>
    <td>18</td>
  </tr>
  <tr align="center">
    <td>fang</td>
    <td>Jackson</td>
    <td>88</td>
  </tr>
</table>
""")
def test_demo2():
    assert True


@allure.description("""简单的计算""")
@allure.title("测试加法 计算")
def test_with_title():
    assert 3 + 3 == 6


@allure.title("参数化的标题: adding {param1} with {param2}")
@pytest.mark.parametrize('param1,param2,expected', [
    (2, 2, 4),
    (1, 2, 5)
])
def test_with_parameterized_title(param1, param2, expected):
    assert param1 + param2 == expected


@allure.link('https://www.youtube.com/watch?v=4YYzUTYZRMU')
def test_with_link():
    pass


@allure.issue('http://www.jira.com/id=19688')
@allure.testcase('http://www.testlink.com/id=19688')
def test_demo():
    print('this is test')
    with allure.step("这是第一步骤"):
        allure.attach("填上我们要的附加信息")


if __name__ == '__main__':
    pytest.main()
