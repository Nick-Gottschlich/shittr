from selenium import webdriver
from pyvirtualdisplay import Display
 
Display(visible=1, size=(800, 600)).start()

profile = webdriver.FirefoxProfile()
profile.native_events_enabled = False
browser = webdriver.Firefox()
browser.set_window_position(0, 0)
browser.set_window_size(800, 480)
browser.get('https://google.com')
print(browser.page_source.encode('utf-8'))

while True:
    fakeButtonPress = input()
    if fakeButtonPress == 'go':
        print(browser.current_url)
        url = browser.current_url
