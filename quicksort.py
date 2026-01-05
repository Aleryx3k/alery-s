def quickSort(array):
    if len(array) < 2: # баз случай
        return array
    else: # начало рекурсии
        pivot = array[0] # опорный элемент
        less = [i for i in array[1:] if i <= pivot] # массивы меньше опорного элемента ПОДМАССИВ

        bigger = [i for i in array[1:] if i > pivot] # массивы больше опорного элемента ПОДМАССИВ
        
        return quickSort(less) + [pivot] + quickSort(bigger)
print(quickSort([30, 20, 3, 1, 100]))

