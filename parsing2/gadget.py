import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    response = requests.get(url, headers=headers)
    return response.text


def get_soup(html):
    soup = BS(html, 'lxml')
    return soup


def get_last_page(soup):
    p = soup.find('ul', class_='pagination__list')
    page = p.find_all('li')[-2]
    return page.text

def is_next(soup):
    p = soup.find('ul', class_='pagination__list')
    is_n = p.find('a', id='NextLink')
    return is_n


def get_data(soup):
    toys = soup.find_all('div', class_='hit__slide')
    
    for product in toys:
        
        try:
            title = product.find('h6', class_='hit__slide__title').text
        except:
            title = ''
        try:
            price = product.find('span', class_='hit__slide__price').text
        except:
            price = ''
        try:
            img = product.find('div', class_='hit__slide__pic').find('img').get('src')
            img = 'https://www.gadget.kg' + img
        except:
            img = ''


        data = {
            'title': title,
            'price': price,
            'image': img
        }

        write_csv(data)


def write_csv(data: dict) -> None:

    with open('gadget.csv', 'a') as csv_file:

        fieldnames = ['title', 'price', 'image']
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
        writer.writerow(data)


def main():
    BASE_URL = 'https://www.gadget.kg/catalog/games/igrovye-pristavki-konsoli'
    
    count = 1
    while True:
        url = f'{BASE_URL}/?page={count}'
        html = get_html(url)
        soup = get_soup(html)
        last_page = get_last_page(soup)
        print(f'Страницы {count} / Последняя страница {last_page}')
        get_data(soup)

        if not is_next(soup) or count > int(last_page):
            break
        count += 1


main()



# html = get_html('https://www.gadget.kg/catalog/games/igrovye-pristavki-konsoli')
# soup = get_soup(html)
# get_last_page(soup)
# get_data(soup)
