from airtest.core.android.adb import ADB
from airtest.core.api import *
from utils.log_base import log_base_run
from airtest.report.report import simple_report
import logging
adb = ADB()

log_run = ""


def common_utils_info():
    """
    获取手机信息
    """
    if not adb.devices():
        raise IndexError('ADB device not found')
    return adb.devices()


def common_utils_serial():
    """
    提取信息中的序列号
    """
    serial = common_utils_info()
    if not serial:
        raise IndexError('ADB serial not found')
    list=[i[0] for i in serial]
    return list


def common_utils_connect(args, path):
    """
    链接手机并设定日志位置
    """
    auto_setup(__file__, logdir=path, devices=['Android://127.0.0.1:5037/{serial}'.format(serial=args)])
    return


def common_utils_report(path):
    """
    生成报告
    """
    simple_report(__file__, logpath=f'{path}', logfile=f'{log_run}/log.txt', output=f'{log_run}/log.html')
    return


def common_utils_start_stop():
    """
    打开app
    """
    stop_app('com.road7.phoenix')
    start_app('com.road7.phoenix')
    return


def common_utils_logging():
    """
    使日志只显示报错
    :return:
    """
    logger = logging.getLogger('airtest')
    logger.setLevel(logging.ERROR)



