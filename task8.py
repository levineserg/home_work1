# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input("Введите длину шоколадки: "))

n = int(input("Введите ширину шоколадки: "))

k = int(input("Сколько долек отломить? "))

if k > (m * n):
    print(m, n, k, "-> no")
elif k % m == 0 or k % n == 0:
    print(m, n, k, "-> yes")
else:
    print(m, n, k, "-> no")
