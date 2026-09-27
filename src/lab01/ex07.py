# Задание 7
flag_Big = False
flag_chis = False
out = '' # изначальная строка
ind_big = 0
ind_chisla = 0
a = str(input('in: ')) # ввод зашифрованного числа

for i in range(len(a)):        # Ищем первую заглавную букву из списка
    if flag_Big == False:      # через флаги находим только одну заглавную букву
        if 'A' <= a[i] <= 'Z':
            flag_Big = True
            out += a[i]
            ind_big = i

for i in range(ind_big+1, len(a)):   # Ищем первую цифру после заглавной
    if flag_chis == False:
        if '0' <= a[i] <= '9':
            flag_chis = True
            ind_chisla = i

different = ind_chisla - ind_big + 1  # сможем найти, через сколько символов стоят числа строки друг от друга, +1 для того чтобы выбрать следущий символ после числа

for i in range(ind_chisla+1, len(a), different): # собирает "изначальную" строку
    out += a[i]
    if a[i] == '.':
        break

print(f'out: {out}')