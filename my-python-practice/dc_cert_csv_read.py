# sample program to extract values from CSV file
import io
dc_certified = []
data = []
all_status = set()
dc_status = {'Withdrawn', 'Rejected', 'Approved', 'REMOVED', 'status',
          'Waiting for Atlassian', 'On hold', 'PENDING MARKETPLACE REMOVAL',
          'AR WAITING FOR VENDOR', 'New', 'AR WAITING FOR ATLASSIAN',
          'AR READY FOR REVIEW', 'Under review', 'Waiting for vendor', 'AR UNDER REVIEW'}
dc_cert = {'Withdrawn', 'Rejected', 'REMOVED',
          'PENDING MARKETPLACE REMOVAL'}



with open('/Users/arajagopalan/Downloads/dc_cert.txt', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        status = item[4]
        if status not in dc_cert:
            dc_certified.append(item)
    with open('dc_cert_apps.txt', 'w') as new_file:
        for app in dc_certified:
            new_file.write(str(app))
            new_file.write('\n')

print(len(dc_certified))

certified_apps = {}
for app in dc_certified:
    status = app[4]
    appkey = app[3]
    if status not in certified_apps:
        certified_apps[status] = set()
        certified_apps[status].add(appkey)
    else:
        certified_apps[status].add(appkey)

print(certified_apps)
with open('dc_certified_apps.txt', 'w') as file:
    for k, v in certified_apps.items():
        for value in v:
            file.write("{}\t{}".format(k,value))
            file.write('\n')
        print(f'{k} - {len(v)}')




