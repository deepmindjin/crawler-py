import logging
import requests
import json
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)


class Crawler:
    login = {
        'email': 'deepmindjin@gmail.com',
        'password': 'plmokn12!'
    }
    slack_bot_api_url = 'https://hooks.slack.com/services/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'

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls
        self.session = requests.session()
        login_page = 'https://kream.co.kr/login'
        res = self.session.post(login_page, data=self.login)

    def download_url(self, url):
        user_agent = {'User-agent': 'Mozilla/5.0'}
        return self.session.get(url, headers=user_agent, allow_redirects=False).text

    def crawl(self, url):
        html = self.download_url(url)
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select('title')[0]
        sale_info = soup.select('tr')
        print(title)
        print(sale_info)
        # json_object = json.dumps(sale_info)
        # for deal in json_object:
        #     print(deal)
        #     requests.post(self.slack_bot_api_url, json=json_object)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')


if __name__ == '__main__':
    Crawler(urls=['https://kream.co.kr/products/44651']).run()
