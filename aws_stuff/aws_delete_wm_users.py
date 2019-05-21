#sample python code to delete a list of workmail users on AWS using Boto3

import boto3
import random

'''
num_users = 100 #provide the number of users
user_list = []
group_n = ''
group_nm = '' #provide name of the group
salt_flag = False # Flag to set a random salt number to be added to the user name string to counter for aws delete user time lags


for num in range(1,(num_users+1)):
	if salt_flag: # if flag is present, add the salt to the username string, else do not add
		salt = random.randrange(10,500,3)
		user_name = group_nm  + '-' + str(salt) + '-user-'
	else:
		user_name = group_nm +'user-'
	user_name = user_name + str(num).zfill(3)
	user_list.append(user_name)

print ('List of users to be deleted is ', user_list)
'''
user_list = ['user-001', 'user-002', 'user-003']
user_id_list = []
user_id = {}
#user_list = ['user-001', 'user-002', 'user-003', 'user-004', 'user-005', 'user-006', 'user-007', 'user-008', 'user-009', 'user-010', 'user-011', 'user-012', 'user-013', 'user-014', 'user-015', 'user-016', 'user-017', 'user-018', 'user-019', 'user-020', 'user-021', 'user-022', 'user-023', 'user-024', 'user-025', 'user-026', 'user-027', 'user-028', 'user-029', 'user-030', 'user-031', 'user-032', 'user-033', 'user-034', 'user-035', 'user-036', 'user-037', 'user-038', 'user-039', 'user-040', 'user-041', 'user-042', 'user-043', 'user-044', 'user-045', 'user-046', 'user-047', 'user-048', 'user-049', 'user-050', 'user-051', 'user-052']
org_id = 'm-a613fdca685e4efdb6e748d916992864'

client = boto3.client('workmail')


response = client.list_users(
	OrganizationId = org_id,
	NextToken = 'H4sIAAAAAAAAAHVSPW8TQRAdOwSICeQDQQcoiNZ7seOcbaUAUkRYHDjChBKxezd3ubC3a/b2nEsKJIQEBaKDngIhJNLSE8EfoKVC6ampkJizE5IUbLG72pn35s2b3fkF46mBqq8TxhO+rRXfTFkUGx6GyHwZo7IpCwLBVnkUq+i+fozqtfjy/NPuh70ylD2YwdyXWRoPsGe5sbdxy8KcR3xOpHUk0aFropUjeIpOt29jKiGXPKgkPL+HaSZt+gSeQinvk47LhY4Rjo1wrMCxVYMpKYH9VYaSBxMGQzSofLQw623wAXckV5HTFRvo26XcwJX/sB2oOKSDYfWZgoRlNpbsFk/X7/D++Kkfu18vPvo+BuUVqEjNgxXuW206MGHXSdO6lkHev35jSDO5eZr26YLQwjltIq7ibV6U6gTE7h73OEUziH0kc7cUT3QgBnVGB0p201oTi8ziAy4zfPjx85+5NfGtDBUPSsLChVGvKtbO8pbF5YwmZcjQE6Lb9SycP2LFstYSuaJgWfQsTI9CRYOOF6eW3kuyMP8sXRILU0fi1HwRVse97ZEyFRV8qrcPnFBrnjdUWjxMEmY4zynKSUc5ef9gWbiaVLlbWwgDn7utRWxgGAgXm41W0K657Xa95TYo62RG7pBpBbxyCL7WDJrIF8P5qhsKt9qo09Za8GvVhdZ83Q25vygaYT8fwsb+zbMQzjrKYoRmdu/d+9/PXrboA3VgfFCopn8yfZh3N0sEmhc7by+defPz1fBj0DyDv1/JixQnAwAA',
	)


print (response['NextToken'])
#print (len(response['Users']))


for n in range(0,100):
		user_id[response['Users'][n]['Name']].append(response['Users'][n]['State'])
		user_id_list.append(response['Users'][n]['Id'])

#print (user_id)
#print (user_id_list)
#print (len(user_id_list))
'''
for user in user_id_list:
	response = client.deregister_from_work_mail(
		OrganizationId = org_id,
		EntityId = user
		)
	print (response)
	response = client.delete_user(
		OrganizationId = org_id,
		UserId = user
		)
	print (response)
'''


