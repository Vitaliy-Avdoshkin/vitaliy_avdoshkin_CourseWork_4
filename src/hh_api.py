from abc import ABC, abstractmethod
from typing import List

import requests


class BaseAPI(ABC):
    """
    Абстрактный класс для работы с API сервиса с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass

    # @abstractmethod
    # def get_vacancies(self):
    #     pass


class HeadHunterAPI(BaseAPI):
    """
    Класс для работы с платформой hh.ru

    """

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []


    def get_vacancies(self, keyword: str):
        """
        Функция для загрузки вакансий по заданному слову
        """
        self.params["text"] = keyword
        while self.params.get("page") != 20:
            try:
                response = requests.get(
                    self.__url, headers=self.__headers, params=self.params
                )
            except Exception as e:
                print(f"Произошла ошибка {e}")
            else:
                vacancies = response.json()["items"]
                self.vacancies.extend(vacancies)
                self.params["page"] += 1
        return self.vacancies

    # def get_vacancies(self) -> List:
    #     """
    #     Возвращает список вакансий
    #     """
    #     return self.vacancies


if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    #hh_api.load_vacancies("Python")
    hh_vacancies = hh_api.get_vacancies("Python")
    print(hh_vacancies)
