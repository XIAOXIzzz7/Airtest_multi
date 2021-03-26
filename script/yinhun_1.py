from airtest.core.api import *
import random
# from utils.tools import utils_tools_poco


def scripe_yinhun_1():
    """
    游戏脚本存放，不要删除代码
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    """
    from poco.drivers.unity3d import UnityPoco
    poco = UnityPoco()
    try:
        touch(Template(r"photo/tpl1614249615214.png", record_pos=(0.188, 0.161), resolution=(2280, 1080)),
              duration=0.5, times=2)

        sleep(3)
        poco("btn_close").click()

        poco(texture="icon_user").click()

        touch(Template(r"photo/tpl1614238713913.png", record_pos=(-0.075, 0.028), resolution=(2280, 1080)))
        touch(Template(r"photo/tpl1614564709607.png", record_pos=(-0.211, -0.081), resolution=(2280, 1080)))

        id = random.sample('123213ssd2dasd1ad313adad213', 5)
        id = ''.join(id)
        text(f"{id}")
        sleep(0.5)
        touch(Template(r"photo/tpl1614305522592.png", record_pos=(-0.231, -0.025), resolution=(2280, 1080)))

        pwd = random.sample('12675hgreta3213daddadaa13213', 5)
        pwd = ''.join(pwd)
        text(f"{pwd}")
        sleep(0.5)
        touch(Template(r"photo/tpl1614238812357.png", record_pos=(-0.03, 0.043), resolution=(2280, 1080)))
        age = random.sample('189879d32adad131dada3213', 5)
        age = ''.join(age)
        text(f"{age}")
        sleep(0.5)
        touch(Template(r"photo/tpl1614241892043.png", record_pos=(0.192, 0.106), resolution=(2280, 1080)))
        sleep(2)
        touch(Template(r"photo/tpl1614242108276.png", record_pos=(0.188, 0.162), resolution=(2280, 1080)))
        sleep(2)
        poco("Txt_CurrServer").click()

        poco("Txt_CurrServer").click()
        poco("Content").child("ServerItemModel(Clone)")[0].child("Txt_Name").click()
        poco(text='开始游戏').click()
        touch(Template(r"photo/tpl1614306103574.png", record_pos=(0.191, 0.161), resolution=(2280, 1080)),
              duration=0.5, times=3)
        poco('Placeholder').click()
        for i in range(8):
            keyevent("67")
        user_name = random.sample('zxcvbnmlkjhgfdswwertuiop123412474', 8)
        user_name = ''.join(user_name)
        text(f"{user_name}")
        poco(text='开始游戏').click()
        poco(text='开始游戏').click()
        sleep(8)
        touch(Template(r"photo/tpl1614305854630.png", record_pos=(0.186, 0.16), resolution=(2280, 1080)),
              duration=0.5, times=5)

        poco(text="呀，真是熟悉的开场啊。").wait_for_appearance()
        poco("img_exit").click()
        # 序章战斗
        poco(text="等等，阿银，是不是不太对劲？这是什么？怎么一上来就是战斗？").wait_for_appearance()
        poco('btn_pass').click()
        poco('img_cost').click()
        poco('scr_card').child('BasicListAdapterItem2(Clone)').offspring('outline_qualitybg').swipe([0.008, -0.3454])

        poco("img_role").wait_for_appearance()
        poco("img_role").click()

        poco('scr_card').child('BasicListAdapterItem2(Clone)').offspring('outline_qualitybg').swipe([-0.0322, -0.184])
        poco('StarNode3').wait_for_appearance()
        poco('StarNode3').click()
        print(f'脚本{os.getpid()}运行完毕')
    except:
        print(f'脚本{os.getpid()}运行失败')


if __name__ == '__main__':
    scripe_yinhun_1()