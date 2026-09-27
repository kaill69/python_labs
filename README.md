# **Лабораторные работы по Python**

## Задание 1.

Выводит информацию, для вывода используется f-строка.

```python
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

id_1 = human(input('Имя: '), int(input('Возраст: ')))
print(f'Привет, {id_1.name}! Через год тебе будет {id_1.age+1}.')
```

# ![Результат задания №1](images/lab1/task№1.png)

## Задание 2.

Вводятся 2 числа, рассчитывается их сумма и среднее арифметическое значение.

```python
nubmer_1 = float(input('введите 1-ое число: ').replace(',', '.'))
nubmer_2 = float(input('введите 2-ое число: ').replace(',', '.'))

print(f'sum={nubmer_2 + nubmer_1:.2f};', f'avg={(nubmer_2+nubmer_1)/2:.2f}')
```

# ![Результат задания №2](images/lab1/task№2.png)
