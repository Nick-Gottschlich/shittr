from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import RPi.GPIO as GPIO
from pydub import AudioSegment
from pydub.playback import play

flush_noise = AudioSegment.from_wav("toilet.wav")

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

browser = webdriver.Firefox()


def reset():
    browser.delete_all_cookies()
    time.sleep(5)
    browser.get('localhost:3000')


def run_flush():
    play(flush_noise)
    time.sleep(3)


def flush_facebook_2():
    input_state = GPIO.input(18)

    if input_state == False:
        # really confirm button once the user presses confirm eat a dick zucc
        fb_really_confirm_button = browser.find_element_by_xpath(
            '/html/body/div[7]/div[2]/div/div/form/div[3]/button')
        fb_really_confirm_button.click()

        run_flush()
        # time.sleep(2)

        reset()
        return
    else:
        time.sleep(0.3)
        flush_facebook_2()


def flush_facebook():
    input_state = GPIO.input(18)

    if input_state == False:
        # confirmation button once the user enters password
        fb_confirm_button = browser.find_element_by_xpath(
            '/html/body/div[7]/div[2]/div/div/form/div[3]/button')
        fb_confirm_button.click()
        
        run_flush()
        # time.sleep(2)

        flush_facebook_2()
        return
    else:
        time.sleep(0.3)
        flush_facebook()


def flush_instagram():
    input_state = GPIO.input(18)

    if input_state == False:
        browser.switch_to.alert.accept()

        run_flush()
        # time.sleep(2)

        reset()
        return
    else:
        time.sleep(0.3)
        flush_instagram()


def flush_twitter():
    input_state = GPIO.input(18)

    if input_state == False:
        twitter_confirm_delete_button = browser.find_element_by_xpath(
            '/html/body/div/div/div/div/main/div/div/div/section[2]/div[2]/div[5]/div/div/span/span'
        )
        twitter_confirm_delete_button.click()

        run_flush()
        # time.sleep(2)

        reset()
        return
    else:
        time.sleep(0.3)
        flush_twitter()


def flush_reddit_2():
    input_state = GPIO.input(18)

    if input_state == False:
        reddit_really_confirm_delete_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div/button[2]')
        reddit_really_confirm_delete_button.click()

        run_flush()
        # time.sleep(2)

        reset()
        return
    else:
        time.sleep(0.3)
        flush_reddit_2()


def flush_reddit():
    input_state = GPIO.input(18)

    if input_state == False:
        reddit_confirm_delete_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div[4]/button[2]')
        reddit_confirm_delete_button.click()

        run_flush()
        # time.sleep(2)

        flush_reddit_2()
        return
    else:
        time.sleep(0.3)
        flush_reddit()


def run_this_shit():
    browser.get('http://localhost:3000')
    browser.maximize_window()
    browser.fullscreen_window()

    zoomed_bool = False

    while True:
        input_state = GPIO.input(18)
        url = browser.current_url

        print(url)

        if (url == 'https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Fhelp%2Fdelete_account' and not zoomed_bool):
            time.sleep(3)
            print('1')
            # this doesn't seem to be working, pick up from here
            # browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, Keys.SUBTRACT)
            # print(browser.find_element_by_tag_name("body"))
            # browser.find_element_by_tag_name("html").send_keys(Keys.LEFT_CONTROL, Keys.SUBTRACT)
            # browser.execute_script("document.body.style.transform = 'scale(0.8)'")
            # browser.execute_script("document.body.style.zoom='zoom 80%'")
            # maybe key down next?
            # actions = ActionChains(browser)
            # browser.find_element_by_tag_name("html").send_keys(Keys.LEFT_CONTROL, Keys.SUBTRACT)
            # ActionChains(browser).send_keys(Keys.CONTROL).send_keys(Keys.SUBTRACT).perform()
            # ActionChains(browser).send_keys(Keys.CONTROL).send_keys(Keys.SUBTRACT).perform()
            # ActionChains(browser).key_down(Keys.CONTROL).send_keys(Keys.SUBTRACT).perform()
            # actions.send_keys(Keys.SUBTRACT).perform()
            # actions.send_keys(Keys.CONTROL, Keys.SUBTRACT).perform()
            # actions.send_keys(Keys.SUBTRACT)
            # actions.perform()
            
            # browser.find_element_by_tag_name('html').key_down(Keys.CONTROL).send_keys(Keys.SUBTRACT)
            print('2')
            zoomed_bool = True

        if input_state == False:
            url = browser.current_url

            if url == 'https://www.facebook.com/help/delete_account':
                # initial delete button
                fb_delete_button = browser.find_element_by_xpath(
                    '/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div[1]/a[2]')
                fb_delete_button.click()
                # run_flush()
                time.sleep(2)

                flush_facebook()

            if url == 'https://www.instagram.com/accounts/remove/request/permanent/':
                ig_delete_button = browser.find_element_by_xpath(
                    '/html/body/div/div[1]/div/div[2]/section/form/div[8]/p[4]/input')
                ig_delete_button.click()
                # run_flush()
                time.sleep(2)

                flush_instagram()

            if url == 'https://twitter.com/settings/deactivate':
                twitter_delete_button = browser.find_element_by_xpath(
                    '/html/body/div/div/div/div/main/div/div/div/section[2]/div[2]/div/div[11]/div/div/span')
                twitter_delete_button.click()
                # run_flush()
                time.sleep(2)

                flush_twitter()

            if url == 'https://www.reddit.com/settings':
                reddit_delete_button = browser.find_element_by_xpath(
                    '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[7]/button')
                reddit_delete_button.click()
                # run_flush()
                time.sleep(2)

                flush_reddit()

        time.sleep(0.3)


if __name__ == '__main__':
    run_this_shit()
