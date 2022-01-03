import requests
from bs4 import BeautifulSoup

URL = 'https://www.advantage-aviation.com/instructor/yaron-ekshtein/'

page = requests.get(URL)
# print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')
instructor = soup.find(id='main')

#print(instructor.prettify())

items = instructor.find_all('p', class_='rate')[0].text
print(items)

URL = 'https://www.advantage-aviation.com/instructor'

page = requests.get(URL)
# print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')
all_instructors = soup.find(id='main')