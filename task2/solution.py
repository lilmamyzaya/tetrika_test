import requests
from bs4 import BeautifulSoup
import csv


def count_animals():
    url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    counts = {}

    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        animal_blocks = soup.select(".mw-category-group ul li a")
        for animal in animal_blocks:
            name = animal.text.strip()
            if not name:
                continue
            first_letter = name[0].upper()
            counts[first_letter] = counts.get(first_letter, 0) + 1

        next_page = soup.find("a", string="Следующая страница")
        url = f"https://ru.wikipedia.org{next_page['href']}" if next_page else None

    with open("beasts.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])


if __name__ == "__main__":
    count_animals()