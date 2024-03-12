from bs4 import BeautifulSoup
import requests
import os
from func import helper


def parser(url: str) -> None:

    try:

        os.makedirs('content', exist_ok=True)

        content = requests.get(url)

        soup = BeautifulSoup(content.text, 'html.parser')

        cont = soup.find('div', class_='texts col')

        original_song_name = cont.find('h2', class_='original').text.replace(' ', '_').replace('?', '').replace(',', '').replace('*', '')

        translate_song_name = cont.find('h2', class_='translate').text

        original = cont.find_all('div', class_='original')
        original = [x.text.replace('\n', '') for x in original]

        translate = cont.find_all('div', class_='translate')
        translate = [x.text.replace('\n', '') for x in translate]

        longest = len(max(original, key=len))

        with open(f'content\\{original_song_name}.txt', 'w', encoding='utf8') as file:

            file.write(original_song_name + ((longest - len(original_song_name) + 1)*' ') + translate_song_name + '\n\n')

            for idk, line in enumerate(original):

                file.write(line + ((longest - len(line) + 1) * ' ') + translate[idk] + '\n')

        yes_no = input('Скрипт успешно завершил работу, желаете продолжить?(y,n)\n')

        if yes_no.lower() in ['y', 'yes', 'ye']:

            helper.helper()

        else:

            print('GoodBye!')

            return

    except Exception as e:

        yes_no = input(f'{e}\nСкрипт завершил работу с ошибкой, желаете продолжить?(y,n)\n')

        if yes_no.lower() in ['y', 'yes', 'ye']:

            helper.helper()

        else:

            print('GoodBye!')

            return
