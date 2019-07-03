import pytest
from selenium import webdriver
import time
import allure


class TestBaidu(object):

    @allure.feature('打开百度')
    @pytest.fixture(scope='function', autouse=True)
    def start(self, driver):
        with allure.step('step one:打开浏览器输入百度网址'):
            driver.get('http://www.baidu.com')
            time.sleep(1)

    @allure.feature('百度搜索功能')
    @allure.story('搜索验证-字母')
    @pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
    def test_soso(self, driver, test_data1):
        with allure.step('step two：在搜索栏输入{0},并点击百度一下'.format(test_data1)):
            driver.find_element_by_id('kw').send_keys(test_data1)
            driver.find_element_by_id('su').click()
            time.sleep(3)
            print(driver.title)
            assert test_data1 in driver.title
        with allure.step('截图保存到项目中'):
            driver.save_screenshot("./result/b.png")
            allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)

    @allure.feature('百度new功能')
    @allure.story('搜索打开新闻页')
    def test_news(self, driver):
        with allure.step('step three：点击新闻，验证是否跳转'):
            driver.find_element_by_link_text('新闻').click()
            print(driver.title)
            assert '新闻' in driver.title

        with allure.step('截图验证'):
            driver.save_screenshot("./result/c.png")
            allure.attach.file("./result/c.png", attachment_type=allure.attachment_type.PNG)

