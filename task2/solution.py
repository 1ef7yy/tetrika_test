import requests
import os
from bs4 import BeautifulSoup
import csv


def get_animals_count() -> dict[str, int]:
    URL = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    letter_counts = {}

    while True:
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

        category_groups = soup.find("div", class_="mw-category-columns")

        if not category_groups:
            category_groups = soup.find("div", class_="mw-category")

        groups = category_groups.find_all(["div", "h3"])

        current_letter = None
        for element in groups:
            if element.name == "h3":
                current_letter = element.text.strip()
                if current_letter not in letter_counts:
                    letter_counts[current_letter] = 0
            elif element.name == "div" and current_letter:
                items = element.find_all("a")
                letter_counts[current_letter] += len(items)

        next_page = soup.find("a", string="Следующая страница")
        if not next_page:
            break

    return letter_counts


def write_to_csv(counts: dict[str, int]) -> None:
    filename = "beasts.csv"
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if not dir_path.endswith("task2"):
        filename = "task2/beasts.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])


if __name__ == "__main__":
    counts = get_animals_count()
    write_to_csv(counts)
    print("данные успешно записаны в beasts.csv")
