# def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
#     text = text.replace("\t", " ")
#     text = text.replace("\r", " ")
#     text = text.replace("\n", " ")
    
#     if yo2e:
#             text = text.replace("ё", "е").replace('Ё', 'Е')
#     if casefold:
#         text = text.casefold()

#     text = " ".join(text.split())
#     return text.strip()

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка", yo2e = True))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))

# import re
# def tokenize(text: str):
#     a = re.findall(r"\w+(?:-\w+)*", text)
#     return a

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

# def count_freq(tokens: list[str]):
#     grz = {}
#     unic = sorted(set(tokens))
#     for i in unic:
#         grz[i] = tokens.count(i)
#     return grz

# def top_n(freq: dict[str, int], n: int = 5):
#     sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
#     return sorted_items[:n]

# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))

# print(top_n(count_freq(["a","b","a","c","b","a"]), n = 2))
# print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n = 2))