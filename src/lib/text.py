import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")
    
    if yo2e:
            text = text.replace("ё", "е").replace('Ё', 'Е')
    if casefold:
        text = text.casefold()

    text = " ".join(text.split())
    return text.strip()

def tokenize(text: str):
    a = re.findall(r"\w+(?:-\w+)*", text)
    return a

def count_freq(tokens: list[str]):
    grz = {}
    unic = sorted(set(tokens))
    for i in unic:
        grz[i] = tokens.count(i)
    return grz

def top_n(freq: dict[str, int], n: int = 5):
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    return sorted_items[:n]