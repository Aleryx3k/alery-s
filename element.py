def count_element(list):
    if not list:
        return 0
    return 1 + count_element(list[1:]) 
print(count_element([1,2,3,4,5,6]))