
def main():
    start = int(input("Введіть початок діапазону: "))
    end = int(input("Введіть кінець діапазону: "))
    print(f"Числа кратні 7 у діапазоні від {start} до {end}:")
    for number in range(start, end + 1):
        if number % 7 == 0:
            print(number)
if __name__ == "__main__":
    main()
-----------------------------------------------------------------------

def main():
    start = int(input("Введіть початок діапазону: "))
    end = int(input("Введіть кінець діапазону: "))
    print(f"Всі числа в діапазоні від {start} до {end}:")
    for number in range(start, end + 1):
        print(number, end=" ")
    print()
    print(f"Всі числа в діапазоні від {end} до {start} у спадному порядку:")
    for number in range(end, start - 1, -1):
        print(number, end=" ")
    print()
    print(f"Числа, кратні 7, в діапазоні від {start} до {end}:")
    for number in range(start, end + 1):
        if number % 7 == 0:
            print(number, end=" ")
    print()  
    count_multiples_of_5 = 0
    for number in range(start, end + 1):
        if number % 5 == 0:
            count_multiples_of_5 += 1
    print(f"Кількість чисел, кратних 5, в діапазоні від {start} до {end}: {count_multiples_of_5}")
if __name__ == "__main__":
    main()
---------------------------------------------------------------------------------------------------

def fizz_buzz_analysis(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print("Fizz Buzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
start = int(input("Введіть початок діапазону: "))
end = int(input("Введіть кінець діапазону: "))
fizz_buzz_analysis(start, end)
___________________________________________________________________________________________________________