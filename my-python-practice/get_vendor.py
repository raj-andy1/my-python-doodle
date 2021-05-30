plugins = {}
dccompat=set()
vn_bb = set()
vn_not_bb = set()
data = []

with open('/Users/arajagopalan/Downloads/CATSD-1292.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        dc_compat = item[2]
        vendor_name = item[5]
        in_bb = item[3]
        if item[2] == "Compatible":
            if item[3] == 'In Bug Bounty':
                vn_bb.add(item[5])
            elif item[3] == 'Not in Bug Bounty':
                vn_not_bb.add(item[5])

print(vn_bb)
print(len(vn_bb))
print(vn_not_bb)
print(len(vn_not_bb))

"""
        if item[2] == "Compatible":
            vn.add(vendor_name)
print(vn)
print(len(vn))

"""
