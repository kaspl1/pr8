def is_number(value):

    return value.lstrip('-').replace('.', '', 1).isdigit()

while True:
    a = input("Введите первое число (или 'exit' для выхода): ")
    if a.lower() == 'exit':
        break

    if not is_number(a):
        print("Ошибка: введено некорректное значение. Пожалуйста, попробуйте снова.")
        continue

    a = float(a)

    b = input("Введите второе число: ")

    if not is_number(b):
        print("Ошибка: введено некорректное значение. Пожалуйста, попробуйте снова.")
        continue

    b = float(b)


    start = int(min(a, b))
    end = int(max(a, b))

    print("Целые числа между ними:")
    for number in range(start + 1, end):
        print(number)