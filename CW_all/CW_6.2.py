# №6.2[41] Дан список, целых чисел.

# Напишите функцию, которая определит те элементы списка, у которых два соседних и, 
# при этом, оба соседних элемента меньше данного.

# Функция

# Аргументы: список целых чисел

# Возвращает: список элементов (смотри условие)

# Примеры/Тесты:

# <function_name>([1, 3, 3, 3, 5]) -> [5]

# <function_name>([1, 5, 1, 6, 1]) -> [5,6]

# <function_name>([7, 5, 1, 6, 8]) -> [8]

# <function_name>([8, 1, 5, 4, 5]) -> [8,5]

def near_el(list1:list)->list:
    res=list()
    for idx in range(len(list1)-1):
        if list1[idx-1]<list1[idx] and list1[idx+1]<list1[idx]:
            res.append(list1[idx])
    idx=len(list1)-1
    if list1[idx-1]<list1[idx] and list1[0]<list1[idx]:
            res.append(list1[idx])        
    return res

print(near_el([1, 3, 3, 3, 5]))
print(near_el([1, 5, 1, 6, 1]))
print(near_el([7, 5, 1, 6, 8]))
print(near_el([8, 1, 5, 4, 5]))



