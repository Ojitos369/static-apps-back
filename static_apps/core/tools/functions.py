# Python
import requests

from bs4 import BeautifulSoup


def print_line_center(error):
    print()
    print(error)
    print()


def currency_convertions(amount, currency_from, currency_to):
    url = f'https://www.google.com/finance/quote/{currency_from.upper()}-{currency_to.upper()}'
    page = requests.get(url)
    # print(url)
    soup = BeautifulSoup(page.content, 'lxml')
    # div class YMlKec fxKbKc
    results = soup.select('.YMlKec.fxKbKc')
    results = results[0]
    results = results.contents[0]
    results = float(results)
    results = results * float(amount)
    results = round(results, 2)
    # print(results)
    return results
