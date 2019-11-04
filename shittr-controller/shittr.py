import webview
from selenium import webdriver
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


def run_this_shit(window):
    browser.get('http://localhost:3000')
    browser.maximize_window()
    browser.fullscreen_window()

    while True:
        input_state = GPIO.input(18)

        if input_state == False:
            print(browser.current_url)
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
    window = webview.create_window('shittr', fullscreen=True)
    webview.start(run_this_shit, window)
