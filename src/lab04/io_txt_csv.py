import csv
from pathlib import Path
from typing import Iterable, Sequence

def read_text(path: str | Path, encoding: str = "cp1251") -> str:
    """
    функция для чтения текстового файла в виде строки
    по умолчанию используется кодировка utf-8
    если файл сохранен в другой кодировке, то нужно указать её в параметре encoding (пример: encoding="cp1251")
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    for i in rows:
        if len(i) != len(rows[0]):
            raise ValueError('Количество элементов в строках не совпадает')
    if rows and header is not None and len(header) != len(rows[0]):
        raise ValueError('Количество элементов в заголовке не совпадает с количеством элементов в строках')
    
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
