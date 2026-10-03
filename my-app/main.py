def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b


def main():
    print("Простой калькулятор")
    print("1) +  2) -  3) *  4) /")
    op = input("Выбери операцию: ").strip()
    a = float(input("Первое число: "))
    b = float(input("Второе число: "))

    ops = {"1": add, "2": sub, "3": mul, "4": div}
    if op in ops:
        print("Результат:", ops[op](a, b))
    else:
        print("Неизвестная операция")


if __name__ == "__main__":
    main()
