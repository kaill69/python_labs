# **Лабораторные работы по Python**

## Задание 1.

```python
class human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

id_1 = human(input('Имя: '), int(input('Возраст: ')))
print(f'Привет, {id_1.name}! Через год тебе будет {id_1.age+1}.')```

![Результат задания №1](images/lab01/task№1.png)
