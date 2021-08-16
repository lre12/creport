import json
import requests
from bs4 import BeautifulSoup


class GetJScoreService:
    def __init__(self):
        self.__company_num_url = 'https://www.jobplanet.co.kr/autocomplete/autocomplete/suggest.json?term='
        self.__base_url = f'https://www.jobplanet.co.kr/companies/'

    def get_score(self, company_name: str) -> str:
        company_id = self.__get_company_num(company_name=company_name)
        score_response = requests.get(self.__base_url + str(company_id) + "/reviews/")
        if score_response.status_code != 200:
            raise Exception

        html = score_response.text
        soup = BeautifulSoup(html, 'html.parser')
        score = soup.select_one(
            'body > div.body_wrap > div.cmp_hd > div.new_top_bnr > div > div.top_bnr_wrap > div > div > '
            'div.company_info_sec > div.company_info_box > div.about_company > div.score_area.type_total_year > div > '
            'span'
        )

        score_text = score.get_text()
        dot_index = score_text.index('.')
        score = score_text[dot_index - 1:dot_index + 2]

        return score

    def __get_company_num(self, company_name: str) -> int:
        company_num_response = requests.get(self.__company_num_url + company_name)
        if company_num_response.status_code != 200:
            raise Exception

        company_id = json.loads(company_num_response.text)["companies"][0]["id"]

        return company_id
