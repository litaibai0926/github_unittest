from selenium.webdriver.common.by import By


# 定义login登录页面元素
class LoginPage:
    def __init__(self,driver): # 这个driver 就是给这些元素加了一个驱动
        self.account_elem=By.ID,'account'  # 定义账号输入框元素
        self.password_elem=By.NAME,'password'# 定义密码元素
        self.login_button_elem=By.ID,'submit' # 登录按钮
        self.user_logout_elem=By.CLASS_NAME,'user-name' # 页面右上角 adminn
        self.logout_elem=By.LINK_TEXT,'退出'# 退出按钮元素
        self.driver=driver # 驱动元素


    def input_username(self,username):  # 给账号输入框定义了一个输入方法，传入的值为“username”

        self.driver.find_element(*self.account_elem).clear()  # 输入内容前，先清空内容，保证输入的准确性
        self.driver.find_element(*self.account_elem).send_keys(username)

    def input_password(self, password):  # 给输入密码框定义了一个输入方法，传入的值为“password”

        self.driver.find_element(*self.password_elem).clear() # 输入内容前，先清空内容，保证输入的准确性
        self.driver.find_element(*self.password_elem).send_keys(password)


    def click_login(self): # 登录按钮，只需要点击，不需要传参数
        self.driver.find_element(*self.login_button_elem).click()

    def click_logout(self):  # 点击admin 按钮 和 退出按钮，不需要传入参数
        self.driver.find_element(*self.user_logout_elem).click()
        self.driver.find_element(*self.logout_elem).click()

