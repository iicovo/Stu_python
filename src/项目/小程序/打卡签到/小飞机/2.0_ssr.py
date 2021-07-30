# encoding:utf-8

"""
主域名：https://xxjc.vip
备用域名1：https://xxjc.work
备用域名2：https://xxjc.one
备用域名3：https://xxjc.nl
备用域名4：https://xxjc.fun
"""

import time
import requests
from selenium import webdriver

user = 'iicovo@qq.com'
pwd = 'kkk00000'


def check_url():
    """选择可用网址"""
    url_list = ['https://xxjc.vip',
                'https://xxjc.work',
                'https://xxjc.one',
                'https://xxjc.nl',
                'https://xxjc.fun'
                ]
    # for i in range(len(url_list)):
    #     cu = requests.get(url_list[i])
    #     if cu.status_code == 200:
    #         return url_list[i]
    return url_list[0]


def open_web():
    """打开浏览器并配置浏览器"""
    # 配置浏览器
    option_chrome = webdriver.ChromeOptions()
    # 隐藏自动化测试横幅
    option_chrome.add_experimental_option('useAutomationExtension', False)
    option_chrome.add_experimental_option('excludeSwitches', ['enable-automation'])

    # 不加载图片, 提升速度
    option_chrome.add_argument('blink-settings=imagesEnabled=false')

    # 隐藏浏览器
    # option_chrome.add_argument('--headless')  # 浏览器不提供可视化页面
    option_chrome.add_argument('--disable-gpu')
    # 打开浏览器
    driver = webdriver.Chrome(options=option_chrome)

    driver.maximize_window()
    return driver


def get_web(driver):
    """打开网页"""
    driver.get(check_url())
    time.sleep(5)


def login(driver):
    """用户登录"""
    try:
        driver.find_element_by_xpath('//*[@id="header"]/nav/ul/li[2]/a').click()  # 点击登录加载登录页面
        time.sleep(2)
        driver.execute_script('window.stop ? window.stop():document.execCommand("Stop");')
        in_user = driver.find_element_by_xpath('//*[@id="email"]')
        in_user.send_keys(user)
        in_pwd = driver.find_element_by_xpath('//*[@id="passwd"]')
        in_pwd.send_keys(pwd)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="login"]').click()
        print("登录成功！")
        time.sleep(5)

    except Exception:
        path = 'E:\\Desktop\\登录失败.txt'
        f1 = open(path, 'w', encoding='utf-8')
        f1.close()


def sign_in(driver):
    """打卡签到"""
    try:
        driver.find_element_by_xpath('//*[@id="checkin"]').click()
        path = 'E:\\Desktop\\签到成功.txt'
        f1 = open(path, 'w', encoding='utf-8')
        f1.close()
    except Exception:
        print("今天已签到！！！")
    finally:
        driver.quit()


def main():
    driver = open_web()  # 打开浏览器
    get_web(driver)  # 打开网页
    login(driver)  # 登录账户
    sign_in(driver)  # 签到


if __name__ == '__main__':
    main()
