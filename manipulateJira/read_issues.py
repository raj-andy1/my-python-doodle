import io
import re

with open('Controls Regrouping - Sheet6.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n")
        print(re.split("\s[A-Z]|[a-z]", item, maxsplit=1)[0], ',', item.split(',')[-1])

