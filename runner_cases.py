import  unittest
from BeautifulReport import BeautifulReport

from config.config import report_path, case_path

# 加载批量的测试用例
suite = unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test*.py')

# runner = unittest.TextTestRunner()
# runner.run(suite)

result = BeautifulReport(suite)
result.report(description='系统登录的测试报告',filename='SIT脚本测试报告',report_dir=report_path)