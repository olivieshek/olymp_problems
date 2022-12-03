a = int(input()) * 86400  # двери в сутки
b = int(input()) * 1440  # колеса в сутки
c = int(input()) * 24  # сиденья в сутки

x = int(input())  # дверей надо
y = int(input())  # колес надо
z = int(input())  # сидений надо

print(int(min(a/x, b/y, c/z)))
