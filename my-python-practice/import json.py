import json
import requests

vendor_nm = {'Botron Software': ['1210910'], '//SEIBERT/MEDIA - AppAnvil': ['1217680']}

vendor_new_dict = {}
app_new_dict ={}
no_dc_apps_list = []

def mplace_url_request():
    

for k,v in vendor_nm.items():
    vendor_name = k
    print ('Vendor Name:' ,vendor_name)
    vendor_id = v[0]
    base_url = 'https://marketplace.atlassian.com/rest/2/addons/vendor/'
    url = ''.join([base_url,vendor_id])
    url = '?'.join([url,'hosting=datacenter'])
    #print (url)
    r = requests.get(url)
    r_json = json.loads(r.text)
    #print (r_json)