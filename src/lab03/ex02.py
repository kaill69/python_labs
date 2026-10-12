import sys
sys.path.append(r"c:\Users\Kirill\Documents\vs code\python_labs")
from src.lib.text import normalize, tokenize, count_freq, top_n

text = input('Введите предложение: ')
text = normalize(text)
count = 0
for i in tokenize(text):
    count += 1
unic = count_freq(tokenize(text))

print(f'Всего слов: {count}')
print(f"Уникальных слов: {len(unic)}")
c = 0
print('Топ-5:')
for i in top_n(unic):
    if c == 5:
        break
    print(f'{i[0]}:{i[1]}')
    c += 1