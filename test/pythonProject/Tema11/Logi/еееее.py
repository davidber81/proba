import requests as rq
import logging
import requests.exceptions

formatting = '[%(levelname)s]: %(message)s'
logging.basicConfig(level=logging.INFO, format=formatting)
logger = logging.getLogger('RequestsLogger')

sites = ['https://www.youtube.com/',
         'https://instagram.com',
         'https://wikipedia.org',
         'https://yahoo.com',
         'https://yandex.ru',
         'https://whatsapp.com',
         'https://twitter.com',
         'https://amazon.com',
         'https://tiktok.com',
         'https://www.ozon.ru']


success_log = 'success_response.log'
bad_log = 'bad_responses.log'
blocked_log = 'blocked_response.log'

def write_to_file(file_name, message):
    with open(file_name, 'a') as file:
        file.write(message + '\n')

for site in sites:
    try:
        response = rq.get(site, timeout=3)

        if response.status_code == 200:
            logging.info(f'{site} response - {response.status_code}')
            write_to_file(success_log, f'INFO {site} response - {response.status_code}')

        elif response.status_code != 200:
            logging.warning(f'{site} response - {response.status_code}')
            write_to_file(bad_log, f'WARNING {site} response - {response.status_code}')

    except requests.exceptions.RequestException as e:
        logging.error(f'{site} No Connection')
        write_to_file(blocked_log, f'ERROR {site} NO CONNECTION')