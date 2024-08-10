import json

with open ('mappings.json', 'r') as f:
    data = json.load(f)

inst_list = ["i-0fbcf282b3b9b8683",
"i-01d201085571bb3b6",
"i-0a3e2dd99a9911279",
"i-01f574488344c65aa",
"i-074dea94b770a4220",
"i-0fb7b846026614b77",
"i-091c9053bc1f6866d",
"i-05405ca77b1df9c34",
"i-0d99bf0b5ad3952cc",
"i-0cd905c7e4137f8c1",
"i-04b1102156ac8f81d",
"i-0c9c635b1bb376c35",
"i-06da368109bb8fd69",
"i-0274ff52e296a3257",
"i-085c563f56e8648c8",
"i-06aa46fcbdeec9496",
"i-0e5b93c5a7cbfd8bd"]
count = 0
inst_found = set()

#print(data)
for item in data:
    if data[item]['arn'].split('/')[1] in inst_list:
        inst_found.add(data[item]['arn'].split('/')[1])
        print(data[item]['service'], data[item]['resourceOwner'])
        count += 1

print(count)
print(len(inst_list))
#print(inst_found)
print(set(inst_list) - inst_found)
