def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2  # Находим середину
        guess = data[mid]
        
        if guess == target:      # Значение найдено
            return mid
        if guess > target:       # Искомое в левой половине
            high = mid - 1
        else:                    # Искомое в правой половине
            low = mid + 1
            
    return -1  # Элемент не найден
print(binary_search_iterative([5,7,1,2,3,8],1))