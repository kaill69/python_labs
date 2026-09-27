# Задание 3 — Чек: скидка и НДС

price = float(input('цена: '))
discount = float(input('скидка(%): '))
vat = float(input('НДС(%): '))

base = price * (1 - discount / 100) # цена со скидкой
vat_amount = base * (vat / 100) # ндс
total = base + vat_amount # цена + ндс

print(f'База после скидки: {base:.2f} ₽')
print(f'НДС:               {vat_amount:.2f} ₽')
print(f'Итого к оплате:    {total:.2f} ₽')