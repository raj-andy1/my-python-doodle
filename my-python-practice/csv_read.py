# sample program to extract values from CSV file
import io
plugins = {}
data = []

with open('/Users/arajagopalan/Downloads/Customer_Analytics_ADHOC_All_Apps_List_2021_03_11.csv', 'r', encoding='utf-8') as csvfile:
    lines = csvfile.readlines()
    for line in lines:
        item = line.rstrip("\n").split(',')
        plugin_key = item[10]
        vendor_name = item[14]
        if vendor_name not in plugins:
            plugins[vendor_name] = set()
            plugins[vendor_name].add(plugin_key)
        else:
            plugins[vendor_name].add(plugin_key)
    print(plugins)
    print(len(plugins))
    count = 0
    with open('dcapps2.csv', 'w') as file:
        for k, v in plugins.items():
            count += len(v)
            file.write("{}\t{}".format(k,v))
            file.write('\n')
    print(count)

