n = int(input('Введите число с 3 до 20:'))
for i in range(1, n):
    for l in range(i + 1, n):
        k = i + l
        if n % k == 0:
            print(i, end='')
            print(l, end='')
