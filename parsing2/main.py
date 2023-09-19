
import requests
from bs4 import BeautifulSoup as BS
import csv



# def get_html(url):
#     response = requests.get(url)
#     return response.text


# def get_soup(html):
#     soup = BS(html, 'lxml')
#     return soup


# def get_data(soup):
#     catalog = soup.find('div', class_='row')
#     products = catalog.find_all('div', class_='product-layout')

#     for product in products:

#         info = product.find('div', class_='product-thumb transition')
        
#         try:
#             title = info.find('div', class_='caption').find('div', class_='name').text.strip()
#         except:
#             title = ''
#         try:
#             price = info.find('div', class_='caption').find('div', class_='price').text.strip()
#         except:
#             price = ''
#         try:
#             img = info.find('div', class_='image').find('a').find('img').get('data-src')
#         except:
#             img = ''


#         data = {
#             'title': title,
#             'price': price,
#             'image': img
#         }

#         write_csv(data)


# def write_csv(data: dict) -> None:

#     with open('softech.csv', 'a') as csv_file:

#         fieldnames = ['title', 'price', 'image']
#         writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
#         writer.writerow(data)


# def main():

#     html = get_html('https://softech.kg/noutbuki')
#     soup = get_soup(html)
#     get_data(soup)


# main()







def get_html(url):
    response = requests.get(url)
    return response.text


def get_soup(html):
    soup = BS(html, 'lxml')
    return soup


def get_data(soup):
    catalog = soup.find('div', class_='row')
    products = catalog.find_all('div', class_='product-layout')

    for product in products:

        info = product.find('div', class_='product-thumb transition')
        
        try:
            title = info.find('div', class_='caption').find('div', class_='name').text.strip()
        except:
            title = ''
        try:
            price = info.find('div', class_='caption').find('div', class_='price').text.strip()
        except:
            price = ''
        try:
            img = info.find('div', class_='image').find('a').find('img').get('data-src')
        except:
            img = ''


        data = {
            'title': title,
            'price': price,
            'image': img
        }

        write_csv(data)


def write_csv(data: dict) -> None:

    with open('softech.csv', 'a') as csv_file:

        fieldnames = ['title', 'price', 'image']
        writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=fieldnames)
        writer.writerow(data)


def main():

    html = get_html('https://softech.kg/noutbuki')
    soup = get_soup(html)
    get_data(soup)


main()