# # Задача 1: Анализ чисел
# # Напишите функцию `analyze_numbers(numbers)`, которая принимает список чисел
# # и возвращает кортеж из трех значений: сумма всех чисел, среднее значение и количество четных чисел.
# #
# # numbers = [1, 2, 3, 4, 5, 6]
# # Вывод функции: (21, 3.5, 3)

def analyze_numbers(numbers):
    all_sum = sum (numbers)
    average = all_sum / len(numbers)
    even_num = sum((num % 2 == 0) for num in numbers)
    return all_sum, average, even_num

numbers = [1, 2, 3, 4, 5, 6]
result = analyze_numbers(numbers)
print(result)


# # Задача 2: Работа со строками
# # Напишите функцию `analyze_strings(strings)`, которая принимает список строк
# # и возвращает кортеж из трех значений: самая длинная строка, самая короткая строка и количество строк, содержащих букву "a"..
# #
# # strings = ["apple", "banana", "cherry", "date"]
# # Вывод функции: ('banana', 'date', 3)

def analyze_strings(strings):
    count_a = 0
    for word in strings:
        if 'a' in word:
            count_a += 1
    # count_a = sum(1 for word in strings if 'a' in word)
    return count_a


print(analyze_strings(["apple", "banana", "cherry", "date"]))


# # Задача 3: Обработка словаря сотрудников
# # Напишите функцию `analyze_salaries(employees)`, которая принимает словарь сотрудников и
# # возвращает кортеж из трех значений: средняя зарплата, максимальная зарплата и имя сотрудника с максимальной зарплатой.
# #
# # employees = {"Alice": 5000, "Bob": 7000, "Charlie": 6000}
# # Вывод функции: (6000.0, 7000, 'Bob')

def analyze_salaries(employees):
    salaries = list(employees.values())
    avg_salary = sum(salaries) / len(salaries)
    max_salary = max(salaries)

    for name in employees:
        if employees[name] == max_salary:
            max_salary_employee = name

    # max_salary_employee = max(employees, key=employees.get)

    return avg_salary, max_salary, max_salary_employee


print(analyze_salaries({"Alice": 5000, "Bob": 7000, "Charlie": 6000}))

# Задача 4: Фильтрация списка
# Напишите функцию `filter_numbers(numbers)`, которая принимает список чисел и
# возвращает кортеж из двух списков: четные числа и нечетные числа.
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Вывод функции: ([2, 4, 6, 8, 10], [1, 3, 5, 7, 9])

def filter_numbers(numbers):
    even_num = [num for num in numbers if num % 2 == 0]  # Четные числа
    odd_num = [num for num in numbers if num % 2 != 0]
    return even_num, odd_num

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_numbers(numbers)
print(result)

# Задача 1: Генерация словаря
# Напишите функцию `create_dict(keys, values)`, которая принимает два списка: ключи и значения,
# и возвращает словарь, где ключи из первого списка, а значения из второго.
#
# keys = ["name", "age", "city"]
# values = ["Alice", 30, "New York"]
# Вывод функции: {'name': 'Alice', 'age': 30, 'city': 'New York'}

def create_dict(keys, values):
    return dict(zip(keys, values))

keys = ['name', 'age', 'city']
values = ["Alice", 30, "New York"]
result = create_dict(keys, values)
print(result)



# Задача 2: Подсчет символов в строке
# Напишите функцию `count_characters(string)`, которая принимает строку и
# возвращает словарь, где ключи - это символы строки, а значения - количество их вхождений.
#
# string = "hello world"
# Вывод функции: {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
def count_characters(string):
    character_count = {}
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
        
    return character_count

string = 'hello world'
result = count_characters(string)
print(result)

# Задача 3: Обработка произвольного числа аргументов
# Напишите функцию `sum_positive_negative(*args)`, которая принимает произвольное число числовых аргументов
# и возвращает кортеж из двух значений: сумма положительных чисел и сумма отрицательных чисел.
#
# sum_positive_negative(1, -2, 3, -4, 5)
# Вывод функции: (9, -6)

def sum_positive_negative(*args):
    positive_sum = sum(x for x in args if x > 0)
    negative_sum = sum(x for x in args if x < 0)
    return (positive_sum, negative_sum)

result = sum_positive_negative(1, -2, 3, -4, 5)
print(result)

# Задача 4: Генерация строки из именованных аргументов
# Напишите функцию `generate_string(**kwargs)`, которая принимает произвольное число именованных аргументов и возвращает строку, состоящую из ключей и значений в формате "key=value".
#
# generate_string(name="Alice", age=30, city="New York")
# Вывод функции: name=Alice, age=30, city=New York

def generate_string(**kwargs):
    return ', '.join(map(lambda item: f'{item[0]}={item[1]}', kwargs.items()))

result = generate_string(name='Alice', age=30, city='New York')
print(result)
