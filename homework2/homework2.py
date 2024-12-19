def is_integer(value):
    return value.lstrip('-').isdigit()

while True:
    num1 = input("Введите первое целое число (или 'exit' для выхода): ")
    if num1.lower() == 'exit':
        break

    if not is_integer(num1):
        print("Ошибка: введено некорректное значение. Пожалуйста, попробуйте снова.")
        continue

    num1 = int(num1)

    num2 = input("Введите второе целое число: ")

    if not is_integer(num2):
        print("Ошибка: введено некорректное значение. Пожалуйста, попробуйте снова.")
        continue

    num2 = int(num2)

    print(f"Сумма: {num1 + num2}")