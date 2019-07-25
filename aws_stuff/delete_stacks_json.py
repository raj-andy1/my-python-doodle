#delete cfn stacks
#python code to delete cfn stacks from json output

import boto3
import botocore
import json

stack_list_file = '/Users/arajagopalan/cf_stack_list.json'

stack_list = []

with open(stack_list_file,'r') as f:
	doc = json.load(f)

#print(doc['Stacks'][0]['StackName'])

for d in range(0,len(doc['Stacks'])):
	stack_list.append(doc['Stacks'][d]['StackName'])

#print (stack_list)

client = boto3.client('cloudformation',region_name='us-west-2')

for stack in stack_list:
	response = client.delete_stack(
		StackName = stack,
		)
	print ('Deleting stack with name %s' % stack)
	print (response)