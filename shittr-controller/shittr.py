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
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)

browser = webdriver.Firefox()


def reset():
    browser.delete_all_cookies()
    browser.get('http://localhost:3000')
    time.sleep(5)


def run_flush():
    play(flush_noise)
    time.sleep(3)


def flush_facebook_2():
    input_state = GPIO.input(18)
    reset_input_state = GPIO.input(25)

    if not reset_input_state:
        reset()

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
        time.sleep(0.05)
        flush_facebook_2()


def flush_facebook():
    input_state = GPIO.input(18)
    reset_input_state = GPIO.input(25)

    if not reset_input_state:
        reset()

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
        time.sleep(0.05)
        flush_facebook()


def flush_instagram():
    input_state = GPIO.input(18)
    reset_input_state = GPIO.input(25)

    if not reset_input_state:
        reset()

    if input_state == False:
        browser.switch_to.alert.accept()

        run_flush()
        # time.sleep(2)

        reset()
        return
    else:
        time.sleep(0.05)
        flush_instagram()


def flush_twitter():
    input_state = GPIO.input(18)
    reset_input_state = GPIO.input(25)

    if not reset_input_state:
        reset()

    if input_state == False:
        twitter_confirm_delete_button = browser.find_element_by_xpath(
            '/html/body/div/div/div/div[2]/main/div/div/div/div/div[5]/div'
        )
        twitter_confirm_delete_button.click()

        run_flush()
        # time.sleep(2)

        reset()
        return
    else:
        time.sleep(0.05)
        flush_twitter()


def flush_reddit_2():
    input_state = GPIO.input(18)
    reset_input_state = GPIO.input(25)

    if not reset_input_state:
        reset()

    if input_state == False:
        reddit_really_confirm_delete_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div/button[2]')
        reddit_really_confirm_delete_button.click()

        run_flush()
        # time.sleep(2)

        reset()
        return
    else:
        time.sleep(0.05)
        flush_reddit_2()


def flush_reddit():
    input_state = GPIO.input(18)
    reset_input_state = GPIO.input(25)

    if not reset_input_state:
        reset()

    if input_state == False:
        reddit_confirm_delete_button = browser.find_element_by_xpath(
            '/html/body/div[1]/div/div/div/div[4]/div/div/div/div/div[4]/button[2]')
        reddit_confirm_delete_button.click()

        run_flush()
        # time.sleep(2)

        flush_reddit_2()
        return
    else:
        time.sleep(0.05)
        flush_reddit()


def run_this_shit():
    print('anything??')
    browser.get('http://localhost:3000')
    print('2')
    browser.maximize_window()
    print('3')
    # browser.fullscreen_window() 
    # ActionChains(browser).send_keys(Keys.F11).perform()
    html = browser.find_element_by_tag_name("html")
    html.send_keys(Keys.F11)
    print('4')

    def zoom_out(scale):
        browser.execute_script(f'document.body.style.MozTransform = "scale({scale})";')
        browser.execute_script('document.body.style.MozTransformOrigin = "0 0";')

    def scroll_to_bottom():
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    print ('bruh what')

    while True:
        url = browser.current_url

        input_state = GPIO.input(18)
        print(input_state)
        # false means button has been pressed
        reset_input_state = GPIO.input(25)

        try:
            print (reset_input_state)
            # if not reset_input_state:
                # reset()

            if url == 'https://www.facebook.com/login.php?next=https%3A%2F%2Fwww.facebook.com%2Fhelp%2Fdelete_account':
                zoom_out(0.8)

            elif url == 'https://www.facebook.com/help/delete_account':
                zoom_out(0.8)

                if not input_state:
                    # initial delete button
                    fb_delete_button = browser.find_element_by_xpath(
                        '/html/body/div[1]/div[3]/div[1]/div/div/div[3]/div/div[1]/a[2]')
                    fb_delete_button.click()
                    # run_flush()
                    time.sleep(2)

                    flush_facebook()

            elif url == 'https://www.instagram.com/accounts/remove/request/permanent/':
                zoom_out(0.8)
                scroll_to_bottom()

                if not input_state:
                    ig_delete_button = browser.find_element_by_xpath(
                        '/html/body/div/div[1]/div/div[2]/section/form/div[8]/p[4]/input')
                    ig_delete_button.click()
                    # run_flush()
                    time.sleep(2)

                    flush_instagram()

            elif url == 'https://twitter.com/settings/deactivate':
                zoom_out(0.65)

                if not input_state:
                    twitter_delete_button = browser.find_element_by_xpath(
                        '/html/body/div/div/div/div[2]/main/div/div/div/div/div/div[11]/div/div/span')
                    twitter_delete_button.click()
                    # run_flush()
                    time.sleep(2)

                    flush_twitter()

            elif url == 'https://www.reddit.com/settings':
                scroll_to_bottom()

                if not input_state:
                    reddit_delete_button = browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div[1]/div[7]/button')
                    reddit_delete_button.click()
                    # run_flush()
                    time.sleep(2)

                    flush_reddit()
        except Exception as error:
            print('ERROR:', error)
            pass

        time.sleep(0.05)


if __name__ == '__main__':
    run_this_shit()
