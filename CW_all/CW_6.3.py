# №6.3[43] Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.

# Считается, что любые два элемента, равные друг другу, образуют одну пару, которую 
# необходимо посчитать.

# Напишите функцию

# Аргументы: список целых чисел

# Возвращает: кол-во пар

# Примеры/Тесты:

# <function_name>([1, 2, 3, 2, 3]) -> 2

# <function_name>([1, 2, 3, 2, 3, 3, 2, 4]) -> 6


# def count_pairs(list1:list)->int:
#     result=0
#     for idx in range(len(list1)):
#         for idx2 in range(idx+1,len(list1)):
#             if list1[idx]==list1[idx2]:
#                 result+=1
#     return result     

def count_pairs(list1:list)->int:
    result=0
    for idx in range(len(list1)):
        result+=list1[idx+1:].count(list1[idx])
    return result    




print(count_pairs([1, 2, 3, 2, 3]))

print(count_pairs([1, 2, 3, 2, 3, 3, 2, 4]))

