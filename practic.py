# cars1 = ("Mers", "BMW", "Lexus")
# cars2 = ("Audi", "Tesla", "Zeekr")

# newCars1 = set(cars1)
# newCars2 = set(cars2)

# total = newCars1.intersection(newCars2)
# print(len(total))

cars = {"tesla": 5000, "BMW": 45000, "Audi": 1000}
carName = input("Унаанын атын жаз: ")
if carName in cars:
    print(f"баасы", cars.values())
else:
    print("Мындай машина жок")
