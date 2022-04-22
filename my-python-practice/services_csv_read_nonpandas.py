# sample program to extract values from CSV file
import csv
count = 0
svcCnt = 0

fileName = '/Users/arajagopalan/Downloads/Copy of FedRAMP Central Supporting Services - discovered-micros-svcs.csv'

with open(fileName, 'r', encoding='utf-8') as csvfile:
    lines = csv.reader(csvfile)
    for line in lines:
        print(line[0])
        svcCnt += 1
        count += len(eval(line[1]))

print(count)
print("Service Count:", svcCnt)
