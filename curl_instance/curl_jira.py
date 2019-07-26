#python script to request http page and get response code
import requests
import time
import datetime
import sys
import signal
import logging
import validators
import boto3
import botocore
from urllib.parse import urlparse

def keyboardInterruptHandler(signal,frame):
	#log.debug('Received keyboard interrupt, Exiting')
	print('Exiting due to interrupt')
	exit(0)

try:
	url = sys.argv[1]
except IndexError:
	print ('Pls provide input url,Exiting!')
	exit(0)
#print (url)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

if validators.url(url):
	'''for a valid URL using url parse determine the stackname from the URL, aws cfn stackname is of the form stackname.domainname
	so we need to split the domain'''
	stacknm = urlparse(url).hostname	
	stacknm = stacknm[:stacknm.find('.')] #find the first period and get the hostname before the first period
	#print (stacknm)
	client = boto3.client('cloudformation')
	while True:
		try:
			response = client.describe_stacks(
				StackName = stacknm)
			#print (response['Stacks'][0]['StackStatus'])
			if response['Stacks'][0]['StackStatus'] == 'CREATE_COMPLETE':
				response = client.describe_stack_events(
					StackName = stacknm)
				stack_creation_time = response['StackEvents'][0]['Timestamp'] - response['StackEvents'][-1]['Timestamp']
				print ('%s Stack has been created' % stacknm)
				print ('Time taken to create the stack is:', stack_creation_time)
				print ('Trying to connect to the service url:', url)
				try:
					r = requests.get(url)
					start_time = time.time()
				except requests.exceptions.RequestException as e:
					print('Connection Error' + '***' + time.strftime("%H:%M:%S", time.gmtime(time.time())))
					#print (e)
					time.sleep(10)
				else:
					print ('Status code for provided URL:' + url + ' is: ' + str(r.status_code))
					if (r.status_code == requests.codes.ok):
						print ('***Instance is up***')
						#elapsed_time = time.time() - start_time
						#print ('Total time for the instance to come up(hh:mm:ss):', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
						exit()
			elif response['Stacks'][0]['StackStatus'] == 'CREATE_FAILED' or response['Stacks'][0]['StackStatus'] == 'ROLLBACK_COMPLETE':
				print ('Error in stack creation,exiting...')
				exit()
		except botocore.exceptions.ClientError as e:
			print (e)
			exit()
		else:
			time.sleep(10)
else:
	print ('URL Validation Failed for: ' + url + '. Please check URL and try again')
	print (validators.url(url))









'''
	try:
			r = requests.get(url)
		except requests.exceptions.RequestException as e:
			print('Connection Error' + '***' + time.strftime("%H:%M:%S", time.gmtime(time.time())))
			#print (e)
			time.sleep(10)
		else:
			print ('Status code for provided URL:' + url + ' is: ' + str(r.status_code))
			if (r.status_code == requests.codes.ok):
				print ('***Instance is up***')
				elapsed_time = time.time() - start_time
				print ('Total time for the instance to come up(hh:mm:ss):', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
				exit()


'''