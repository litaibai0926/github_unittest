

# 日志文件的formate
'''
%(created)f: 日期
%(name)s: Logger的名字
%(levelno)s: 数字形式的日志级别 DEBUG 10, INFO 20,WARING 30,ERROR 40,CRITICAL 50
%(levelname)s: 文本形式的日志级别
%（filename）s: 调用日志输出函数的模块的完整路径名称
%（module）s: 调用日志输出的模块mingz
%(asctime)s:字符串形式的当前时间，'2025-01-22'
%(message)s:用户输入的信息
'''
import logging
from config.config import log_file
# 创建日志器
logger=logging.getLogger()
# 定义日志器的级别
logger.setLevel(logging.INFO)
# 定义处理器的格式，就是展示信息的样式
format=logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
logFile=log_file
# 创建处理器
fh=logging.FileHandler(log_file,mode='a',encoding='utf-8')
#设置处理器的级别
fh.setLevel(logging.INFO)
# 设置处理器的格式
fh.setFormatter(format)
# 添加到日志器
logger.addHandler(fh)
