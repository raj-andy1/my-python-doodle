#python script to request http page and get response code
import requests
import time
import sys
import signal


def keyboardInterruptHandler(signal,frame):
	print('Exiting due to interrupt')
	exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)

start_time = time.time()
print ('Start time:', time.strftime("%H:%M:%S", time.gmtime(start_time)))
url = sys.argv[1]
#print (url)

while True:
	try:
		r = requests.get(url)
	except requests.exceptions.RequestException as e:
		print ('Connection Error' + '***' + time.strftime("%H:%M:%S", time.gmtime(time.time())))
		time.sleep(10)
	else:
		#print (r.status_code)
		if (r.status_code == requests.codes.ok):
			print ('***Jira is up***')
			elapsed_time = time.time() - start_time
			print ('Total time to provision (hh:mm:ss):', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
			exit()