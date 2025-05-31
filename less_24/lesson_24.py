"""
Тема: Функции. Анонимные функции. Map, Filter, Sorted. Урок: 24
- синтаксис анонимных функций
"""

from marvel import small_dict, full_dict, simple_set
from pprint import pprint

# def foo(x):
#     x = x + 10
#     return x

# # print(foo(500))
# # print()


# foo1 = lambda x: x + 10
# # print(foo1(100))

simple_list = list(simple_set)
simple_list = sorted(simple_list)

# new_simple_list = []

# for film in simple_list:
#     new_simple_list.append(film)

# # list comprehension
# new_simple_list = [film for film in simple_list] # Эта запись означает: "Для каждого элемента film из списка simple_list добавь этот элемент в новый список"

# result_list_3 = []

# for film in simple_list:
#     if 'чел' in film.lower():
#         result_list_3.append(film)

# result_list_3 = [film for film in simple_list if 'чел' in film.lower()]

# # filter функция высшего порядка
# # Высший порядок - это функция, которая принимает другую функцию в качестве аргумента
# # Принимает 2 аргумента: функцию и итерируемый объект
# # Возвращает булево значение

# # banana = print
# # banana("Hello")
# # banana()

def search_string(string):
    return 'чел' in string.lower()

def my_filter(func, iterable):
    result = []

    for item in iterable:
        item_calc = func(item)
        result.append(item_calc)
    return result

result_list_1 = my_filter(search_string, simple_list)

result_list_2 = list(filter(search_string, simple_list))
result_list_3 = list(filter(lambda film: 'чел' in film.lower(), simple_list))

# # pprint(result_list_1)
# # print()
# # pprint(result_list_2)
# # print()
# # pprint(result_list_3)
# # print()


# ###### MAP ######
# # Обход с помощью map, comprehension коллекций

def filter1(func, movie_list):
    result = []

    for movie in movie_list:
        if func(movie):
            result.append(movie.upper())
    return result

result_list_7 = filter1(search_string, simple_list)
pprint(result_list_7)
print()

result_list_8 = list(map(lambda film: film.upper(), filter(lambda film: 'чел' in film.lower(), simple_list)))
pprint(result_list_8)

# result_list_4 = []

# for film in simple_list:
#     result_list_4.append(film.upper().replace(" ", ""))

# result_list_4 = [film.upper() for film in simple_list]

# result_list_5 = list(map(lambda film: film.upper().replace(" ", ""), filter(lambda film: 'чел' in film.lower(), simple_list)))

# result_list_6 = list(map(lambda film: str.upper(film.replace(" ", "")), filter(lambda film: 'чел' in film.lower(), simple_list)))


# # pprint(result_list_4)
# # print()
# # pprint(result_list_5)
# # print()
# # pprint(result_list_6)
# # print()


def filter_or_none(movie_list):
    result = []
    name = "Чел"
    for movie in movie_list:
        if name.lower() in movie.lower():
            if " " in movie:
                result.append(movie.upper().replace(" ", "_"))
            else:
                result.append(movie.lower())
    return result

result_list_9 = filter_or_none(simple_list)
pprint(result_list_9, width=40)
print()

result_list_10 = list(map(lambda film: film.upper() if " " in film else film.lower(), filter(lambda film: 'чел' in film.lower(), simple_list)))
pprint(result_list_10)
print()


# result_list_11 = []
# for film in simple_list:
#     if " " in film:
#         result_list_11.append(film.lower().replace(" ", "_"))
#     else:
#         result_list_11.append(film)
# pprint(result_list_11)
# print()

# result_list_12 = [film.lower().replace(" ", "_") if " " in film else film for film in simple_list]
# pprint(result_list_12)
# print()

# result_list_13 = list(map(lambda film: film.lower().replace(" ", "_") if " " in film else film, simple_list))
# pprint(result_list_13)
# print()

##### Комбо ######

result_list_14 = []

for film in simple_list:
    if len(film) > 15:
        if " " in film:
            result_list_14.append(film.lower().replace(" ", "_"))
        else:
            result_list_14.append(film.upper())

pprint(result_list_14)
print()

result_list_15 = [film.lower().replace(" ", "_") if " " in film else film.upper() for film in simple_list if len(film) > 15]

pprint(result_list_15)
print()

result_list_16 = list(map(lambda film: film.lower().replace(" ", "_") if " " in film else film.upper(), filter(lambda film: len(film) > 15, simple_list)))

pprint(result_list_16)
print()

result_list_17 = list(map(lambda film: str.lower(film.replace(" ", "_")) if " " in film else str.upper(film), filter(lambda film: len(film) > 15, simple_list)))

pprint(result_list_17)
print()

###### sorted ######

full_list = []

for index, film in full_dict.items():
    full_list.append({"id": index, **film})

full_list = sorted(full_list, key=lambda film: film["id"])

pprint(full_list, sort_dicts=False)
print()

full_list = [{"id": index, **film} for index, film in full_dict.items()]

pprint(full_list, sort_dicts=False, width=240)
print()

full_list_sorted = sorted(full_list, key=lambda film: film["id"])
