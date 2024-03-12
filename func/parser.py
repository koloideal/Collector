from bs4 import BeautifulSoup
import requests
import os


def parser(url: str) -> None:

    try:

        os.makedirs('/home/kolo/Python_Projects/Collector/content', exist_ok=True)

        content = requests.get(url)

        soup = BeautifulSoup(content.text, 'html.parser')

        cont = soup.find('div', class_='texts col')

        print(cont)

        original_song_name = cont.find('h2', class_='original').text

        translate_song_name = cont.find('h2', class_='translate').text

        original = cont.find_all('div', class_='original')

        translate = cont.find_all('div', class_='translate')

        longest = len(max([x.text for x in original], key=len))

        with open(f'/home/kolo/Python_Projects/Collector/content/{original_song_name}.txt', 'w', encoding='utf8') as file:

            file.write(original_song_name + ((longest - len(original_song_name) + 1)*' ') + translate_song_name + '\n\n')

            for idk, line in enumerate(original):

                file.write(line.text + ((longest - len(line.text) + 1) * ' ') + translate[idk].text + '\n')

        print(f'Скрипт успешно завершил работу')

    except Exception as e:

        print(f'Скрипт завершил работу с ошибкой, {e}')
