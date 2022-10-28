# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.
# 1 –> Понедельник
# 10 –> Нет такого дня
# 7 –> Воскресение

# number = int(input("input number: "))

# if number <= 0 or number > 7:
#     print(number, "-> Такого дня недели нет.")

# elif number == 1:
#     print(number, "-> Понедельник")
# elif number == 2:
#     print(number, "-> Вторник")
# elif number == 3:
#     print(number, "-> Среда")
# elif number == 4:
#     print(number, "-> Четверг")
# elif number == 5:
#     print(number, "-> Пятница")
# elif number == 6:
#     print(number, "-> Суббота")
# elif number == 7:
#     print(number, "-> Воскресенье")

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# A (3,6); B (2,1) -> 5,1
# A (7,-5); B (1,-1) -> 7,21

# from math import *
# import numbers

# x1 = float(input("Введите координату x1: "))
# y1 = float(input("Введите координату y1: "))
# x2 = float(input("Введите координату x2: "))
# y2 = float(input("Введите координату y2: "))

# def distance(x1, y1, x2, y2):
#     number = sqrt((x2-x1)**2 + (y2-y1)**2)
#     return number

# number = distance(x1, y1, x2, y2)
# print(number)

# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# 1 -> x > 0, y > 0


# number = int(input("Введите номер четверти: "))

# if number == 1:
#     print("1 -> x > 0, y > 0")
# elif number == 2:
#     print("2 -> x < 0, y > 0")
# elif number == 3:
#     print("3 -> x < 0, y < 0")
# elif number == 4:
#     print("4 -> x > 0, y < 0")


# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

number = int(input("input number: "))
count = 0

while count <= number:
    print(count)
    count += 2