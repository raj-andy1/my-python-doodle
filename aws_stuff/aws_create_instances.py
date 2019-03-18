#python script to create n instances from ami 

import boto3
import random
import json

num_instances = 0
instance_list=[]
user_str = 'jsd'
domain_nm = '.og.summit19labs.com'
salt_flag = True #Flag set to add a random number to instance name string to counter for AWS instance delete time lag

for num in range(0,(num_instances+1)):
	if salt_flag: # if flag is present, add the salt to the instance name string
		salt = random.randrange(10,500,3)
		instance_name = user_str  + '-' + str(salt) +'-'
	else:
		instance_name = user_str + '-'
	instance_name = instance_name + str(num).zfill(3) + domain_nm
	instance_list.append(instance_name)

print('List of instances:', instance_list)

ec2 = boto3.resource('ec2',region_name='us-west-2')

while True:
	response = input('Press "P" to proceed or "C" to cancel:')
	if response == '' or response == 'C' or response == 'c':
		print ('Cancelling!!')
		break
	elif response == 'P' or response == 'p':
		print ('Creating Instances')
		for inst_nm in instance_list:
			instance = ec2.create_instances(
				DryRun=False,
				ImageId = 'ami-01e24be29428c15b2',
				MinCount =1,
				MaxCount = 1,
				InstanceType = 't2.small',
				KeyName = 'atl-master-us-west-2',
				NetworkInterfaces=[
				{
					'DeviceIndex':0,
					'AssociatePublicIpAddress':True,
					'DeleteOnTermination':True,
					'SubnetId':'subnet-0f463f0d9bb2d4b94',
					'Groups':['sg-0f9dc38a01de01cb9'],
				}],
				BlockDeviceMappings=[
				{ 
				'DeviceName':'/dev/xvda',
				'Ebs': {
					'DeleteOnTermination':True,
					'VolumeSize': 10,
					'VolumeType':'gp2',
					'Encrypted': False,
				},
				}],
				TagSpecifications=[
				{
				'ResourceType': 'instance',
				'Tags': [
				{
                    'Key': 'Name',
                    'Value': inst_nm,
                },]},],
				)
			#print (instance)
			print (instance[0].instance_id)
			inst = boto3.client('ec2',region_name='us-west-2')
			inst_desc = inst.describe_instances(
				InstanceIds=[instance[0].instance_id,],
				DryRun = False
				)
			print ('Instance Description***')
			#print (inst_desc)
			inst_pub_ip = inst_desc['Reservations'][0]['Instances'][0]['PublicIpAddress']
			print ('PublicIpAddress***')
			print (inst_pub_ip)
			dns = boto3.client('route53')
			rrupdate = dns.change_resource_record_sets(
			HostedZoneId='Z3MYWP3Y9LDS3A',
			ChangeBatch={
			'Changes': [
			{
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': inst_nm,
                    'Type': 'A',
                    'TTL': 300,
                    'ResourceRecords': [
                        {
                            'Value': inst_pub_ip
                        },
                    ],}},]})
			print ('R53 Update status')
			print (rrupdate)
			exit()

		
