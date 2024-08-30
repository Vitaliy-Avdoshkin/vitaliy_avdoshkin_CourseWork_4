import json
import os
from config import *

# #x = input("Введите ключевые слова для фильтрации вакансий: ").split("-")
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 1]
# lst_new = []
# let = int(input("Введите число"))
# # for i in lst:
# #     if i >= int(x[0]) and i <= int(x[-1]):
# #         lst_new.append(i)
#
# def hlp(word, inlist):
#     lst_new = []
#     try:
#         if word.isdigit():
#             for i in inlist:
#                 if i == word:
#                     lst_new.append(i)
#
#                 else:
#                     pass
#             return lst_new
#     except:
#         print('g')
#     finally:
#         return inlist
# print(hlp(let, lst))
#
#
os.path.join(DATA_DIR, "vacancies.json")

with open("vacancies.json", "r", encoding="UTF-8") as f:
    vacs = json.load(f)
