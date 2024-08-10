from bs4 import BeautifulSoup

with open('report.html') as f:
    soup = BeautifulSoup(f, 'html.parser')


tr_tags_with_data_tt_id = soup.select('tr[data-tt-id]')

for tr in tr_tags_with_data_tt_id:
    print(tr)