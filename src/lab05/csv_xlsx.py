import csv
import os
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(csv_path, 'r', encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    if not data:
        raise ValueError("CSV пустой")

    for row in data:
        ws.append(row)

    for col in ws.columns:
        max_length = 0
        column_letter = col[0].column_letter

        for cell in col:
            if cell.value:
                length = len(str(cell.value))
                if length > max_length:
                    max_length = length

        ws.column_dimensions[column_letter].width = max(max_length + 2, 8)

    os.makedirs(os.path.dirname(xlsx_path), exist_ok=True)
    wb.save(xlsx_path)

if __name__ == "__main__":
    csv_path = (
        "data/samples/people.csv"
        if os.path.exists("data/samples/people.csv")
        else "data/lab05/samples/people.csv"
    )
    out_dir = "data/out" if "data/samples" in csv_path else "data/lab05/out"
    csv_to_xlsx(csv_path, f"{out_dir}/people.xlsx")