#sample python code to create multiple cloudformation stacks
import boto3
import random

stack_list = []
num_stack = 1
user_str = 'j8'
salt_flag = True

#boto params
region_nm = 'us-west-2'

#CF params
domain_nm = 'j8.summit19labs.com.'
s3_url = 'https://s3-us-west-2.amazonaws.com/summit19-labs/j8/templates/j8-jira-dc.yaml'
j_ver = '8.0.2'
j_prod = 'All'

for num in range(0,(num_stack+1)):
	if salt_flag: # if flag is present, add the salt to the instance name string
		salt = random.randrange(10,500,3)
		instance_name = user_str  + '-' + str(salt) + '-'
	else:
		instance_name = user_str + '-'
	instance_name = instance_name + str(num).zfill(3)
	stack_list.append(instance_name)

print ('List of stacks to be created:',stack_list)


client = boto3.client('cloudformation',region_name=region_nm)

while True:
	response = input('Press "P" to proceed or "C" to cancel:')
	if response == '' or response == 'C' or response == 'c':
		print ('Cancelling!!')
		break
	elif response == 'P' or response == 'p':
		print ('Creating Instances')
		for stack in stack_list:
			response = client.create_stack(
				StackName = stack,
				TemplateURL=s3_url,
				Parameters= [
				{'ParameterKey':'JiraProduct','ParameterValue':j_prod,'UsePreviousValue':False},
				{'ParameterKey':'JiraVersion','ParameterValue':j_ver,'UsePreviousValue':False},
				{'ParameterKey':'DeployEnvironment','ParameterValue':'prod','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeInstanceType','ParameterValue':'t3.medium','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeMax','ParameterValue':'1','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeMin','ParameterValue':'1','UsePreviousValue':False},
				{'ParameterKey':'ClusterNodeVolumeSize','ParameterValue':'50','UsePreviousValue':False},
				{'ParameterKey':'DBInstanceClass','ParameterValue':'db.t2.medium','UsePreviousValue':False},
				{'ParameterKey':'DBIops','ParameterValue':'1000','UsePreviousValue':False},
				{'ParameterKey':'DBMasterUserPassword','ParameterValue':'Charlie101','UsePreviousValue':False},
				{'ParameterKey':'DBMultiAZ','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'DBPassword','ParameterValue':'Charlie101','UsePreviousValue':False},
				{'ParameterKey':'DBStorage','ParameterValue':'200','UsePreviousValue':False},
				{'ParameterKey':'DBStorageEncrypted','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'DBStorageType','ParameterValue':'General Purpose (SSD)','UsePreviousValue':False},
				{'ParameterKey':'AssociatePublicIpAddress','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'CidrBlock','ParameterValue':'0.0.0.0/0','UsePreviousValue':False},
				{'ParameterKey':'KeyPairName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'SSLCertificateARN','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'CustomDnsName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'HostedZone','ParameterValue':domain_nm,'UsePreviousValue':False},
				{'ParameterKey':'JiraDownloadUrl','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'LocalAnsibleGitRepo','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'LocalAnsibleGitSshKeyName','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'StartCollectd','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'TomcatContextPath','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'CatalinaOpts','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'JvmHeapOverride','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'DBPoolMaxSize','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBPoolMinSize','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBMaxIdle','ParameterValue':'20','UsePreviousValue':False},
				{'ParameterKey':'DBMaxWaitMillis','ParameterValue':'10000','UsePreviousValue':False},
				{'ParameterKey':'DBMinEvictableIdleTimeMillis','ParameterValue':'18000','UsePreviousValue':False},
				{'ParameterKey':'DBMinIdle','ParameterValue':'','UsePreviousValue':False},
				{'ParameterKey':'DBRemoveAbandoned','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'DBRemoveAbandonedTimeout','ParameterValue':'60','UsePreviousValue':False},
				{'ParameterKey':'DBTestOnBorrow','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'DBTestWhileIdle','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'DBTimeBetweenEvictionRunsMillis','ParameterValue':'60000','UsePreviousValue':False},
				{'ParameterKey':'MailEnabled','ParameterValue':'true','UsePreviousValue':False},
				{'ParameterKey':'TomcatAcceptCount','ParameterValue':'10','UsePreviousValue':False},
				{'ParameterKey':'TomcatConnectionTimeout','ParameterValue':'20000','UsePreviousValue':False},
				{'ParameterKey':'TomcatDefaultConnectorPort','ParameterValue':'8080','UsePreviousValue':False},
				{'ParameterKey':'TomcatEnableLookups','ParameterValue':'false','UsePreviousValue':False},
				{'ParameterKey':'TomcatMaxThreads','ParameterValue':'200','UsePreviousValue':False},
				{'ParameterKey':'TomcatMinSpareThreads','ParameterValue':'10','UsePreviousValue':False},
				{'ParameterKey':'TomcatProtocol','ParameterValue':'HTTP/1.1','UsePreviousValue':False},
				{'ParameterKey':'TomcatRedirectPort','ParameterValue':'8443','UsePreviousValue':False},
				{'ParameterKey':'TomcatScheme','ParameterValue':'http','UsePreviousValue':False},
				],
    			OnFailure='ROLLBACK',
    		 	Capabilities=['CAPABILITY_IAM',],
    			Tags=[
    			{'Key': 'resource_owner','Value': 'csa_team'},
    			{'Key': 'Purpose','Value': 'j8_lab'},
    			{'Key': 'business_unit','Value': 'FieldOps'},
    			{'Key':'Name','Value':stack},
    			],
    			ClientRequestToken=str(random.randrange(10,1000,3)),
    			EnableTerminationProtection=False,
    			)
			if response['ResponseMetadata']['HTTPStatusCode'] == 200:
				print('Created Stack: %s' % stack)
	#print (response)'''
		exit()