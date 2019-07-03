import pytest
import allure


@allure.feature("购物车功能")
class TestShopping(object):
    @allure.story("加入购物车")
    def test_add_shopping(self):
         # 先登陆
        login('linda','88888')
        with allure.step("步骤1：浏览商品"):
            allure.attach("商品1", "华为手机")
            allure.attach("商品2", "火车票")
        with allure.step("点击商品"):
            allure.attach('<head></head><body>点击商品，添加到购物车中</body>', '这是一个网页', allure.attachment_type.HTML)
        with allure.step("验证添加的结果，确定添加商品正确"):
            allure.attach("期望结果", "添加购物车成功")
            allure.attach("实际结果", "添加购物车失败")
            assert 'success'=='failure'

    @allure.story("修改购物车中商品")
    def test_edit_shopping(self):
        pass

    @pytest.mark.skipif(reason="不想删除")
    @allure.story("删除购物车商品")
    def test_delete_shopping(self):
        pass


def login(user,pwd):
    print(user,pwd)


if __name__ == '__main__':
    pytest.main(["--allure-features='购物车功能'"])
