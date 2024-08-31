import json

from src.file_worker import JSONSaver

from src.utils import FilterSortVacancies
from config import *
# from dotenv import load_dotenv
#
# # load_dotenv(".env")
# #
# # API_KEY_RATES = os.getenv("API_KEY_RATES")
# # API_KEY_STOCKS = os.getenv("API_KEY_STOCKS")
#
# # Получаем абсолютный путь до текущей директории
# current_dir = os.path.dirname(os.path.abspath(__file__))
#
# # # Создаем путь до файла логов относительно текущей директории
# # rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
# # abs_log_file_path = os.path.abspath(rel_log_file_path)
#
# # Создаем путь до файла user_settings.json относительно текущей директории.
# # В файл храниться словарь с требуемыми валютами и акциями
# rel_json_path = os.path.join(current_dir, "../data/vacancies.json")
# abs_json_path = os.path.abspath(rel_json_path)
#
# # # Создаем путь до файла operations.xlsx относительно текущей директории
# # rel_xlsx_path = os.path.join(current_dir, "../data/operations.xlsx")
# # abs_xlsx_path = os.path.abspath(rel_xlsx_path)
# #
# # # Добавляем логгер, который записывает логи в файл.
# # logger = logging.getLogger("utils")
# # logger.setLevel(logging.INFO)
# # file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
# # file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
# # file_handler.setFormatter(file_formatter)
# # logger.addHandler(file_handler)
#
#
#
#
# # #x = input("Введите ключевые слова для фильтрации вакансий: ").split("-")
# # lst = [1, 2, 3, 4, 5, 6, 7, 8, 1]
# # lst_new = []
# # let = int(input("Введите число"))
# # # for i in lst:
# # #     if i >= int(x[0]) and i <= int(x[-1]):
# # #         lst_new.append(i)
# #
# # def hlp(word, inlist):
# #     lst_new = []
# #     try:
# #         if word.isdigit():
# #             for i in inlist:
# #                 if i == word:
# #                     lst_new.append(i)
# #
# #                 else:
# #                     pass
# #             return lst_new
# #     except:
# #         print('g')
# #     finally:
# #         return inlist
# # print(hlp(let, lst))
# #
# #
# # os.path.join(DATA_DIR, "vacancies.json")
#
# with open(JSON_DIR, "r", encoding="UTF-8") as f:
#     vacs = json.load(f)


def read_file(file):
    """
    Функция для чтения файла. Проверяет, есть ли файл. И, если есть, сохраняет список объектов
    """
    if os.path.exists(file):
        with open(file, "r", encoding="UTF-8") as f:
            vacs = json.load(f)
        vacs_list = [i for i in vacs]
    return vacs_list

print(read_file(JSON_DIR))
#for i in vacs:


    #if i['description']:
    #print(i)
        #print(i.get("description"))
# with open(DATA_DIR/"vacancies.json", "r", encoding="UTF-8") as f:
#     vacs = json.load(f)

#print(vacs)
# json_saver = JSONSaver()
#
# def user_interaction():
#
#     search_query = input('Введите поисковый запрос: ')
#
#
#     # Обращение к пользователю. Сбор информации
#     top_n = int(input('Введите количество вакансий для вывода в топ N: '))
#     filter_word = input('Введите ключевое слово для фильтрации вакансий по описанию: ')
#     filter_city = input('Введите город для фильтрации вакансий по местоположению: ')
#     filter_salary = input('Введите диапазон интересующих зарплат. Например: 10000-15000: ').split('-')
#
#     print('')
#
#     read_vacs_from_json = json_saver.read_file()
#     # Создание экземпляра класса фильтрации и сортировки вакансий
#     filtered_obj = FilterSortVacancies(filter_word, filter_city, filter_salary, top_n)
#
#     filtered_by_description = filtered_obj.filter_by_description(read_vacs_from_json)
#     print(f"Отфильтровано {len(filtered_by_description)} вакансий по описанию")
#     filtered_by_city = filtered_obj.filter_by_city(filtered_by_description)
#     print(f"Отфильтровано {len(filtered_by_city)} вакансий по местоположению")
#     filtered_by_salary = filtered_obj.filter_by_salary(filtered_by_city)
#     print(f'Отфильтровано {len(filtered_by_salary)} вакансий по зарплате\n')
#
#     sorted_by_salary = filtered_obj.sort_vacancies_by_salary(filtered_by_salary)
#
#     top_vacancies = filtered_obj.get_top_vacancies(sorted_by_salary)
#
#     print(f'Топ {top_n} вакансий:\n{top_vacancies}\n')
#
#     user_input = input('Очистить файл с вакансиями? (да / нет): ').lower()
#     if user_input == 'да':
#         json_saver.del_vacancy()
#
#
# if __name__ == '__main__':
#     user_interaction()