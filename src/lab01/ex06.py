# Задания со звездочкой
# Задание 6*

och = 0
zaoch = 0
n = int(input('in_1: ')) # кол-во строк
c = 2 # для in_{c}, чтобы счёт шел по возрастанию


class human:
    def __init__(self, name = str(), age = 0, out = None):
        self.set_data(name, age, out)

    def set_data(self, name, age, out):
        self.name = name
        self.age = age
        self.out = out


while n>0:                        # вводим данные для каждого участника
    name = input('Фамилия Имя: ')
    age = int(input('Возраст: '))
    form = input('очно/заочно? ')

    if form == 'очно':
        form = True
        och += 1
    else:
        form = False
        zaoch += 1

    information = human(name, age, form)
    print(f'in_{c}: {information.name} {information.age} {information.out}')
    c += 1
    n -= 1

print(f'out: {och} {zaoch}')