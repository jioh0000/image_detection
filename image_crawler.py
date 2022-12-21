from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Failed to create the directory")

def crawling_img(name):
    driver = webdriver.Chrome('/Users/kis/Documents/GitHub/image_detection/chromedriver')
    driver.get("https://www.google.co.kr/imghp?hl=ko&authuser=0&ogbl")
    elem = driver.find_element_by_name('q') # 서치바 , SearchBar
    elem.send_keys(name) # 최예나 
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight") # 브라우저의 높이를 찾음
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # 페이지 로딩 기다리기
        time.sleep(SCROLL_PAUSE_TIME)
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height: 
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break   
        last_height = new_height
        
    imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    dir = '/Users/kis/Documents/GitHub/image_detection/' + name
    
    createDirectory(dir)

    count = 1
    for img in imgs:
        try:
            img.click()
            time.sleep(2)
            imgUrl = driver.find_element_by_xpath(
                '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img').get_attribute("src")
            # print(imgUrl)
            path = dir + '/'
            #imgurl to real image
            # /Users/Danny/Desktop/GitHub/coding-academy-jioh/image-detection/최예나/최예나26.jpg
            urllib.request.urlretrieve(imgUrl, path+name+str(count) + ".jpg") # 최예나25.jpg, 
            count += 1

            if count >= 70:
                break
        except:
            pass
    driver.close()

classes = ['유리병', '페트병']
for each in classes:
    crawling_img(each)