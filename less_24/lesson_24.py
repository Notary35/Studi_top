"""
Тема: Функции. Анонимные функции. Map, Filter, Sorted. Урок: 24
- синтаксис анонимных функций
"""
from marvel import small_dict, full_dict, simple_set
def foo(x):
    x = x + 10
    return x

print(foo(500))
print()


foo1 = lambda x: x + 10
print(foo1(100))

simple_list = list(simple_set)
simple_list = sorted(simple_list)

new_simple_list = []

for film in simple_list:
    new_simple_list.append(film)

# list comprehension
new_simple_list = [film for film in simple_list] # Эта запись означает: "Для каждого элемента film из списка simple_list добавь этот элемент в новый список"

result_list_3 = []

for film in simple_list:
    if 'чел' in film.lower():
        result_list_3.append(film)

result_list_3 = [film for film in simple_list if 'чел' in film.lower()]

# filter функция высшего порядка
# Высший порядок - это функция, которая принимает другую функцию в качестве аргумента
# Принимает 2 аргумента: функцию и итерируемый объект
# Возвращает булево значение

banana = print
banana("Hello")
banana()

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

print(result_list_1)
print()
print(result_list_2)
print()
print(result_list_3)