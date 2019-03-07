#sample python code to create multiple cloudformation stacks
import boto3
import random

stack_list = []
num_stack = 5

for num in range(1,(num_stack + 1)):
	stack_name = 'aws-j8-' + str(random.randrange(10,500,3)) + '-stack-' + str(num)
	stack_list.append(stack_name)

#print ('List of stacks to be created:',stack_list)

client = boto3.client('cloudformation')

for stack in stack_list:
	response = client.create_stack(
		StackName = stack,
		TemplateURL='https://s3.amazonaws.com/atl-andyr-cloudformation/qs/quickstart-jira-dc.template.yaml',
		Parameters= [
		{'ParameterKey':'JiraProduct','ParameterValue':'Software','UsePreviousValue':False},
		{'ParameterKey':'JiraVersion','ParameterValue':'8.0.0','UsePreviousValue':False},
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
		{'ParameterKey':'HostedZone','ParameterValue':'teamsin.space.','UsePreviousValue':False},
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
    	{'Key': 'service_name','Value': 'summit19 test'},
    	{'Key': 'business_unit','Value': 'FieldOps'},
    	],
    	ClientRequestToken=str(random.randrange(10,1000,3)),
    	EnableTerminationProtection=False
    	)
	if response['ResponseMetadata']['HTTPStatusCode'] == 200:
		print('Created Stack: %s' % stack)
	#print (response)
