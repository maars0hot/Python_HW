a = int(input("Введите первое неотрицительное число "))
b = int(input("Введите второе неотрицательно число "))


def recurs_sum(a, b):
    if a == 0:
        return b
    else:
        return recurs_sum(a - 1, b + 1)


print(recurs_sum(a, b))