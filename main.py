def calculate_sum(a, b, c):
    return a + b + c
def calculate_product(a, b, c):
    return a * b * c
def main():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        num3 = float(input("Введіть третє число: "))
    except ValueError:
        print("Будь ласка, введіть числа коректно.")
        return
    print("Оберіть операцію:")
    print("1. Обчислити суму трьох чисел")
    print("2. Обчислити добуток трьох чисел")
   
    choice = input("Ваш вибір (1 and 2): ")  
    if choice == '1':
        result = calculate_sum(num1, num2, num3)
        print(f"Сума чисел {num1}, {num2} i {num3} дорівнює {result}.")
    elif choice == '2':
        result = calculate_product(num1, num2, num3)
        print(f"Добуток чисел {num1}, {num2} i {num3} дорівнює {result}.")
    else:
        print("Неправильний вибір опції. Будь ласка, введіть '1' and '2'.")
if __name__ == "__main__":
    main()
--------------------------------------------------------------------------------------------------------------    
   
   
   
   
   
   
 
def calculate_maximum(a, b, c):
    return max(a, b, c)
def calculate_minimum(a, b, c):
    return min(a, b, c)
def calculate_average(a, b, c):
    return (a + b + c) / 3
def main():
    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
        num3 = float(input("Введіть третє число: "))
    except ValueError:
        print("Будь ласка, введіть числа коректно.")
        return
    print("Оберіть операцію:")
    print("1. Знайти максимум із трьох чисел")
    print("2. Знайти мінімум із трьох чисел")
    print("3. Знайти середньоарифметичне трьох чисел")  
    choice = input("Ваш вибір (1, 2 and 3): ")  
    if choice == '1':
        result = calculate_maximum(num1, num2, num3)
        print(f"Максимум із чисел {num1}, {num2} i {num3} дорівнює {result}.")
    elif choice == '2':
        result = calculate_minimum(num1, num2, num3)
        print(f"Мінімум із чисел {num1}, {num2} i {num3} дорівнює {result}.")
    elif choice == '3':
        result = calculate_average(num1, num2, num3)
        print(f"Середнє арифметичне чисел {num1}, {num2} i {num3} дорівнює {result}.")
    else:
        print("Неправильний вибір опції. Будь ласка, введіть '1', '2' and '3'.")
if __name__ == "__main__":
    main()
------------------------------------------------------------------------------------------------------------------
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
def meters_to_miles(meters):
    return meters * 0.000621371
def meters_to_inches(meters):
    return meters * 39.3701
def meters_to_yards(meters):
    return meters * 1.09361
def main():
    try:
        meters = float(input("Введіть кількість метрів: "))
    except ValueError:
        print("Будь ласка, введіть число коректно.")
        return
    print("Оберіть одиницю для конвертації:")
    print("1. Милі")
    print("2. Дюйми")
    print("3. Ярди")  
    choice = input("Ваш вибір (1, 2 and 3): ")  
    if choice == '1':
        result = meters_to_miles(meters)
        print(f"{meters} метрів дорівнює {result} миль.")
    elif choice == '2':
        result = meters_to_inches(meters)
        print(f"{meters} метрів дорівнює {result} дюймів.")
    elif choice == '3':
        result = meters_to_yards(meters)
        print(f"{meters} метрів дорівнює {result} ярдів.")
    else:
        print("Неправильний вибір опції. Будь ласка, введіть '1', '2' and '3'.")
if __name__ == "__main__":
    main()
_______________________________________________________________________________________________________________________________________________________










