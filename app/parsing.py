import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

base_url = "kupidonia.ruspisok/spisok-suschestvitelnyh-russkogo-jazyka/bukva"

letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЭЮЯ"
all_nouns = []

for letter in tqdm(letters):
    url = f"{base_url}/{letter}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        if table:
            for row in table.find_all('tr'):
                columns = row.find_all('td')
                for column in columns:
                    noun = column.text.strip()
                    if noun and len(noun) > 5:
                        all_nouns.append(noun)

print(len(all_nouns))


with open("../data/words.txt", "w", encoding="utf-8") as file:
    for noun in all_nouns:
        file.write(noun + "\n")