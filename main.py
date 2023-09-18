# requests - библиотека помагает нам работать с http запросами 

# bs4  -  позволяет нам извлекать информацию из html данная библиотека разбирается в тегах, 
# различает от обычного текста она может извлекать данные из нужных нам тегов


import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url: str) -> str:
    response = requests.get(url)
    return response.text



def get_data(html):
    soup = BS(html, 'lxml')
    catalog = soup.find('div', class_='catalog-list')
    cars = catalog.find_all('a', class_='catalog-list-item')
  

    for car in cars:

        try:
            title = car.find('span', class_='catalog-item-caption').text.strip()
            ind = title.index(',')
            title = title[:ind]
        except:
            title = ''

        try:
            price = car.find('span', class_='catalog-item-price').text.strip()
        except:
            price = ''

        try:
            img = car.find('img', class_='catalog-item-cover-img').get('src')
        except:
            img = ''

        try:  
            discription = car.find('span', class_='catalog-item-descr').text.strip()
        except:
            discription = ''

        try:
            date = car.find('span', class_='catalog-item-info').text.strip()
        except:
            date = ''

        data = {
                'title': title,
                'price': price,
                'deta': date,
                'discription': discription,
                'image': img
                }

        write_csv(data)


def write_csv(data: dict) -> None:

    with open('cars.csv', 'a') as csv_file:

        fieldnames = ['title', 'price','deta', 'discription', 'image']
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
        writer.writerow(data)


def main():
    # url = 'https://cars.kg/offers'
    # html = get_html(url)
    # get_data(html)

    for page in range(1,2):
        url = f'https://cars.kg/offers/{page}'
        print(f'Парсинг {page} страницы!!')
        html = get_html(url)
        get_data(html)
        print(f'Парсинг {page} страницы завершен!!')

main()


# print(get_html('https://pythonru.com/osnovy/stroki-python'))