# №5.2[33]. Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные.

# Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот: 
# все максимальные – на минимальные.

# Функция должна возвращать новый список оценок

# Примечание: Обратите внимание на side effects функции.

# Примеры/Тесты:

# <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]


def hack(grades):
    max_grades=max(grades)
    min_grades=min(grades)
    if max_grades==min_grades:return None
    for i,item in enumerate(grades):
        if grades[i]==max_grades:
            grades[i]=min_grades


    return grades        

lst=[3,3,3,3,3,3,3,3,3]

print(hack(lst))
