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
debug = False
all_ins = []

all_instructors = getSoup('https://www.advantage-aviation.com/instructor')

if debug:
    print(all_instructors.prettify())
    print(all_instructors.find_all('div', class_='instructor'))

instructors = all_instructors.find_all('div', class_='instructor')
for instructor_data in instructors:
    if debug: print(instructor_data, end="\n"*2)
    inst_detail_d = {}
    instructor_detail = instructor_data.find('div', class_='col-info')
    instructor_name = instructor_detail.find('h3').text
    instructor_contact = instructor_data.find('div', class_='cta')
    instructor_phone = instructor_contact.find_all('a')[0]['href'].split(':')[1]
    instructor_url_from_ww = instructor_contact.find_all('a')[1]['href']
    inst_detail_d['instructor_name'] = instructor_detail.find('h3').text
    inst_detail_d['instructor_phone'] = instructor_contact.find_all('a')[0]['href'].split(':')[1]
    inst_detail_d['email'] = cfDecodeEmail(instructor_contact.find_all('a')[2]['href'].split('#')[1])
    instructor_url = instructor_contact.find_all('a')[1]['href']
    if flag:
        print(f'getting instructor rate for {inst_detail_d["instructor_name"]}')
        instructor = getSoup(instructor_url)
        inst_detail_d['instructor_rate'] = instructor.find_all('p', class_='rate')[0].text
    all_ins.append(inst_detail_d)
    if debug:
        print(inst_detail_d)
        print(instructor_name)
        print(instructor_phone)
        print(instructor_url_from_ww)
        print(instructor_contact, end="\n" * 2)
        print(all_ins)
for ins in all_ins:
    print(ins, sep='\n')
