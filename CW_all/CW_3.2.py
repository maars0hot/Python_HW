# №3.2[19]. Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,
# K – положительное число.

# Примечание: Пользователь может вводить значения списка или список задан изначально.

# Примеры/Тесты:

# Input: [1, 2, 3, 4, 5] k = 3

# Output: [4, 5, 1, 2, 3]

list1 = [1, 2, 3, 4, 5]
list2=[]
k=3
list2=list1[k:]+list1[:k]
print(list2)





