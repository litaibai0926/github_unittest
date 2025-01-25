import unittest
from time import sleep, time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from objectpage.login_page import LoginPage
from config.config import url, driver_path,system_version
from data.data import ReadWrite
from log.log import logger

'''
以上的类应该是导进来，注释以后运行脚本不能正常加载测试用例

不注释的话，则可以正常加载测试用例

'''

class LoginCases(unittest.TestCase):
    # 夹具的使用fixture
    @classmethod
    def setUpClass(cls):
        e = Service(executable_path=driver_path)
        cls.driver = webdriver.Chrome(service=e)
        cls.driver.maximize_window()
        cls.driver.get(url)
        cls.loginpage=LoginPage(cls.driver)
        print("打开浏览器")
    @classmethod
    def tearDownClass(cls):
        print("关闭浏览器")
        cls.driver.quit()

    def test_01(self):
        '''

         验证：用户输入正确账号密码可以正常登录
        '''
        print("验证第一条")
        user_list=ReadWrite().excelread('users') # 读取'users'这张sheet页的数据
        username= user_list[0][0] # excel表的第0列的第0位就是用户名
        password=user_list[0][1] # excel表的第0列的第1位就是密码
        self.loginpage.input_username(username)
        self.loginpage.input_password(password)
        self.loginpage.click_login()
        sleep(1)
        # try:
        self.assertIn('我的地盘 - 禅道', self.driver.title,'登录页面不存在')  # 断言判断登录成功后的页面，self.driver.title是不是包含“我的地盘——禅道”，有则说明登录成功
        self.loginpage.click_logout()
        logger.info('有效的用户名和密码登录成功')
        # except:
        #     print("登录页面不显示")



    # @unittest.skip('跳过不执行')
    @unittest.skipIf(system_version=='1.1',reason="只有在版本号为1.2的时候才执行")
    def test_02(self):
        '''
         验证：用户输入密码为空时，登录失败
        '''

        self.loginpage.input_username('admin')
        self.loginpage.click_login()
        sleep(2)
        alert_login = self.driver.switch_to.alert
        alert_login.accept()
        print("验证第二条")

