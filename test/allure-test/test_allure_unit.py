import pytest
import allure

@allure.step("测试步骤一：字符串相加{0}，{1}")
def str_add(str1, str2):
    print("这两个字符串如下：", str1, str2)
    if not isinstance(str1, str):
        return "%s 不是字符串" % str1
    if not isinstance(str2, str):
        return "%s 不是字符串" % str2
    return str1 + str2


@allure.description("测试两个字符串相加的各种情况")
@allure.severity("critical")               # 优先级，包含blocker, critical, normal, minor, trivial 几个不同的等级
# @allure.feature("测试功能_demo1")           # 功能块，feature功能分块时比story大,即同时存在feature和story时,feature为父节点
# @allure.story("测试模块_demo2")             # 功能块，具有相同feature或story的用例将规整到相同模块下,执行时可用于筛选
# @allure.issue("BUG号：123")                 # BUG编号，关联标识已有的问题，可为一个url链接地址
@allure.issue("http://www.jira.com/id=19688")   # BUG编号，关联标识已有的问题，可为一个url链接地址
# @allure.testcase("用例名：测试字符串相等")      # 用例标识，关联标识用例，可为一个url链接地址
@allure.testcase("http://www.testlink.com/id=19688")
@pytest.mark.parametrize("para_one,para_two",
                         [("hello,", "world!"),
                          ('888', '999'),
                          ("我是最幸福的", "人"),
                          ("333", "ad智慧")], ids=[
        "letter-abc",
        "decimal-123",
        "unicode",
        "mix-abc123"
    ])
def test_stradd(para_one, para_two):
    # 获取参数-vars()返回属性和属性值的字典
    paras = vars()
    allure.attach("用例参数", "{0}".format(paras))
    with allure.step("测试步骤二：调用str_add的方法"):
        res = str_add(para_one, para_two)
    allure.attach("返回的结果", "{0}".format(res))
    with allure.step("测试步骤三：结果检验{0}=={1}".format(res, para_one+para_two)):
        assert res == para_one + para_two

