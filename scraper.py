from bs4 import BeautifulSoup
import requests
from utils import get_dollar_amt


def get_values(url):
    retail_val = "No retail value found"
    current_val = "Available at retail"

    result = requests.get(url)
    src = result.content
    soup = BeautifulSoup(src, 'html.parser')

    table = soup.find('table')
    smalls = table.find_all('small')
    parent_divs = set()

    for small in smalls:
        parent_divs.add(small.find_parent())
    for parent_div in parent_divs:
        # print(parent_div)
        text = parent_div.text

        if "$" in text and "Value" in text:
            current_val = get_dollar_amt(str(text))
        elif "$" in text:
            retail_val = get_dollar_amt(str(text))
    return {
            'retail value': retail_val,
            'current value': current_val
            }