import argparse
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-конвертер табличных и структурированных данных (JSON, CSV, XLSX)")
    sub = parser.add_subparsers(dest="cmd", required=True, help="Режим конвертации")

    p1 = sub.add_parser("json2csv", help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Путь к входному JSON-файлу")
    p1.add_argument("--out", dest="output", required=True, help="Путь к выходному CSV-файлу")

    p2 = sub.add_parser("csv2json", help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Путь к входному CSV-файлу")
    p2.add_argument("--out", dest="output", required=True, help="Путь к выходному JSON-файлу")

    p3 = sub.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Путь к входному CSV-файлу")
    p3.add_argument("--out", dest="output", required=True, help="Путь к выходному XLSX-файлу")

    args = parser.parse_args()

    in_path = Path(args.input)
    if not in_path.is_file():
        raise FileNotFoundError(f"Файл не найден: {args.input}")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if args.cmd == "json2csv":
        json_to_csv(str(in_path), str(out_path))
        print(f"Успешно: {in_path} -> {out_path}")

    elif args.cmd == "csv2json":
        csv_to_json(str(in_path), str(out_path))
        print(f"Успешно: {in_path} -> {out_path}")
        
    elif args.cmd == "csv2xlsx":
        csv_to_xlsx(str(in_path), str(out_path))
        print(f"Успешно: {in_path} -> {out_path}")


if __name__ == "__main__":
    main()
