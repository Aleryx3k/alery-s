def find_max(lst):
    # Базовый случай: если в списке один элемент, он и есть максимальный
    if len(lst) == 1:
        return lst[0]
    
    # Рекурсивный шаг: находим максимум в хвосте списка
    max_of_rest = find_max(lst[1:])
    
    # Сравниваем первый элемент с максимумом остальной части
    return lst[0] if lst[0] > max_of_rest else max_of_rest

# Пример использования:
numbers = [3, 15, 7, 9]
print(f"Максимальный элемент: {find_max(numbers)}")
