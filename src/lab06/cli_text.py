import argparse
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n


def cmd_cat(input_path: str, number_lines: bool) -> None:

    path = Path(input_path)
    if not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    with open(path, "r", encoding="utf-8") as f:
        lineno = 1
        for line in f:
            clean_line = line.rstrip("\n")
            if number_lines:
                print(f"{lineno}: {clean_line}")
            else:
                print(clean_line)
            lineno += 1



def cmd_stats(input_path: str, top: int) -> None:

    path = Path(input_path)
    if not path.is_file():
        raise FileNotFoundError(f"Файл не найден: {input_path}")

    text = path.read_text(encoding="utf-8")
    tokens = tokenize(normalize(text))
    freqs = count_freq(tokens)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freqs)}")
    print(f"Топ-{top} слов:")
    for word, count in top_n(freqs, top):
        print(f"{word}: {count}")


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI-утилита для работы с текстом (cat и stats)")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Доступные подкоманды")

    # Подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла построчно")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать выводимые строки")

    # Подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Посчитать статистику и частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество самых частых слов (по умолчанию: 5)")
    args = parser.parse_args()

    if args.command == "cat":
        cmd_cat(args.input, args.n)
    elif args.command == "stats":
        if args.top <= 0:
            parser.error("Параметр --top должен быть положительным целым числом")
        cmd_stats(args.input, args.top)


if __name__ == "__main__":
    main()
