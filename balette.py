n, k = list(map(int, input().split()))
a = input().split()  # начальная расстановка
q = int(input())

coups = list()

for i in range(q):
    coups.append(list(map(int, input().split())))

print(coups)

for coup in coups:
    a[coup[0] - 1], a[coup[1] - 1] = a[coup[1] - 1], a[coup[0] - 1]


print(a[k - 1])