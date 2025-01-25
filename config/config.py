

# 储存基础配置信息
# 例如浏览器驱动位置
# 浏览器网址
#
# 驱动器的本地绝对路径为：r'C:\Users\86177\AppData\Local\Python\Python38\chromedriver.exe'



import os
root_path=os.path.dirname(os.path.dirname(__file__))  # dirname()当前文件夹的上一级
print(root_path)
# 要是更换网址了，从这里修改就行，其他地方不用动
url= 'http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html'
driver_path=r'C:\Users\86177\PycharmProjects\web自动化\PyaotuTest\1unittest_day2\driver\chromedriver.exe' # 驱动器本地绝对路径
driver_path=root_path+r'\driver\chromedriver.exe'
case_path = root_path+r'/test_demo'
report_path = root_path+r'/report'
log_file = root_path+r'/log/log.txt'
file_path =root_path+r'/data/test.xlsx'
system_version='1.2'




