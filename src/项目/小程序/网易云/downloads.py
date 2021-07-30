# encoding:utf-8
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import requests
import time

""" 批量下载歌单歌曲 """

user = 'iicovo@163.com'  # ##这里添加网易账号
pwd = 'Kong6666*'  # ##这里添加网易密码


def gain_list(gain_url):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(gain_url)
    cookies = dict(name="WM_TID", value='5SvKbGNNTp5AVFAVRFZ7XS%2B%2BXkeB1vdC')
    driver.add_cookie(cookies)

    driver.get(gain_url)

    # try:
    #     driver.find_element_by_css_selector('.link.s-fc3').click()  # 点击登录
    #     time.sleep(1)
    #     driver.find_element_by_css_selector('.u-btn2.other').click()  # 选择其他方式
    #
    #     driver.find_element_by_id('j-official-terms').click()  # 点击同意
    #
    #     driver.find_element_by_css_selector('.u-mlg2.u-mlg2-wy').click()  # 网易账户登录
    #     time.sleep(1)
    #
    #     username = driver.find_element_by_id('e')
    #     username.send_keys(user)
    #     time.sleep(1)
    #
    #     kwd = driver.find_element_by_id('epw')
    #     kwd.send_keys(pwd)
    #     time.sleep(1)
    #
    #     driver.find_element_by_css_selector('.js-primary.u-btn2.u-btn2-2').click()
    #     time.sleep(15)

    # except Exception:
    #     print('登录失败!')

    driver.switch_to.frame('contentFrame')
    source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(source, 'lxml')
    contents = soup.find_all('span', attrs={'class': 'txt'})  # 获取歌单列表

    id_list = []  # 创建id列表
    name_list = []  # 创建歌曲名列表

    for content in contents:
        x = str(content)
        counts = re.search('href="/song\?id=(.+?)"', x).group(1)  # 获取歌曲id
        title = re.search('title="(.*?)"', x).group(1)  # 获取歌曲名
        id_list.append(counts)
        name_list.append(title)
    print("获取歌名id成功！！！")
    for i in range(len(id_list)):
        download(id_list[i], name_list[i])  # 逐个进行下载
        time.sleep(1)


def download(count, name):
    """ 下载歌曲并保存 """

    url_download = "http://music.163.com/song/media/outer/url?id=" + str(count)
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
    }
    res = requests.get(url_download, headers=headers)
    filename = name + '.mp3'  # 保存文件名为歌曲名
    try:
        with open(filename, "wb") as f:
            f.write(res.content)
    except Exception:
        """ 文件名不支持格式异常处理 """
        filename = "未命名歌曲" + count + '.mp3'
        print('*' * 10 + '歌曲名异常' + '*' * 10)
        with open(filename, "wb") as f:
            f.write(res.content)
    print(name + ": 下载成功!")


if __name__ == '__main__':
    while True:
        url = input("请输入要下载的歌单id地址:")  # 登录网页版查看网页链接后的id数字
        gain_list(url)
        print('下载完成!')
        c = input("是否退出 (y退出):")
        if c == 'y' or c == 'Y':
            break
