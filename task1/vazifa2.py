import math

# 1-masala

# a = int(input("soni kiriting; "))
# S = a ** 2
# print("yuzasi",S)

# 2-masala

# d = int(input("soni kiriting; "))
# pi = 3.14
# L = d * pi
# print("Uzunligi", L)

# 3-masala

# L = float(input("Aylananing uzunligini kiriting (L): "))
# pi = 3.14
# R = L / (2 * pi)
# S = pi * R**2
#
# print(f"Radius R = {R}")
# print(f"Yuza S = {S}")

# 4-masala
a = float(input("1-katetni kiriting (a): "))
b = float(input("2-katetni kiriting (b): "))

c = math.sqrt(a**2 + b**2)
P = a + b + c

print(f"Gipotenuza c = {c}")
print(f"Perimetri P = {P}")
