import random
n = int(input())
m = int(input())
a = []
for i in range(n): # ЗАПОЛНЕНИЕ ДВУМЕРНОГО МАССИВА СЛУЧАЙНЫМИ ЧИСЛАМИ ОТ 0 ДО 9
    a.append([])
    for j in range(m):
        a[i].append(random.randint(0,9))
for i in range(n): # ПЕЧАТЬ ПЕРВИЧНОГО МАССИВА
    for j in range(m):
        print("{:4d}".format(a[i][j]), end = "  ")
    print()
print()
for k in range(n * m - 1):   # СОРТИРОВКА МАССИВА ПО УБЫВАНИЮ
    for i in range(n):
        for j in range(m):
            if j != m - 1:
                if a[i][j] > a[i][j + 1]:
                    a[i][j],a[i][j+1] = a[i][j+1],a[i][j]
            else:
                if i != n - 1:
                    if a[i][j] > a[i + 1][0]:
                        a[i][j], a[i + 1][0] = a[i + 1][0], a[i][j]
for i in range(n): # ПЕЧАТЬ МАССИВА
    for j in range(m):
        print("{:4d}".format(a[i][j]), end = "  ")
    print()
