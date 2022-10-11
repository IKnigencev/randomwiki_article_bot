import logging

import requests


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

URL = "https://ru.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "random",
    "rnlimit": "1"
}


def get_title_and_link() -> str:
    try:
        response = requests.get(url=URL, params=PARAMS)
        data = response.json()
        random_article = data["query"]["random"]

        title = random_article[0].get("title")
        link = str(title).replace(' ', '_')
        link = f'https://ru.wikipedia.org/wiki/{link}'

        result = f'{title} \n {link}'

        return result
    except Exception as error:
        logging.error(f'Ошибка при подключение к API: {error}')
        result = 'Мы к сожалению не смогли подключится к API википедии'

        return result


def main():
    result = get_title_and_link()
    return result


if __name__ == '__main__':
    main()
