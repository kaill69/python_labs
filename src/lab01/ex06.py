# Задания со звездочкой
# Задание 6*

och = 0
zaoch = 0
n = int(input('in_1: ')) # кол-во строк

for i in range(2, n + 2):
    get_data = input(f'in_{i}: ').split()
    if get_data[-1] == 'True':
        och +=1
    else: zaoch += 1

print(f'out: {och} {zaoch}')