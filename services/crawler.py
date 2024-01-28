import random
from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class LinkedinParser:
    @staticmethod
    def start_parse(url: str, driver: WebDriver, action: ActionChains):
        driver.get(url)
        sleep(random.uniform(3.0, 5.0))

        action.send_keys(Keys.END)
        action.perform()
        sleep(5)
        action.send_keys(Keys.END)
        action.perform()
        sleep(5)
        page_html = driver.page_source

        return page_html
