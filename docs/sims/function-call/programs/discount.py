def discount(total, member):
    pay = total
    if total >= 100:
        pay = pay - 15
    if member:
        pay = pay * 0.95
    return round(pay, 2)

a = discount(128, True)
b = discount(86, False)
print(a, b)
