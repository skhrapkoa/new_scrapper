import random
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from seleniumbase import Driver

from conf import settings


class LinkedinParser:
    @staticmethod
    def start_parse(url: str, driver: Driver, action: ActionChains):
        driver.uc_open(url)
        sleep(random.uniform(3.0, 5.0))

        action.send_keys(Keys.END)
        action.perform()
        sleep(5)
        action.send_keys(Keys.END)
        action.perform()
        sleep(5)
        page_html = driver.get_page_source()

        return page_html

    @staticmethod
    def start_page() -> tuple[Driver, ActionChains]:
        driver = Driver(undetected=True, headed=True)
        action = ActionChains(driver)

        driver.get("https://www.linkedin.com/login?fromSignIn=true&amp;trk=guest_homepage-basic_nav-header-signin")

        print("Начинаю авторизацию...")

        driver.wait_for_element("#username")
        sleep(random.uniform(2.5, 4.8))
        driver.type("#username", settings.LINKEDIN_LOGIN)

        driver.wait_for_element("#password")
        sleep(random.uniform(3.1, 4.6))
        driver.type("#password", settings.LINKEDIN_PASSWORD + "\n")
        sleep(random.uniform(0.6, 1.2))

        print("Авторизация окончена!")

        return driver, action
