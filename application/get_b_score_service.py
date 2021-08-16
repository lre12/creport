from typing import Optional

import requests
from bs4 import BeautifulSoup


class GetBScoreService:
    def __init__(self):
        self.__base_url = f'https://www.teamblind.com/kr/company/'

    def get_score(self, company_name: str) -> Optional[str]:
        request_headers = {
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'),
        }
        score_response = requests.get(self.__base_url + company_name + "/reviews", headers=request_headers)
        if score_response.status_code != 200:
            return None

        html = score_response.text
        soup = BeautifulSoup(html, 'html.parser')
        score = soup.select_one(
            '#wrap > section > div > div > div.cpctw > div > div > div > div > section:nth-child(1) > div > '
            'div.rating_stars > div.rating_no > strong '
        )

        score_text = score.get_text()
        dot_index = score_text.index('.')
        score = score_text[dot_index - 1:dot_index + 2]

        return score
