def personal_sum(*numbers):
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += float(item)

        except (TypeError, ValueError):
            incorrect_data += 1
    return result, incorrect_data



def calculate_average(*numbers):
    try:
        total_sum, incorrect_count = personal_sum(numbers)
        if len (numbers) - incorrect_count == 0:
            raise ZeroDivisionError("Деление на 0 невозможно.")
        return total_sum / (len(numbers) - incorrect_count)


    except TypeError:
        return "В numbers записан некоректный тип данных"
    except ZeroDivisionError:
        return 0
# Примеры использования этих функций
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')