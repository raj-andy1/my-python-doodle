#python script to request http page and get response code
import requests
import time
import datetime
import sys
import signal
import logging
import validators
import boto3
from urllib.parse import urlparse,urlsplit



try:
	url = sys.argv[1]
except IndexError:
	print ('Pls provide input url,Exiting!')
	exit(0)
#print (url)

'''try:
	log_path = sys.argv[2]
except IndexError:
	print ('Log path not provided using default location \'/var/log\'')
	log_path = '/var/log/'


logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger(__name__)
'''


def keyboardInterruptHandler(signal,frame):
	#log.debug('Received keyboard interrupt, Exiting')
	print('Exiting due to interrupt')
	exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

start_time = time.time()
print ('Program Start time for URL-' + url + '***' + time.strftime("%H:%M:%S", time.gmtime(start_time)))
#log.debug('Program Start time for URL-' + url + '***' + time.strftime("%H:%M:%S", time.gmtime(start_time)))
#print ('Log File: ' + log_path)
#log.debug ('Log File: ' + log_path)
#log.debug ('Is ' + url + ' valid?')
#log.debug (validators.url(url))

if validators.url(url):
	stacknm = urlparse(url).hostname
	stacknm = stacknm[:stacknm.find('.')]
	#print (stacknm)
	client = boto3.client('cloudformation')
	response = client.describe_stack_events(
		StackName = stacknm)
	stack_creation_time = response['StackEvents'][0]['Timestamp'] - response['StackEvents'][-1]['Timestamp']
	print (stack_creation_time)
	while True:
		try:
			r = requests.get(url)
		except requests.exceptions.RequestException as e:
			print('Connection Error' + '***' + time.strftime("%H:%M:%S", time.gmtime(time.time())))
			#print (e)
			#log.debug(e)
			time.sleep(10)
		else:
			#log.debug('Status code for provided URL:' + url + 'is: ' + str(r.status_code))
			print ('Status code for provided URL:' + url + ' is: ' + str(r.status_code))
			if (r.status_code == requests.codes.ok):
				print ('***Instance is up***')
				elapsed_time = time.time() - start_time
				print ('Total time for the instance to come up(hh:mm:ss):', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
				#log.debug('Program has ended time for URL-' + url + '***' + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
				exit()
else:
	print ('URL Validation Failed for: ' + url + '. Please check URL and try again')
	print (validators.url(url))
	#log.debug(validators.url(url))