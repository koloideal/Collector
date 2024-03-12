import requests
from func.parser import parser


def helper() -> None:

    while True:

        try:

            url = input('\nВведите ссылку на интересующий вас трек : ')

            code = requests.get(url).status_code

            if url.startswith('https://www.amalgama-lab.com/songs/') and code == 200:

                break

            else:

                print('Неккоректная ссылка')

        except ConnectionError:

            print('Сайт не отвечает или же введённой ссылки не существует')

    print('В процессе...')

    parser(url)

