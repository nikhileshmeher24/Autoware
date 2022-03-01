from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
my_username=""
my_password=""
usernames=['','','']
messages="Hey, this is an automated 2nd message"
browser=webdriver.Chrome('chromedriver')
browser.get('https://www.instagram.com/')
sleep_time=3

def login(username,password):
    browser.get('https://www.instagram.com/')
    time.sleep(sleep_time)
    input_uname=browser.find_element_by_name('username')
    input_pass=browser.find_element_by_name('password')
    input_uname.send_keys(username)
    time.sleep(2)
    input_pass.send_keys(password)
    time.sleep(2)
    input_pass.submit()
    time.sleep(sleep_time)

def send_mess(users,messages):
    browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a').click()
    time.sleep(sleep_time)
    browser.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
    time.sleep(sleep_time)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button').click()
    time.sleep(sleep_time)

    for user in users:
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(user)
        time.sleep(sleep_time)
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]').find_element_by_tag_name('button').click()
        time.sleep(sleep_time)
        browser.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div').click()
        time.sleep(sleep_time)
        text_area=browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        text_area.send_keys(messages)
        time.sleep(sleep_time)
        text_area.send_keys(Keys.ENTER)
        print(f'Message successfully sent to {user}')
        time.sleep(sleep_time)
        browser.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
        time.sleep(sleep_time)



login(my_username,my_password)
time.sleep(sleep_time)
send_mess(usernames,messages)
browser.quit()

    
