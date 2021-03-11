# sample program to extract values from CSV file
plugins = {}
data = []

with open('/Users/arajagopalan/Downloads/new_vendorList.txt', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        plugin_name = item[0]
        vendor_name = item[14]
        if vendor_name not in plugins:
            plugins[vendor_name] = set()
            plugins[vendor_name].add(plugin_name)
        else:
            plugins[vendor_name].add(plugin_name)
    print(plugins)
    print(len(plugins))
    count = 0
    for k, v in plugins.items():
        count += len(v)
    print(count)

