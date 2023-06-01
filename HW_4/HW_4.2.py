# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и 
# с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать 
# за один заход собирающий модуль, находясь перед некоторым кустом. 
# На входе задано количество ягод на каждом кусте. 
# Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы

#     Примеры/Тесты:
#     Input1: 1, 2, 3, 4, 5, 6, 7, 8
#     Output1: Макс. кол-во ягод 21, собрано для куста 7

#     Input1: 11, 92, 1, 42, 15, 12, 11, 81
#     Output1: Макс. кол-во ягод 184, собрано для куста 1

n=int(input())
lst=list()
for i in range(n):
    x=int(input())
    lst.append(x)

lst_count=list()
for i in range(len(lst)-1):
    lst_count.append(lst[i-1]+lst[i]+lst[i+1])
print(f'Максимум ягод -> {max(lst_count)}, собрано для куста {lst[i]}')    
