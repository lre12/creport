import json
from typing import Optional

import requests
from bs4 import BeautifulSoup


class GetInvestmentMoneyService:
    def __init__(self):
        self.__base_url = f'https://thevc.kr/'
        self.__convert_name_url = f"https://api.thevc.kr/information/organizations/search?keyword="

    def get_money(self, company_name: str) -> Optional[str]:
        request_headers = {
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'),
        }
        company_name = self.__convert_name(company_name=company_name)
        if not company_name:
            return None
        score_response = requests.get(self.__base_url + company_name, headers=request_headers)
        if score_response.status_code != 200:
            return None

        html = score_response.text
        soup = BeautifulSoup(html, 'html.parser')
        score = soup.select_one(
            '#layout-wrap > div.holy-grail.vc-responsive-m.main-el > div.holy-grail-middle > div > section:nth-child(1) > div > div.body > div > div > div.profile-funding-info > div:nth-child(2) > p.vc-typo-size-xxl > b'
        )

        score_text = score.get_text()

        return score_text

    def __convert_name(self, company_name: str) -> Optional[str]:
        # TODO 정리 필요

        request_headers = {
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\
        Safari/537.36'),
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'origin': 'https://thevc.kr',
            'referer': 'https://thevc.kr',
            "sec-ch-ua": '" Not;A Brand";v = "99", "Google Chrome";v = "91", "Chromium";v = "91"',
            'sec-ch-ua-mobil': '?0',
            'sec-fetch-des': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site'
        }
        name_response = requests.get(self.__convert_name_url + company_name + "&limit=4", headers=request_headers)

        if name_response.status_code != 200:
            return None

        if name_response.text == '[]':
            return None

        name_dict = json.loads(name_response.text)[0]
        return name_dict["profilePage"]
