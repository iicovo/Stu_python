# encoding : utf-8
import time
from selenium import webdriver
import requests


class Clock_in:

    def __init__(self):
        self.user = "iicovo@qq.com"
        self.pwd = "kkk00000"

    def get_url(self):
        urls = ["https://xxjc.pro", "https://xxjc.vip", "https://xxjc.host"]
        # for i in range(len(urls)):
        #     req = requests.get(urls[i])
        #     if req.status_code == 200:
        Clock_in.Qian_dao(self, urls[1])
        # break

    def Qian_dao(self, url):
        # options = webdriver.ChromeOptions()
        # options.add_argument('--headless')
        driver = webdriver.Chrome()
        driver.get(url)
        try:
            # 登录
            driver.find_element_by_xpath('//*[@id="header"]/nav/ul/li[2]/a').click()
            inputname = driver.find_element_by_xpath('//*[@id="email"]')
            inputname.send_keys(self.user)
            inputpwd = driver.find_element_by_xpath('//*[@id="passwd"]')
            inputpwd.send_keys(self.pwd)
            driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[6]/div/div/label/span[3]').click()
            driver.find_element_by_xpath('//*[@id="login"]').click()
            time.sleep(2)

            # 打卡签到
            try:
                driver.find_element_by_xpath('//*[@id="checkin"]').click()
                print('签到成功!')
            except:
                pass
        except:
            driver.find_element_by_xpath('//*[@id="header"]/nav/ul/li[2]/a').click()
            time.sleep(2)
            try:
                driver.find_element_by_xpath('//*[@id="checkin"]').click()
                print('签到成功!')
            except:
                print('今天已签到!')

        driver.quit()

    def main(self):
        Clock_in.get_url(self)


if __name__ == '__main__':
    run = Clock_in()
    run.main()
