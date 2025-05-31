"""
Тема: Функции. Области видимости. Замыкания. Декортаор. Урок 25
- Области видимости:
    Buit-in - встроенная
    Global - глобальная
    Local - локальная
    Nonlocal - не локальная
"""
# Buit-in
# print()
# len()
# sum()
# bool()

# Global
# a = 5

# Local
# def func():
#     a = 5
#     print(a)

# def func2():
#     b = 5
#     print(b)

# Local - область видимости внутри функций \ методов

a = 5
def func():
    a = 10
    print(a)

def func2():
    a = 15
    print(a)

def func3():
    print(a)

def func4(a: int) -> None:
    """
    Печатает число
    :param a: число для печати
    """
    print(a)

def func6():
    global a, b
    a = 20
    b = 22
    print(f'{a=} внутри ')

# print = "печенька"
# print("!") # 'str' object is not callable

# Проверим a
print(f'{a=}')

# Вызов 2 функций
func()
func2()

# Проверим a
print(f'{a=}')

# Вызов функции 6
func6()

# Проверим a
print(f'{a=}')

# Проверим b
print(f'{b=}')

def func7():
    a = 7
    print(f'функция 7 {a=}')
    
    def built7():
        nonlocal a
        a = 77
        print(f'встроенная функция 7 {a=}')
    
    built7()
    print(f'функция 7 после вызова built7 {a=}')

# Вызов функции 7
func7()

# Проверим a
print(f'{a=}')

def func8(a):
    def inner8():
        print(a)
    return inner8

func8(5)

banan = print
banan("Привет")

foo = func8(10)
foo()