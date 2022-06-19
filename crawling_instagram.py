import time
import sys
from selenium import webdriver
from bs4 import BeautifulSoup

username = sys.argv[1]
browser = webdriver.Chrome('./chromedriver')
browser.get('https://www.instagram.com/'+username)
browser.execute_script("document.querySelectorAll('.-nal3')[1].click();")

time.sleep(2)

browser.find_element_by_name('username').send_keys(sys.argv[1])
browser.find_element_by_name('password').send_keys(sys.argv[2])

browser.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button').submit()

time.sleep(5)

browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()

time.sleep(5)

if len(sys.argv) > 3:
    username = sys.argv[3]

print('계정: ' + username)
browser.get('https://www.instagram.com/'+username)

time.sleep(2)

browser.execute_script("document.querySelectorAll('.-nal3')[1].click();")

time.sleep(1)

oldHeight = -1
newHeight = -2
while oldHeight != newHeight:
    oldHeight = newHeight
    newHeight = browser.execute_script("return document.querySelectorAll('.jSC57')[0].scrollHeight")
    browser.execute_script("document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('.jSC57')[0].scrollHeight)")
    time.sleep(0.5)

soup = BeautifulSoup(browser.page_source, 'html.parser')
followers = soup.findAll('a',['FPmhX','notranslate','_0imsa'])
followers_text = []
for follower in followers:
    followers_text.append(follower.get_text())

print("팔로워 수: " + str(len(followers_text)))

browser.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()

time.sleep(0.5)

browser.execute_script("document.querySelectorAll('.-nal3')[2].click();")

time.sleep(1)

oldHeight = -1
newHeight = -2
while oldHeight != newHeight:
    oldHeight = newHeight
    newHeight = browser.execute_script("return document.querySelectorAll('.jSC57')[0].scrollHeight")
    browser.execute_script("document.querySelectorAll('.isgrP')[0].scrollTo(0,document.querySelectorAll('.jSC57')[0].scrollHeight)")
    time.sleep(0.5)

soup = BeautifulSoup(browser.page_source, 'html.parser')
followings = soup.findAll('a',['FPmhX','notranslate','_0imsa'])
followings_text = []
for following in followings:
    followings_text.append(following.get_text())

print("팔로잉 수: " + str(len(followings_text)))

result = []
for following in followings_text:
    cnt = 0
    for follower in followers_text:
        if following == follower:
            cnt += 1
            break
    if cnt == 0:
        result.append(following)

print('맞팔하지 않은 사람 목록: '+str(result))
