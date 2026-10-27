from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import normalize, tokenize, count_freq, top_n
import sys

try:
    txt = read_text("data/lab04/input.txt")
except FileNotFoundError:
    print("Файл не найден")
    sys.exit(1)

freq_txt = count_freq(tokenize(normalize(txt)))
sorted_txt = sorted(freq_txt.items(), key=lambda x: (-x[1], x[0]))
write_csv(sorted_txt, "data/lab04/report.csv", header=["word", "count"])

print(f'Всего слов: {len(tokenize(normalize(txt)))}')
print(f"Уникальных слов: {len(count_freq(tokenize(normalize(txt))))}")
print(f"Топ-5 слов:")
for word, count in top_n(freq_txt, 5):
    print(f"{word}: {count}")
