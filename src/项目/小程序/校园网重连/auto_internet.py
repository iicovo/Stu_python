from selenium import webdriver
import time
import requests
from datetime import date
import random


class Login:
    def __init__(self):
        self.url = "http://172.168.168.198/eportal/index.jsp?wlanuserip=a9e78885c09ee2af8dab1057e891eacf&wlanacname=2ed9344ad269849b22b87e886f5f8de4&ssid=&nasip=23233415e0bb04d29539e3d0205de4db&snmpagentip=&mac=10010b29463f182eb2099729ecd6888d&t=wireless-v2&url=8d1882559b7926e28a248aa52dbb06ed8c05336e64c82d3fd29d18112bc470a3&apmac=&nasid=2ed9344ad269849b22b87e886f5f8de4&vid=164ed2bfbb1fb450&port=edf1490adda5a443&nasportid=bf2334948d573506cc1d9ee53f3aec36bc77a8c269be147166fcb9de7ac385aaf15cae4983df8a8e"
        self.username = '1983812' + str(random.randint(1000, 9999))
        self.pwd = '123456'

    def con_web(self):  # 检查网络状态
        try:
            status = requests.get("https://www.baidu.com/?tn=06074089_11_dg")
            if status.status_code == 200:
                return True
            else:
                return False
        except Exception:
            print("error")
            return False

    def net(self):  # 自动登录连接
        option = webdriver.ChromeOptions()
        option.add_argument('--headless')  # 浏览器不提供可视化页面
        option.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        option.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
        driver = webdriver.Chrome(options=option)
        driver.get(self.url)

        driver.execute_script("document.querySelector('#username').style.display='block';")  # 显示隐藏元素
        input_user = driver.find_element_by_id('username')
        input_user.send_keys(self.username)

        driver.execute_script("document.querySelector('#pwd').style.display='block';")
        input_pwd = driver.find_element_by_id('pwd')
        input_pwd.send_keys(self.pwd)

        driver.find_element_by_xpath("//*[@id='loginLink_div']").click()  # inputTag.submit() //*[@id='loginLink_div']

        print("登录成功!")
        driver.quit()


run = Login()
n = 1
while True:
    if run.con_web():
        time.sleep(300)
    else:
        run.net()
        now = date.today()
        print('重连第' + str(n) + '次' + " " + str(now))
        n = n + 1
