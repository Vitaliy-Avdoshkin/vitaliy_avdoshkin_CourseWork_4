import re
from typing import List


class FilterSortVacancies:
    """
    Класс для фильтрации, сортировки и вывода топ вакансий
    """

    # def __init__(self, filter_word, filter_city, filter_salary, top_n):
    #     self.filter_word = filter_word
    #     self.filter_city = filter_city
    #     self.filter_salary = filter_salary
    #     self.top_n = top_n


    def __init__(self, filter_word, filter_city, top_n):
        self.filter_word = filter_word
        self.filter_city = filter_city
        self.top_n = top_n

    def filter_by_description(self, vacancies_list: List) -> List:
        """
        Функция для фильтрации вакансий по заданному слову в описании
        """
        filtered_vacancies_list = []
        for vac in vacancies_list:
            if re.findall(self.filter_word, str(vac['description']), re.IGNORECASE):
                filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    def filter_by_city(self, vacancies_list: List) -> List:
        """
        Функция для фильтрации вакансий по заданному городу
        """
        filtered_vacancies_list = []
        for vac in vacancies_list:
            if re.findall(self.filter_city, str(vac['city']), re.IGNORECASE):
                filtered_vacancies_list.append(vac)
        return filtered_vacancies_list

    # def filter_by_salary(self, vacancies_list: list) -> list:
    #     """
    #     Функция для фильтрации вакансий по заданной зарплате
    #     (оставляет вакансии с зарплатой выше либо равной указанной пользователем)
    #     """
    #     filtered_vacancies_list = []
    #     try:
    #         for vac in vacancies_list:
    #             if int(vac['salary_from']) <= int(
    #                 self.filter_salary[0]
    #             ) and int(vac['salary_to']) <= int(self.filter_salary[-1]):
    #                 filtered_vacancies_list.append(vac)
    #     except:
    #         pass
    #     return filtered_vacancies_list

    @staticmethod
    def sort_vacancies_by_salary(vacancies_list: List) -> List:
        """
        Функция для сортировки вакансий по зарплате (по убыванию)
        """
        vacancies_list.sort(key=lambda x: x.salary_from, reverse=True)
        return vacancies_list

    def get_top_vacancies(self, vacancies_list: List) -> str:
        """
        Функция для получения топ N вакансий (N указывает пользователь)
        """
        top_vacancies = ""
        if self.top_n < len(vacancies_list):
            for i in range(self.top_n):
                top_vacancies += f"Вакансия {i + 1}:\n{str(vacancies_list[i])}\n\n"
        else:
            for i in range(len(vacancies_list)):
                top_vacancies += f"Вакансия {i + 1}:\n{str(vacancies_list[i])}\n\n"
        return top_vacancies
