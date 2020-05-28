#sample program to extract values from CSV file
vendor_name ={}

with open('/Users/arajagopalan/Downloads/vendor.txt', 'r', encoding='utf-8') as csvfile:
    lines=csvfile.readlines()
    for line in lines:
        line = line.rstrip("\n")
        separated = line.split("\t")
        plugin = separated[2]
        vn = separated[3]
        if vn not in vendor_name:
            vendor_name[vn]=set()
            vendor_name[vn].add(plugin)
        else:
            vendor_name[vn].add(plugin)

    for vn in vendor_name:
        plist = list(vendor_name[vn])
        pplist = ",".join(plist)
        print ("{}\t{}".format(vn,pplist))