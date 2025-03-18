"""
19.01.2025
Тема: ООП Ч5. Наследование. Множественное. Иерархическое. MRO. Урок: 20
- Взаимозависимость классов
- Вызов метода наследника через родителя
"""

# Цепочка наследования A - B - C
# Альтернативный вариант
# Много минусов. 

class A:
    def method_a(self) -> None:
        print("Метод класса A")
        print()

class B:
    def method_a(self) -> None:
        print("Метод A в классе B")
        print()
class C(A, B):
    pass

c = C()
c.method_a()

print(C.mro()) 
        
# class A:
#     def __init__(self, attr_a: str) -> None:
#         self.attr_a = attr_a
        
#     def method(self) -> None:
#         print(f"Метод класса A: {self.attr}")

# class B(A):
#     def __init__(self, attr_b: str) -> None:
#         self.attr_b = attr_b

#     def method(self) -> None:
#         print(f"Метод класса B: {self.attr_b}")
        
# class C(A, B):
#     def __init__(self, attr_a: str, attr_b: str, attr_c: str) -> None:
#         A.__init__(self, attr_a)
#         B.__init__(self, attr_b)
#         self.attr_c = attr_c