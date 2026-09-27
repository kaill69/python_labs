# Задание 1 - Привет и возраст
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

id_1 = human(input('Имя: '), int(input('Возраст: ')))
print(f'Привет, {id_1.name}! Через год тебе будет {id_1.age+1}.')
