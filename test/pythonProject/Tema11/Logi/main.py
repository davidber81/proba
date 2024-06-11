# import bs4
# import requests as rq
# import logging
#
# logger = logging.getLogger('RequestsLogger')
#
# sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
#          'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
#          'https://www.ozon.ru']
#
# for site in sites:
#     try:
#         response = rq.get(site, timeout=3)
#         soup = bs4.BeautifulSoup(response.text, 'lxml')
#         print(response)
#     except:
#         print('NO CONNECTION')
#     logging.basicConfig(filename="success_responses.log", level=logging.INFO)
#     logging.basicConfig(filename="bad_responses.log", level=logging.WARNING)
#     logging.basicConfig(filename="blocked_responses.log", level=logging.ERROR)
#     if response.status_code == 200:
#
#         logger.info(f'Info: {site}', extra={"response": response.text})
#     elif response.status_code != 200:
#         # logging.basicConfig(filename="bad_responses.log", level='WARNING')
#         logger.warning(f'{site}', extra={"response": response.text})
#     elif response.status_code == 'NO CONNECTION':
#         # logging.basicConfig(filename="blocked_responses.log")
#         logger.error(f'Error: {site}', extra={"response": 'NO CONNECTION'})

import logging
import bs4
import requests as rq

logging.basicConfig(level=logging.INFO)

sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',         'https://www.ozon.ru']

info_handler = logging.FileHandler("success_responses.log")
info_handler.setLevel(logging.INFO)
warning_handler = logging.FileHandler("bad_responses.log")
warning_handler.setLevel(logging.WARNING)
error_handler = logging.FileHandler("blocked_responses.log")
error_handler.setLevel(logging.ERROR)

logger = logging.getLogger('RequestsLogger')
logger.addHandler(info_handler)
logger.addHandler(warning_handler)
logger.addHandler(error_handler)

for site in sites:
    try:
        response = rq.get(site, timeout=3)
        soup = bs4.BeautifulSoup(response.text, 'lxml')
        print(response)
        if response.status_code == 200:
            logger.info(f'INFO: {site}, "response -", {response.status_code}')
        else:
            logger.warning(f'WARNING: {site}, "response -", {response.status_code}')
    except Exception as e:
        logger.error(f'Error: {site}, "NO CONNECTION"')

for handler in logger.handlers:
    handler.close()
