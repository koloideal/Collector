import requests
from func.parser import parser


def helper() -> None:

    print('\nЗдраствуй, я скрипт, который поможет тебе скачать текст песни и её перевод с портала '
          'https://www.amalgama-lab.com\n'
          'Введи ссылку на интересующую тебя песню и я создам файл с результатами в папке contents\n'
          'Если ты передумал введи stop')

    while True:

        try:

            url = input('\nВведите ссылку на интересующий вас трек : ')

            if url.startswith('https://') and url.endswith('.html'):

                code = requests.get(url).status_code

                if url.startswith('https://www.amalgama-lab.com/songs/') and code == 200:

                    break

                else:

                    print('Некорректная ссылка')

            elif url == 'stop':

                print('GoodBye!')

                return

            else:

                print('Введённый текст не является ссылкой')

        except Exception as e:

            print(f'Некорректная ссылка, ошибка - {e}')

    print('\nВ процессе...\n')

    parser(url)

