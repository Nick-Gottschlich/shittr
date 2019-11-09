import webview
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

browser = webdriver.Firefox()

def doit(window):
    browser.get('http://whatkeyamipressing.com')

    time.sleep(3)

    actions = ActionChains(browser)
    actions.send_keys(Keys.CONTROL).perform()


if __name__ == '__main__':
    window = webview.create_window('tester')
    webview.start(doit, window)


