#sample code to test out the instances

import boto3
import requests
import validators
import signal
import sys

#og_url_list = ['jsd-000.og.summit19labs.com', 'jsd-001.og.summit19labs.com', 'jsd-002.og.summit19labs.com', 'jsd-003.og.summit19labs.com', 'jsd-004.og.summit19labs.com', 'jsd-005.og.summit19labs.com', 'jsd-006.og.summit19labs.com', 'jsd-007.og.summit19labs.com', 'jsd-008.og.summit19labs.com', 'jsd-009.og.summit19labs.com', 'jsd-010.og.summit19labs.com', 'jsd-011.og.summit19labs.com', 'jsd-012.og.summit19labs.com', 'jsd-013.og.summit19labs.com', 'jsd-014.og.summit19labs.com', 'jsd-015.og.summit19labs.com', 'jsd-016.og.summit19labs.com', 'jsd-017.og.summit19labs.com', 'jsd-018.og.summit19labs.com', 'jsd-019.og.summit19labs.com', 'jsd-020.og.summit19labs.com', 'jsd-021.og.summit19labs.com', 'jsd-022.og.summit19labs.com', 'jsd-023.og.summit19labs.com', 'jsd-024.og.summit19labs.com', 'jsd-025.og.summit19labs.com', 'jsd-026.og.summit19labs.com', 'jsd-027.og.summit19labs.com', 'jsd-028.og.summit19labs.com', 'jsd-029.og.summit19labs.com', 'jsd-030.og.summit19labs.com', 'jsd-031.og.summit19labs.com', 'jsd-032.og.summit19labs.com', 'jsd-033.og.summit19labs.com', 'jsd-034.og.summit19labs.com', 'jsd-035.og.summit19labs.com', 'jsd-036.og.summit19labs.com', 'jsd-037.og.summit19labs.com', 'jsd-038.og.summit19labs.com', 'jsd-039.og.summit19labs.com', 'jsd-040.og.summit19labs.com', 'jsd-041.og.summit19labs.com', 'jsd-042.og.summit19labs.com', 'jsd-043.og.summit19labs.com', 'jsd-044.og.summit19labs.com', 'jsd-045.og.summit19labs.com', 'jsd-046.og.summit19labs.com', 'jsd-047.og.summit19labs.com', 'jsd-048.og.summit19labs.com', 'jsd-049.og.summit19labs.com', 'jsd-050.og.summit19labs.com', 'jsd-051.og.summit19labs.com', 'jsd-052.og.summit19labs.com', 'jsd-053.og.summit19labs.com', 'jsd-054.og.summit19labs.com', 'jsd-055.og.summit19labs.com', 'jsd-056.og.summit19labs.com', 'jsd-057.og.summit19labs.com', 'jsd-058.og.summit19labs.com', 'jsd-059.og.summit19labs.com', 'jsd-060.og.summit19labs.com', 'jsd-061.og.summit19labs.com', 'jsd-062.og.summit19labs.com', 'jsd-063.og.summit19labs.com', 'jsd-064.og.summit19labs.com', 'jsd-065.og.summit19labs.com', 'jsd-066.og.summit19labs.com', 'jsd-067.og.summit19labs.com', 'jsd-068.og.summit19labs.com', 'jsd-069.og.summit19labs.com', 'jsd-070.og.summit19labs.com', 'jsd-071.og.summit19labs.com', 'jsd-072.og.summit19labs.com', 'jsd-073.og.summit19labs.com', 'jsd-074.og.summit19labs.com', 'jsd-075.og.summit19labs.com', 'jsd-076.og.summit19labs.com', 'jsd-077.og.summit19labs.com', 'jsd-078.og.summit19labs.com', 'jsd-079.og.summit19labs.com', 'jsd-080.og.summit19labs.com', 'jsd-081.og.summit19labs.com', 'jsd-082.og.summit19labs.com', 'jsd-083.og.summit19labs.com', 'jsd-084.og.summit19labs.com', 'jsd-085.og.summit19labs.com', 'jsd-086.og.summit19labs.com', 'jsd-087.og.summit19labs.com', 'jsd-088.og.summit19labs.com', 'jsd-089.og.summit19labs.com', 'jsd-090.og.summit19labs.com', 'jsd-091.og.summit19labs.com', 'jsd-092.og.summit19labs.com', 'jsd-093.og.summit19labs.com', 'jsd-094.og.summit19labs.com', 'jsd-095.og.summit19labs.com', 'jsd-096.og.summit19labs.com', 'jsd-097.og.summit19labs.com', 'jsd-098.og.summit19labs.com', 'jsd-099.og.summit19labs.com', 'jsd-100.og.summit19labs.com', 'jsd-101.og.summit19labs.com', 'jsd-102.og.summit19labs.com', 'jsd-103.og.summit19labs.com', 'jsd-104.og.summit19labs.com', 'jsd-105.og.summit19labs.com', 'jsd-106.og.summit19labs.com', 'jsd-107.og.summit19labs.com', 'jsd-108.og.summit19labs.com', 'jsd-109.og.summit19labs.com', 'jsd-110.og.summit19labs.com', 'jsd-111.og.summit19labs.com', 'jsd-112.og.summit19labs.com', 'jsd-113.og.summit19labs.com', 'jsd-114.og.summit19labs.com', 'jsd-115.og.summit19labs.com', 'jsd-116.og.summit19labs.com', 'jsd-117.og.summit19labs.com', 'jsd-118.og.summit19labs.com', 'jsd-119.og.summit19labs.com', 'jsd-120.og.summit19labs.com', 'jsd-121.og.summit19labs.com', 'jsd-122.og.summit19labs.com', 'jsd-123.og.summit19labs.com', 'jsd-124.og.summit19labs.com', 'jsd-125.og.summit19labs.com', 'jsd-126.og.summit19labs.com', 'jsd-127.og.summit19labs.com', 'jsd-128.og.summit19labs.com', 'jsd-129.og.summit19labs.com', 'jsd-130.og.summit19labs.com', 'jsd-131.og.summit19labs.com', 'jsd-132.og.summit19labs.com', 'jsd-133.og.summit19labs.com', 'jsd-134.og.summit19labs.com', 'jsd-135.og.summit19labs.com', 'jsd-136.og.summit19labs.com', 'jsd-137.og.summit19labs.com', 'jsd-138.og.summit19labs.com', 'jsd-139.og.summit19labs.com', 'jsd-140.og.summit19labs.com', 'jsd-141.og.summit19labs.com', 'jsd-142.og.summit19labs.com', 'jsd-143.og.summit19labs.com', 'jsd-144.og.summit19labs.com', 'jsd-145.og.summit19labs.com', 'jsd-146.og.summit19labs.com', 'jsd-147.og.summit19labs.com', 'jsd-148.og.summit19labs.com', 'jsd-149.og.summit19labs.com', 'jsd-150.og.summit19labs.com', 'jsd-151.og.summit19labs.com', 'jsd-152.og.summit19labs.com', 'jsd-153.og.summit19labs.com', 'jsd-154.og.summit19labs.com', 'jsd-155.og.summit19labs.com', 'jsd-156.og.summit19labs.com', 'jsd-157.og.summit19labs.com', 'jsd-158.og.summit19labs.com', 'jsd-159.og.summit19labs.com', 'jsd-160.og.summit19labs.com', 'jsd-161.og.summit19labs.com', 'jsd-162.og.summit19labs.com', 'jsd-163.og.summit19labs.com', 'jsd-164.og.summit19labs.com', 'jsd-165.og.summit19labs.com', 'jsd-166.og.summit19labs.com', 'jsd-167.og.summit19labs.com', 'jsd-168.og.summit19labs.com', 'jsd-169.og.summit19labs.com', 'jsd-170.og.summit19labs.com', 'jsd-171.og.summit19labs.com', 'jsd-172.og.summit19labs.com', 'jsd-173.og.summit19labs.com', 'jsd-174.og.summit19labs.com', 'jsd-175.og.summit19labs.com', 'jsd-176.og.summit19labs.com', 'jsd-177.og.summit19labs.com', 'jsd-178.og.summit19labs.com', 'jsd-179.og.summit19labs.com', 'jsd-180.og.summit19labs.com', 'jsd-181.og.summit19labs.com', 'jsd-182.og.summit19labs.com', 'jsd-183.og.summit19labs.com', 'jsd-184.og.summit19labs.com', 'jsd-185.og.summit19labs.com', 'jsd-186.og.summit19labs.com', 'jsd-187.og.summit19labs.com', 'jsd-188.og.summit19labs.com', 'jsd-189.og.summit19labs.com', 'jsd-190.og.summit19labs.com', 'jsd-191.og.summit19labs.com', 'jsd-192.og.summit19labs.com', 'jsd-193.og.summit19labs.com', 'jsd-194.og.summit19labs.com', 'jsd-195.og.summit19labs.com', 'jsd-196.og.summit19labs.com', 'jsd-197.og.summit19labs.com', 'jsd-198.og.summit19labs.com', 'jsd-199.og.summit19labs.com', 'jsd-200.og.summit19labs.com']
#j8_url_list = []
j8dc_url_list = ['kl-user-000.atlassian.guru', 'kl-user-001.atlassian.guru', 'kl-user-002.atlassian.guru', 'kl-user-003.atlassian.guru', 'kl-user-004.atlassian.guru', 'kl-user-005.atlassian.guru', 'kl-user-006.atlassian.guru', 'kl-user-007.atlassian.guru', 'kl-user-008.atlassian.guru', 'kl-user-009.atlassian.guru', 'kl-user-010.atlassian.guru', 'kl-user-011.atlassian.guru', 'kl-user-012.atlassian.guru', 'kl-user-013.atlassian.guru', 'kl-user-014.atlassian.guru', 'kl-user-015.atlassian.guru', 'kl-user-016.atlassian.guru', 'kl-user-017.atlassian.guru', 'kl-user-018.atlassian.guru', 'kl-user-019.atlassian.guru', 'kl-user-020.atlassian.guru', 'kl-user-021.atlassian.guru', 'kl-user-022.atlassian.guru', 'kl-user-023.atlassian.guru', 'kl-user-024.atlassian.guru', 'kl-user-025.atlassian.guru', 'kl-user-026.atlassian.guru', 'kl-user-027.atlassian.guru', 'kl-user-028.atlassian.guru', 'kl-user-029.atlassian.guru', 'kl-user-030.atlassian.guru', 'kl-user-031.atlassian.guru', 'kl-user-032.atlassian.guru', 'kl-user-033.atlassian.guru', 'kl-user-034.atlassian.guru', 'kl-user-035.atlassian.guru']
#j8dc_stack_list = ['j8dc-000', 'j8dc-001', 'j8dc-002', 'j8dc-003', 'j8dc-004', 'j8dc-005', 'j8dc-006', 'j8dc-007', 'j8dc-008', 'j8dc-009', 'j8dc-010', 'j8dc-011', 'j8dc-012', 'j8dc-013', 'j8dc-014', 'j8dc-015', 'j8dc-016', 'j8dc-017', 'j8dc-018', 'j8dc-019', 'j8dc-020', 'j8dc-021', 'j8dc-022', 'j8dc-023', 'j8dc-024', 'j8dc-025', 'j8dc-026', 'j8dc-027', 'j8dc-028', 'j8dc-029', 'j8dc-030', 'j8dc-031', 'j8dc-032', 'j8dc-033', 'j8dc-034', 'j8dc-035', 'j8dc-036', 'j8dc-037', 'j8dc-038', 'j8dc-039', 'j8dc-040', 'j8dc-041', 'j8dc-042', 'j8dc-043', 'j8dc-044', 'j8dc-045', 'j8dc-046', 'j8dc-047', 'j8dc-048', 'j8dc-049', 'j8dc-050', 'j8dc-051', 'j8dc-052', 'j8dc-053', 'j8dc-054', 'j8dc-055', 'j8dc-056', 'j8dc-057', 'j8dc-058', 'j8dc-059', 'j8dc-060', 'j8dc-061', 'j8dc-062', 'j8dc-063', 'j8dc-064', 'j8dc-065', 'j8dc-066', 'j8dc-067', 'j8dc-068', 'j8dc-069', 'j8dc-070', 'j8dc-071', 'j8dc-072', 'j8dc-073', 'j8dc-074', 'j8dc-075', 'j8dc-076', 'j8dc-077', 'j8dc-078', 'j8dc-079', 'j8dc-080', 'j8dc-081', 'j8dc-082', 'j8dc-083', 'j8dc-084', 'j8dc-085', 'j8dc-086', 'j8dc-087', 'j8dc-088', 'j8dc-089', 'j8dc-090']
bad_url_list = []
good_url_list = []

port = '8080'

def keyboardInterruptHandler(signal,frame):
	#log.debug('Received keyboard interrupt, Exiting')
	print('Exiting due to interrupt')
	exit(0)

signal.signal(signal.SIGINT, keyboardInterruptHandler)
'''
for stack in j8dc_stack_list:
	url = stack + '.j8dc.summit19labs.com'
	j8dc_url_list.append(url)

#print (j8dc_url_list)
'''

for url in j8dc_url_list:
	if port:
		full_url = 'http://' + url + ':' + str(port)
	else:
		full_url = 'http://' + url
	#print ('New url is %s' % full_url)
	if validators.url(full_url):
		#print ('Validation successful for %s' % full_url)
		try:
			r = requests.get(full_url)
		except requests.exceptions.RequestException as e:
			print ('Connection Error for url: %s' % full_url)
			bad_url_list.append(url)
		else:
			#print ('Status code for provided URL:' + full_url + ' is: ' + str(r.status_code))
			if (r.status_code == requests.codes.ok):
				print ('Connection Succesful for url: %s' %full_url)
				good_url_list.append(url)
	else:
		print ('Validation failed for %s' % url)
print ('List of NON working urls is: %s' % bad_url_list)
print ('List of working urls is: %s' % good_url_list)

exit(0)