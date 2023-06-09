# №5.3[35]. Напишите функцию, которая принимает число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя нацело: 1 и само число

# Если число простое - функция возвращает True, если нет - возвращает False

# Примеры/Тесты:

# <function_name>(13) -> True

# <function_name>(10) -> False

a=int(input('Введи число:'))
def check_basic_num(a):
    i=0
    for devider in range(2,a//2+1):
        if a%devider==0:
            i+=1
    if i>1:
        return False
    else: return True

print(check_basic_num(a))            