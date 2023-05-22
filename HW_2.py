# Задача 2: Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n =input('Введите трезначное число:')
sum_digits=0

if len(n) == 3 and n.isdigit():
    n = int(n)
    while n >0:
        digit=n%10
        sum_digits+=digit
        n//=10
    print(f'Сумма цифр числа = {sum_digits}')    
else :
    print('Ввод некорректен')


