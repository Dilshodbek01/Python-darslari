# a va b o'zgaruvchilarini aniqlash
a = 6
b = 3

# 1. Ikki sonni qo'shish
def add(a, b):
    return a + b
print(f"1. {a} + {b} = {add(a, b)}")

# 2. Birinchi sondan ikkinchi sonni ayirish
def subtract(a, b):
    return a - b
print(f"2. {a} - {b} = {subtract(a, b)}")

# 3. Sonlarni ko'paytirish
def multiply(a, b):
    return a * b
print(f"3. {a} * {b} = {multiply(a, b)}")

# 4. Ikkinchi sonni birinchi songa bo'lish
def divide(a, b):
    if b != 0:
        return a / b
    return "Xatolik"
print(f"4. {a} / {b} = {divide(a, b)}")

# 5. Qoldiqni topish
def remainder(a, b):
    return a % b
print(f"5. {a} % {b} = {remainder(a, b)}")

# 6. Butun qismni topish
def quotient(a, b):
    return a // b
print(f"6. {a} // {b} = {quotient(a, b)}")

# 7. Kvadratlarini qaytarish
def squares(a, b):
    return a ** 2, b ** 2
print(f"7. {a}^2, {b}^2 = {squares(a, b)}")

# 8. A^B
def power(a, b):
    return a ** b
print(f"8. {a}^{b} = {power(a, b)}")

# 9. Ko'paytma va yig'indini taqqoslash
def compare_product_sum(a, b):
    return a * b > a + b
print(f"9. {a} * {b} > {a} + {b} = {compare_product_sum(a, b)}")
