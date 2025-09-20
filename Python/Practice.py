"""""
a = "Змінна з текстом"
print("a", type(a))

b = 1
print(b, type(b))

b1 = 1.1
print("b1:", b1, type(b1))

c = ["a", 1, 1.25, "Слово", a]
print("c:", c, type(c))

d = {"a": "Слово", "b": 1, "c": a}
print("d:", d, type(d))

e = ("a", a)
print("e:", e, type(e))

f = {"ss", a + " b"}
print("f:", f, type(f))


print("Перша константа:", True)
print("Друга константа:", False)
print("Третя константа:", None)

print(f"І можна так робити вивід? {True}")
print(f"None теж працює: {None}")
"""
"""""
# Приклади вбудованих функцій у Python

print("Модуль числа -12.5:", abs(-12.5))          # abs() → модуль числа
print("Довжина рядка 'Python':", len("Python"))   # len() → довжина
print("Найбільше число з [3, 7, 2]:", max(3, 7, 2))  # max() → найбільший елемент

# А ще можна вивести через f-рядок
print(f"Округлення 3.14159 до 2 знаків: {round(3.14159, 2)}")

print("сума чисел [13 і 11] дорівнює:", sum([13, 11]))

numbers = [1, 7, 9]
print("сума чисел:", sum(numbers))

print("\nЦикл while:")
count = 4
while count > 0:
    print("Залишилось:", count)
    count -= 1

print("Цикл for з range:")
for i in range(6):
    print("Крок:", i)

    fruits = ["яблуко", "банан", "вишня"]
print("\nЦикл for по списку:")
for fruit in fruits:
    print("Фрукт:", fruit)

number = 7
if number % 2 == 0:
    print(f"{number} є парним")
else:
    print(f"{number} є непарним")


try:
    x = 10 / 0   
    print("Результат:", x)
except ZeroDivisionError:
    print("Помилка: ділення на нуль! ")
finally:
    print("Цей блок виконується завжди ")

with open("READ", "r") as f:
    for line in f:
        print(line)

add = lambda a, b: a + b
print(add(3, 1))  
"""