def sum_numbers():
    """Запрашивает числа у пользователя до тех пор, пока не будет введен 'stop' и 'end', затем выводит сумму."""

    numbers = []
    while True:
        user_input = input("Введите число (или 'stop' и 'end' для завершения): ")
        if user_input.lower() == 'stop' and len(numbers)>0: #проверка на непустой список
            break
        elif user_input.lower() == 'end' and len(numbers)>0: #проверка на непустой список
            break
        try:
            number = float(user_input)  # Преобразуем в число, если возможно
            numbers.append(number)
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число или 'stop' и 'end'.")

    if numbers:  # Проверка на случай, если пользователь сразу ввел "stop" и "end"
        total = sum(numbers)
        print(f"Сумма введенных чисел: {total}")
    else:
        print("Вы не ввели ни одного числа.")


if __name__ == "__main__":
    sum_numbers()