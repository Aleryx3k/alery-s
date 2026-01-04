def recursive_sum(lst):
    # Базовый случай: если список пуст, возвращаем 0
    if not lst:
        return 0
    # Рекурсивный шаг: первый элемент + сумма остальных
    else:
        return lst[0] + recursive_sum(lst[1:])

# Пример использования:
numbers = [1, 2, 3, 4, 5]
print(f"Сумма списка: {recursive_sum(numbers)}") # Выведет 15
