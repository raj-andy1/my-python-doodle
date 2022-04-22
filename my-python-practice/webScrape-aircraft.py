import requests
from bs4 import BeautifulSoup


def getSoup(URL, id='main'):
    """

    :param id:
    :param URL:
    :return:
    """
    soup = BeautifulSoup(requests.get(URL).content, 'html.parser')
    if debug:
        print(requests.get(URL).text)
    return soup.find(id=id)


def cfDecodeEmail(encodedString):
    r = int(encodedString[:2], 16)
    email = ''.join([chr(int(encodedString[i:i + 2], 16) ^ r) for i in range(2, len(encodedString), 2)])
    return email


flag = True
debug = True
aircraft = []

all_aircraft = getSoup('https://www.advantage-aviation.com/rental-aircraft/')

if debug:
    #print(all_aircraft.prettify())
    print(all_aircraft.find_all('div', class_='aircraft'))
