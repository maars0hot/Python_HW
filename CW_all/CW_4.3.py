# №4.3[29]. Для натурального n создать список, состоящий из элементов последовательности 
# 3n + 1.

# Пример:

# - Для n = 6: [1, 4, 7, 10, 13, 16, 19]

# Усложнение:

# Создать список, где указанные числа будут стоять на соответствующих индексах, 
# остальные элементы сделать нулевыми, т.е. для индекса 1, значение 1,

# для индекса 4, значение 4 и т.п.

# Пример:

# - Для n = 6: [0,1,0,0,4,0,0,7,0,0,10]

# n=int(input('Введите число'))
# list_1=[0]*(3*n+2)
# for i in range(n+1):
#     x=3*i+1
#     list_1[x]=x
# print(list_1)

#ВТОРОЙ ВАРИАНТ РЕШЕНИЯ 

n=int(input('Введите число'))
list_1=[]
for i in range(n+1):
    list_1.append(0)
    list_1.append(3*i+1)
    list_1.append(0)
list_1.pop()    
print(list_1)

