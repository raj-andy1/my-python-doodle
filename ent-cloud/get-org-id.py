#python script to extract org id from list
import requests
import json

'''api_output is the dump from this link https://admin.atlassian.com/gateway/api/adminhub/organization/my2
the resulatant dataset needs to be massaged to change null object to 'null' (with quotes) so it can be manipulated pythonically'''

api_output = {"id":"d37bdb91-ca25-44c5-bc1b-be7df7faed9e","name":"cm-user-44","sites":[{"id":"c20b6d4a-587e-4698-9a71-b4e318b71319","siteUrl":"null","orgId":"null","siteAdmin":"null","displayName":"null","avatar":"null","products":"null"}],"domains":{"total":0,"verified":0},"memberTotal":0},{"id":"dffc378b-25b1-4560-846e-1d3d1f406585","name":"cm-user-24","sites":[{"id":"2342275d-7af9-4fc6-951e-102d67d48396","siteUrl":"null","orgId":"null","siteAdmin":"null","displayName":"null","avatar":"null","products":"null"}],"domains":{"total":0,"verified":0},"memberTotal":0},{"id":"e53656e3-be70-49cb-9a17-9fa6f6dd15d7","name":"cm-user-5","sites":[{"id":"ec964f5e-5ce4-453c-b4a7-e32ab1508260","siteUrl":"null","orgId":"null","siteAdmin":"null","displayName":"null","avatar":"null","products":"null"}],"domains":{"total":0,"verified":0},"memberTotal":0},{"id":"f45ad01d-8846-4a0a-a25e-0c5887d5ea48","name":"cm-user-29","sites":[{"id":"74162f92-186f-430c-8b9e-ead834bb7ff4","siteUrl":"null","orgId":"null","siteAdmin":"null","displayName":"null","avatar":"null","products":"null"}],"domains":{"total":0,"verified":0},"memberTotal":0},{"id":"f33eabfa-65f4-4a2f-bcf4-626a989f60b2","name":"cm-user-38","sites":[{"id":"a19aab31-1b36-402d-9714-74efe7713226","siteUrl":"null","orgId":"null","siteAdmin":"null","displayName":"null","avatar":"null","products":"null"}],"domains":{"total":0,"verified":0},"memberTotal":0},{"id":"fa4e1132-e035-4e9d-8262-c4c682ab4c6b","name":"cm-user-23","sites":[{"id":"d2148940-f7e3-493e-82ec-0b3992d8742d","siteUrl":"null","orgId":"null","siteAdmin":"null","displayName":"null","avatar":"null","products":"null"}],"domains":{"total":0,"verified":0},"memberTotal":0}
org_d = {}

for n in range(0,len(api_output)):
	key = api_output[n]['name']
	#print (key)
	org_d[key] = []
	org_d[key] = api_output[n]['id']

print (sorted(org_d))
print (len(org_d))

'''for item in org_d.values():
	print (item)
'''
 

headers = {'Content-Type': 'application/json', 'cookie': 'cloud.session.token=eyJraWQiOiJzZXNzaW9uLXNlcnZpY2VcL3Nlc3Npb24tc2VydmljZSIsImFsZyI6IlJTMjU2In0.eyJhc3NvY2lhdGlvbnMiOltdLCJzdWIiOiI1YmViNmYzNjNiNWI0YjExNmE5ZWY0ZmYiLCJlbWFpbERvbWFpbiI6ImF0bGFzc2lhbi5jb20iLCJpbXBlcnNvbmF0aW9uIjpbXSwicmVmcmVzaFRpbWVvdXQiOjE1NjU2NDUyNDgsImlzcyI6InNlc3Npb24tc2VydmljZSIsInNlc3Npb25JZCI6ImM5MjZmYzdiLThkZDEtNDAwNy1hNGRlLTA2YWMzYzRhMjI1MiIsImF1ZCI6ImF0bGFzc2lhbiIsIm5iZiI6MTU2NTY0NDY0OCwiZXhwIjoxNTY4MjM2NjQ4LCJpYXQiOjE1NjU2NDQ2NDgsImVtYWlsIjoiYXJhamFnb3BhbGFuQGF0bGFzc2lhbi5jb20iLCJqdGkiOiJjOTI2ZmM3Yi04ZGQxLTQwMDctYTRkZS0wNmFjM2M0YTIyNTIifQ.Nk9IGlTl8d92F-gsFTPZsgDqFmtrrdhsszhrkOdV1zQbdcRbxi9uaFde59sXiBI55UpVBw45FOW8M41lAtFFn_JHpgs7Tf0I-a_LM0okcGLvLbc42WohMfBoqmDlH-leWgR1tLaJ6Bc74GjMtQ_VRQcpGuftodHCTnUyzoaD_UFb0Go4SJ0Ijge1z5loav2R1rQ-hNap9c6qlmKbpFdNYTLao_gk1KczZuzgkXZrYQv9DKV99e08JqrKYxfYeoVXzJacThhUdszvGybNc5sgj6rtnOTyrh6q8f5dC-lwn4UddWucfL_btsGSHAKlTtY9hyFgi0U03ikBn_HPLIynwg'}
for k,v in sorted(org_d.items()):
	payload = {'primaryOrgId': '01aaecd7-8e29-4f54-919d-b74b4954f4cf', 'secondaryOrgId': v}
	#print (payload)
	print ('Move parent organization for: %s' % k) 
	while True:
		response = response = input('Press "P" to proceed or "C" to cancel:')
		if response == '' or response == 'C' or response == 'c':
			print ('Cancelling!!')
			break
		elif response == 'P' or response == 'p':
			try:
				r = requests.post('https://admin.atlassian.com/gateway/api/adminhub/organization/reparent', data=json.dumps(payload), headers=headers)
				print (r)
			except Exception as e:
				print (e)


