# print("Hello Wolrd!")
# input("Enter your name: ")

# name = input("Enter your name: ")
# print(name)

# int — целые числа (номера)

# a = 10
# b = 3

# print(a + b)  # 13   сложение
# print(a - b)  # 7    вычитание
# print(a * b)  # 30   умножение
# print(a / b)  # 3.333... деление (float)
# print(a // b)  # 3    целочисленное деление
# print(a % b)  # 1    остаток от деления
# print(a**b)  # 1000 возведение в степень

# x = -15

# print(abs(x))  # 15    модуль числа
# print(pow(x, 2))  # 225   возведение в степень
# print(divmod(x, 4)) # (3, 3) → (частное, остаток)
# print(int("123"))  # 123  преобразование строки в число
# print(bin(10))     # '0b1010' → двоичная
# print(oct(10))     # '0o12' → восьмеричная
# print(hex(10))     # '0xa' → шестнадцатеричная

# float — числа с плавающей точкой (десятичные)

# a = 5.5
# b = 2.0

# print(a + b)   # 7.5   сложение
# print(a - b)   # 3.5   вычитание
# print(a * b)   # 11.0  умножение
# print(a / b)   # 2.75  деление
# print(a // b)  # 2.0   целочисленное деление (float)
# print(a % b)   # 1.5   остаток от деления
# print(a ** b)  # 30.25 возведение в степень

# x = -3.7
# y = 3.14159

# print(abs(x))       # 3.7   модуль числа
# print(round(y, 2))  # 3.14 округление до 2 знаков
# print(pow(2.5, 3))  # 15.625 возведение в степень
# print(divmod(7.5, 2)) # (3.0, 1.5) → частное и остаток
# print(float("3.14"))  # 3.14 преобразование строки в число

# str — строки (текст)

# print("ZhOoDaR".lower())
# print("ZhOoDaR".upper())
# print("ZhOoDaR".title())
# print("ZhOoDaR".capitalize())
# print(len("ZhOoDaR"))
# print("ZhOoDaR".count("O"))
# print("ZhOoDaR".replace("h", "u"))
# print("Zhoodar Jasmin".split())
# print(" ".join(["Zhoodar", "Jasmin"]))

# bool — логический тип

# number = int(input("Сан жаз: "))

# if number > 0:
#     print("+ сан")
# elif number < 0:
#     print("- сан")
# elif number == 0:
#     print("барабар")
# else:
#     print(404)

# age = int(input("Жашынды жаз: "))

# if age > 18:
#     print("толук курактуу")
# elif age == 18:
#     print("18 жашка тен")
# else:
#     print("толук курактагы эмес")

# number1 = int(input("Биринчи сан жаз: "))
# number2 = int(input("Экинчи сан жаз: "))
# print(number1 + number2)

# car = input("Унаанын атын жаз: ")

# print(car.upper())
# print(car.capitalize())
# print(len(car))

# country = input("Оз каалаган олкону жаз: ")

# if country == "Kyrgyzstan":
#     print("Ассалому алейкум")
# elif country == "russia":
#     print("привет")
# elif country == "america":
#     print("Hi")
# else:
#     print(404)

# age = int(input("Жашынды жаз: "))
# if age > 18:
#     print(f"18 жаштан уулу")
# elif age == 18:
#     print(f"18 жашка тен")
# else:
#     print(f"18 жаштан кичине")

# name = input("Атынды жаз: ")
# print(f"Ассалому алейкуи {name}")

# list — список

# cars = ["Mers", "BMW", "Audi", "Lexux", "Toyota", "Supra"]

# print(cars)
# print(cars[1])
# print(cars[-1])
# print(cars[1:4])
# print(cars[::3])
# cars.append("Sonata")
# print(cars)
# cars.insert(3, "Caddilac")
# print(cars)
# cars[-1] = "Nissan"
# print(cars)
# cars.remove("Audi")
# print(cars)
# cars.pop(2)
# print(cars)
# cars.clear()
# print(cars)
# del cars[1:3]
# print(cars)
# print(len(cars))
# print(cars.count("Mers"))
# print(cars[::-1])
# cars.sort()
# cars.sort(reverse=True)
# print(sorted(cars))
# print(sorted(cars, reverse=True))
# print(cars.index("Mers"))

# numbers = [12, 31, 42, 4, 35, 135]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# numbers1 = [1, 2, 3, 4, 5]
# numbers2 = [6, 7, 8, 9, 10]
# print(sorted(numbers1 + numbers2, reverse=True))

# numbers = [34, 51, 345, 134, 6, 36]
# print(f"Эн чон сан {max(numbers)}")
# print(f"Эн кичине сан {min(numbers)}")
# print(f"Суммасы {sum(numbers)}")

# carName = input("Унааны атын жаз: ")
# cars = ["Mers", "BMW", "Audi", "Lexus", "Toyota", "Supra"]

# if carName in cars:
#     cars.remove(carName)
#     print(cars)
# else:
#     print(404)

# carName = input("унаанын атын жаз: ")
# cars = ["Mers", "BMW", "Audi", "Lexus", "Toyota", "Supra"]

# if carName in cars:
#     print("бар")
# else:
#     print("Жок")

# carName = input("унаанын атын жаз: ")
# cars = ["Mers", "BMW"]

# if carName in cars:
#     print("бар")
# else:
#     cars.append(carName)
#     print(cars)

# fruits = ["apple", "banana", "qiwi", "apple", "apple"]
# fruitName = input("Жер жемиш атын жаз: ")
# if fruitName in fruits:
#     print(f"өлчөмү {fruits.count(fruitName)}")
# else:
#     print(f"өлчөмү {fruits.count(fruitName)}")

# tuple — кортеж

# numbers = (41, 34, 12, 4, 515, 34)
# print(numbers[-1])
# print(numbers[::2])
# print(sorted(numbers))
# print(list(numbers))

# text = input("Соз жаз: ")
# if text == text[::-1]:
#     print("Polindrom")
# else:
#     print("No polindrom")
