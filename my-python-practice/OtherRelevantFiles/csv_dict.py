vendor_name = set()

with open('/Users/arajagopalan/Downloads/vendor.txt', 'r', encoding='utf-8') as csvfile:
    lines=csvfile.readlines()
    for line in lines:
        line = line.rstrip("\n")
        separated = line.split("\t")
        vendor_name.add(separated[3])

print (sorted(vendor_name))