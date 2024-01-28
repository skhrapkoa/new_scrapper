import re

from bs4 import BeautifulSoup

from services.crawler import LinkedinParser


class ParseService:
    def crawl_run(self, url: str, driver, action) -> dict[str, list]:
        linkedin_parser = LinkedinParser()
        full_url = self.concat_url(url)
        html = linkedin_parser.start_parse(full_url, driver, action)
        data = self.parse_html(html)
        return data

    def parse_html(self, html: str):
        soup = BeautifulSoup(html, 'html.parser')
        urn_data = soup.find_all("div", {"data-urn": True})
        text_element = soup.find_all("div", {"class": "feed-shared-update-v2__description-wrapper"})
        text_data = [elem.find("span", {"dir": "ltr"}) for elem in text_element]

        texts = [elem.text for elem in text_data]

        try:
            urns = [urn["data-urn"] for urn in urn_data if re.match(r"urn:li:activity:\d+", urn["data-urn"])]
        except Exception as error:
            print(
                f"Can't parse data: {urn_data}. Error: {error}"
            )
            return None

        links = self.create_links(urns)
        result = {"2": links[:20], "3": texts[:20]}
        return result

    @staticmethod
    def create_links(urns: list[str]) -> list[str]:
        return ["https://www.linkedin.com/feed/update/" + urn for urn in urns]

    @staticmethod
    def concat_url(url: str) -> str:
        if "company" in url:
            return f"{url}posts/?feedView=all"
        return f"{url}recent-activity/all/"
