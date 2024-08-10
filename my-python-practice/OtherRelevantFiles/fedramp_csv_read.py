services_for_fedramp = []
services_classification = []

with open('/Users/arajagopalan/Downloads/fedRAMP Questionnaire - Services-level Questions.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        service_id = item[0]
        services_for_fedramp.append(service_id)


with open('/Users/arajagopalan/Downloads/service-dep-classifications.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        service_id = item[0]
        services_classification.append(service_id)

services_for_fedramp.pop(0)
services_classification.remove('source')
print(set(services_for_fedramp))
print(len(set(services_for_fedramp)))
print(set(services_classification))
print(len(set(services_classification)))
print(set(services_for_fedramp).intersection(set(services_classification)))
print(type(set(services_for_fedramp).intersection(set(services_classification))))
print(set(services_for_fedramp).difference(set(services_classification)))
print(len(set(services_for_fedramp).difference(set(services_classification))))

