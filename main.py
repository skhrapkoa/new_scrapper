from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from conf import settings
from services.crawler import LinkedinParser
from services.google_sheet_service import GoogleSheet
from services.parse_service import ParseService
from selenium.webdriver.chrome.service import Service


if __name__ == '__main__':
    print(1)
    options = Options()
    print(2)
    service = ParseService()
    print(3)
    google_sheet = GoogleSheet(settings.GOOGLE_SHEET_URL, settings.SHEET_START_COL)
    print(4)

    options.add_experimental_option("debuggerAddress", "localhost:9222")
    print(5)
    service_selenium = Service('chromedriver.exe')
    print(6)
    driver = webdriver.Chrome(options=options, service=service_selenium)
    print(7)
    action = ActionChains(driver)
    print(8)

    while True:
        url = input('Введите linkedin url или нажмите Ctrl+C для выхода из программы:\n')
        print("Собираю данные...")
        links = service.crawl_run(url, driver, action)
        print("Данные получены и записываются в Google Sheet!")
        if settings.COMPANY in url:
            google_sheet.append_data(settings.COMPANY_SHEET_NAME, 'append_to_column', row_data=links)
        else:
            google_sheet.append_data(settings.CONTACT_SHEET_NAME, 'append_to_column', row_data=links)
        print("Запись в Google Sheet прошла успешно!")
