from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

from conf import settings
from services.google_sheet_service import GoogleSheet
from services.gpt import OpenAIClient
from services.parse_service import ParseService
from selenium.webdriver.chrome.service import Service


if __name__ == '__main__':
    options = Options()
    service = ParseService()
    gpt_client = OpenAIClient()
    google_sheet = GoogleSheet(settings.GOOGLE_SHEET_URL, settings.SHEET_START_COL)

    options.add_experimental_option("debuggerAddress", "localhost:9222")
    service_selenium = Service('chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=service_selenium)
    action = ActionChains(driver)

    while True:
        url = input('Введите linkedin url или нажмите Ctrl+C для выхода из программы:\n')

        name = service.get_name_from_url(url)

        print("Собираю данные...")
        links = service.crawl_run(url, driver, action)

        print("Данные получены и записываются в Google Sheet!")
        if settings.COMPANY in url:
            google_sheet.append_to_column(settings.COMPANY_SHEET_NAME, row_data=links)
        else:
            google_sheet.append_to_column(settings.CONTACT_SHEET_NAME, row_data=links)
        print("Запись в Google Sheet прошла успешно!")

        print("Начинаю работу с Chat GPT")
        gpt_answer = gpt_client.generate_answer(links)
        print("Ответ от Chat GPT получен, начинаю запись в Google Sheet...")

        google_sheet.append_to_column_gpt_data(settings.GPT_SHEET_NAME, gpt_answer, name)
        print("Запись в Google Sheet прошла успешно!")
