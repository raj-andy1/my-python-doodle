#python script to create cloud

import requests
import json
from random import randint
from time import sleep

hdrs = {'ATL-Xsrf-Token':'cfca92f2762839a153d099d99d8aa2b3a7f215e686ee25ecac27f40bc90d10c2'}
cks = {'cloud.session.token':'eyJraWQiOiJzZXNzaW9uLXNlcnZpY2VcL3Byb2QtMTU5Mjg1ODM5NCIsImFsZyI6IlJTMjU2In0.eyJhc3NvY2lhdGlvbnMiOlt7ImFhSWQiOiI1ZTY4Mzg5NDg0ZGNmYzBjZjM5MTM2YjMiLCJzZXNzaW9uSWQiOiJjNTZjZWI2Ny04Mjk2LTQ5NjAtOTk4Yi00ZTkxODAzMjc1ZWUiLCJlbWFpbCI6ImVwYXJpc0B1c2VyLTAwNy5jaGFybGllb2lsLmNvbSJ9LHsiYWFJZCI6IjVmM2M5ZDk5ZTExNTQyMDA0NjdmYTNkNyIsInNlc3Npb25JZCI6IjdmZDM2Y2FlLWZmOTQtNGZlOS1hNTMwLWFlYTc3MzgxZmU2MyIsImVtYWlsIjoiZXBhcmlzQHVzZXItMDIyLmNoYXJsaWVvaWwuY29tIn1dLCJzdWIiOiI1YmViNmYzNjNiNWI0YjExNmE5ZWY0ZmYiLCJlbWFpbERvbWFpbiI6ImF0bGFzc2lhbi5jb20iLCJpbXBlcnNvbmF0aW9uIjpbXSwiY3JlYXRlZCI6MTU5NDg1NjExOCwicmVmcmVzaFRpbWVvdXQiOjE1OTg0OTg0MTcsInZlcmlmaWVkIjp0cnVlLCJpc3MiOiJzZXNzaW9uLXNlcnZpY2UiLCJzZXNzaW9uSWQiOiJjNTY1NDRhMS0yMTY3LTQ5ZjMtOGE1Zi1jNWFiMTc2MjVjZGMiLCJhdWQiOiJhdGxhc3NpYW4iLCJuYmYiOjE1OTg0OTc4MTcsImV4cCI6MTYwMTA4OTgxNywiaWF0IjoxNTk4NDk3ODE3LCJlbWFpbCI6ImFyYWphZ29wYWxhbkBhdGxhc3NpYW4uY29tIiwianRpIjoiYzU2NTQ0YTEtMjE2Ny00OWYzLThhNWYtYzVhYjE3NjI1Y2RjIn0.yIQ2EGSH8jRGVQtnAnF1Llx-olzDpi2kQblS14NgMNhCA62Uxws3bmqymZFPZ-qfCPCOWplvjCFwgnvxuK96Hv28Kb9BurgK0D4wnDXk_Nb0ADwfrFU3g8YTDtgIiD1Jwymc3L22x4uXh94iK1uWOmZ_pcWTEJD_a93BUfNmpI4yCT-NM5Mxb0jRqUVbnmIl4jMUjoYelSbASHl9DEyHPEFnWZG3W-2Dq7vPPX0mWU_UOB5iZR0Jv-r2qV8mH9N8gI_JXnzjXvgZPhmH99h-iwGGUFy_SXfQb67qFmMPkGrZy98fGzHT0NgYmqlLvvF9sfwrLIvC1ji3JvDWJuebow'}

url = 'https://cofs.prod.public.atl-paas.net/' + 'cloud'

un_prov_cloud = []

'''
cloudInst = [{"cloudName": "user-001-charlieoil", "country": "US", "state": "CA", "email": "admin@user-001.charlieoil.com", "firstName": "Admin", "lastName": "Istrator", "products": [{ "product": "jira-software.ondemand"},
{ "product": "confluence.ondemand", "edition": "premium"}], "timezone": "US/LosAngeles", "languagePreference": "en-US" }, {"cloudName": "user-002-charlieoil", "country": "US", "state": "CA", "email": "admin@user-002.charlieoil.com", "firstName": "Admin", "lastName": "Istrator", "products": [{ "product": "jira-software.ondemand"},
{ "product": "confluence.ondemand", "edition": "premium"}], "timezone": "US/LosAngeles", "languagePreference": "en-US" },{"cloudName": "user-003-charlieoil", "country": "US", "state": "CA", "email": "admin@user-003.charlieoil.com", "firstName": "Admin", "lastName": "Istrator", "products": [{ "product": "jira-software.ondemand"},
{ "product": "confluence.ondemand", "edition": "premium"}], "timezone": "US/LosAngeles", "languagePreference": "en-US" } ]
'''

cloudInst = [{
	"cloudName": "user-002-charlieoil",
	"country": "US",
	"state": "CA",
	"email": "admin@user-002.charlieoil.com",
	"firstName": "Admin",
	"lastName": "Istrator",
	"products": [{
		"product": "jira-software.ondemand",
		"edition": "premium"
	}]
}]


for cloud in cloudInst:
	#sleep (rand)
	try:
		r = requests.post(url,json=cloud,headers=hdrs,cookies=cks)
		print (r.text)



'''
			if r.text == 'Rate limit exceeded':
			un_prov_cloud.append(cloud['cloudName'])
'''



