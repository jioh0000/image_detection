from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time 
import urllib.request
from webdriver_manager.chrome import ChromeDriverManager as CM
import requests
import os

keywords = input("검색할 키워드를 입력하세요: ") # 아이유, 에스파윈터, 최예나
count = int(input("몇 개의 데이터가 필요하신가요?: ")) #몇 개 데이터가 필요하신가요?
# Selenium config
options = webdriver.ChromeOptions()

mobile_emulation = {
    "userAgent": 'Mozilla/5.0 (Linux; Android 4.0.3; HTC One X Build/IML74K) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/99.0.4844.51 Mobile Safari/535.19'
}
# options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(executable_path=CM().install(), options=options)
driver.set_window_position(0, 0)
driver.set_window_size(1200, 800)
driver.get('https://www.google.co.kr/imghp?hl=ko')

headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}
# cateCd = 카테고리 번호 005 = 시럽


elem = driver.find_element_by_name("q")
elem.send_keys(keywords)
elem.send_keys(Keys.RETURN)
images = driver.find_element_by_css_selector(".rg_i.Q4LuWd")


x = 0
# for image in images:
images.click()
time.sleep(2)
imgUrl = driver.find_element_by_xpath('/html/body/div[3]/c-wiz/div[3]/div[1]/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[27]/a[1]/div[1]/img').get_attribute("src")
print(imgUrl)
img_data = requests.get(imgUrl).content

with open(keywords+'.jpg', 'wb') as handler:
    handler.write(img_data)

# urllib.request.urlretrieve(imgUrl, "image-class-1/" + keywords + str(x) +".jpg") # image-class-1/최예나24.jpg
x += 1

driver.close()