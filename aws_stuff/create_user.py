#sample python code to create a list of users on AWS using Boto3

import boto3
import random

num_users = 3
user_list = []
salt = salt = random.randrange(5,100,5)
passwd='Summit19Jira8DCDLab!'


for num in range(1,(num_users+1)):
	user_name = 'j8-dcd-'+str(salt) + '-user-' + str(num)
	user_list.append(user_name)

print ('List of users is ', user_list)


iam = boto3.client('iam')

for user_nm in user_list:
	iam.create_user(UserName=user_nm)
	iam.add_user_to_group(GroupName='j8-dcd-group',UserName=user_nm)
	iam.create_login_profile(UserName=user_nm,Password=passwd,PasswordResetRequired=False)



