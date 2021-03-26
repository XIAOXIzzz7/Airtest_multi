import time

from multiprocessing import Pool
from utils.common_utils import common_utils_serial, common_utils_report, common_utils_start_stop, common_utils_connect, common_utils_logging
from airtest.core.api import *
from script.yinhun_1 import scripe_yinhun_1


def multi_process(arg):
    """
    多进程设置连接手机-打开app-运行脚本
    """
    _time = "D:/log/log_{}".format(int(time.time()))
    try:
        common_utils_logging()
        common_utils_connect(arg, _time)
        common_utils_start_stop()
        sleep(10)
        scripe_yinhun_1()
    finally:
        common_utils_report(_time)


def multi_main():
    """
    进程池 通过获得序列号，判断序列号数量创建进程
    """
    po = Pool(3)
    list = common_utils_serial()
    for i in list:
        po.apply_async(multi_process, (i,))
    po.close()
    po.join()


if __name__ == '__main__':
    multi_main()
