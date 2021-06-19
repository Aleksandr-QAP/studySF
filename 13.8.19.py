n = int(input('Число посетителей'))
result = 0
for i in range(n,):
    age = int(input("Возраст посетителей"))
    if age < 18:
        result += 0
    elif 18 <= age < 25:
        result += 990
    elif 25 <= age:
        result += 1390
if n > 3:
    result = result * 0.9
print("Стоимость всех билетов с учетом скидки", result)