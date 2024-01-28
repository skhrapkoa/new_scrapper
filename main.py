from conf import settings
from services.crawler import LinkedinParser
from services.google_sheet_service import GoogleSheet
from services.parse_service import ParseService


if __name__ == '__main__':
    service = ParseService()
    parser = LinkedinParser()
    google_sheet = GoogleSheet(settings.GOOGLE_SHEET_URL, settings.SHEET_START_COL)

    driver, action = parser.start_page()

    while True:
        url = input('Введите linkedin url или нажмите Ctrl+C для выхода из программы:\n')
        links = service.crawl_run(url, driver, action)
        print("Данные получены и записываются в Google Sheet!")
        if settings.COMPANY in url:
            google_sheet.append_data(settings.COMPANY_SHEET_NAME, 'append_to_column', row_data=links)
        else:
            google_sheet.append_data(settings.CONTACT_SHEET_NAME, 'append_to_column', row_data=links)
        print("Запись в Google Sheet прошла успешно!")
