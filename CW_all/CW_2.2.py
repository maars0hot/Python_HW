# №2.3[13]. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).

# Затем пользователь последовательно вводит температуру для каждого дня. Температуры – целые числа и лежат в диапазоне от –50 до 50

# Необходимо вычислить длительность самой длинной оттепели

# Примеры/Тесты:

# Введите число рассматриваемых дней>? 11

# Введите среднесуточную температуру для дня 1>? 1

# Введите среднесуточную температуру для дня 2>? 7


n = int(input('Введите кол-во рассматриваемых дней:'))
maxStrick=0
currentTemp=0
currentStrick=0
for i in range(n):
    currentTemp=int(input('Введите температуру:'))
    if currentTemp=='':
        print('Ввод данных закончен')
        break
    if currentTemp>0:
        currentStrick+=1
    else:
        if currentStrick>maxStrick:
            currentStrick=maxStrick
        currentStrick=0
    if currentStrick>maxStrick:
        maxStrick=currentStrick

print(f'Теплых дней - {maxStrick}')
                
