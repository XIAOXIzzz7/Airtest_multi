import os


def utils_log_base(log_path, number):
    while True:
        log = f'{log_path}{number}'
        decide = os.path.exists(log)
        if not decide:
            os.makedirs(log)
            print(f'创建{log}成功')
            return log
        else:
            number += 1
            continue


def log_base_run():
    log_path = 'D:/log/log_'
    number = 1
    return utils_log_base(log_path, number)


if __name__ == '__main__':
    log_base_run()






