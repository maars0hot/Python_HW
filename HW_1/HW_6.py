# Задача 6: Вы пользуетесь общественным транспортом? Вероятно,
# вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n_input =(input('Введите номер билета:'))

left_side =int(n_input[0:3])
right_side = int(n_input[3:6])

sum_left=0

while left_side>0:
    digit=left_side%10
    sum_left+=digit
    left_side//=10
sum_right=0
while right_side>0:
    digit=right_side%10
    sum_right+=digit
    right_side//=10

if sum_right==sum_left:
    print(f'ВАШ БИЛЕТ {n_input} - СЧАСТЛИВЫЙ!')
else:
    print('В следующий раз повезет!')

print(f'Сумма правой стороны - {sum_right} , левой стороны - {sum_left}')   