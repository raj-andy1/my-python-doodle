import datetime
import tzlocal

x = {"Contents": [{"Key": "siteimport/datasets/cloud-jira-partner-edu-jsw-align-30users.zip", "LastModified": datetime.datetime(2021, 3, 18, 17, 26, 1), "ETag": "5ad9d9445f6d171347f6f2a7084bf256", "Size": 222040, "StorageClass": "STANDARD", "Owner": {"DisplayName": "cloud-team+paas-dev", "ID": "b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426"}},
{"Key": "siteimport/datasets/cloud-jira-se-demo-jsm-jsw-10users-groups.zip", "LastModified": datetime.datetime(2021, 3, 15, 5, 35, 16), "ETag": "ea4c17ee65d30e13140839027928e63a-4", "Size": 30046679, "StorageClass": "STANDARD", "Owner": {"DisplayName": "cloud-team+paas-dev", "ID": "b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426"}},
{"Key": "siteimport/datasets/cloud-jira-tis-jsd-jsw-10users-groups.zip", "LastModified": datetime.datetime(2021, 3, 18, 17, 26, 16), "ETag": "f5e3d437a9e5b31ec2e3710999e387b1", "Size": 2218701, "StorageClass": "STANDARD", "Owner": {"DisplayName": "cloud-team+paas-dev", "ID": "b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426"}},
{"Key": "siteimport/datasets/mega-cloud-lab-15.jira-dev.com.zip", "LastModified": datetime.datetime(2021, 3, 15, 22, 0, 12), "ETag": "e8fdb25aed497cb94e86d8c15c3d8f13", "Size": 459538, "StorageClass": "STANDARD", "Owner": {"DisplayName": "cloud-team+paas-dev", "ID": "b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426"}},
{"Key": "siteimport/datasets/se-demo-final-jsm-12-10-20.zip", "LastModified": datetime.datetime(2021, 3, 18, 6, 40, 48), "ETag": "ba7e2a63266ce7879970b506e13146a2-4", "Size": 29980887, "StorageClass": "STANDARD", "Owner": {"DisplayName": "cloud-team+paas-dev", "ID": "b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426"}},
{"Key": "siteimport/datasets/se-sandbox.atlassian.net-no-users.zip", "LastModified": datetime.datetime(2021, 3, 22, 18, 16, 48), "ETag": "5ff3118df9fe2ff50b0739a05dd8da35-5", "Size": 38671809, "StorageClass": "STANDARD", "Owner": {"DisplayName": "cloud-team+paas-dev", "ID": "b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426"}}]}


z = {'ResponseMetadata': {'RequestId': 'X61YMQ7NY46MGAK8', 'HostId': '9IpEkb4keK54NoToZwPZ0la6Px9P0bbGqpQC9v4R7+dPPyPrWxybCDX8ac+YVkUFElC75mrOXvs=', 'HTTPStatusCode': 200, 'HTTPHeaders': {'x-amz-id-2': '9IpEkb4keK54NoToZwPZ0la6Px9P0bbGqpQC9v4R7+dPPyPrWxybCDX8ac+YVkUFElC75mrOXvs=', 'x-amz-request-id': 'X61YMQ7NY46MGAK8', 'date': 'Thu, 08 Apr 2021 14:41:51 GMT', 'x-amz-bucket-region': 'ap-southeast-2', 'content-type': 'application/xml', 'transfer-encoding': 'chunked', 'server': 'AmazonS3'}, 'RetryAttempts': 0}, 'IsTruncated': False, 'Marker': '',
     'Contents': [{'Key': '/datasets/cloud-jira-se-demo-jsm-jsw-10users-groups.zip', 'LastModified': datetime.datetime(2021, 4, 6, 1, 17, 59), 'ETag': '"9d714ceafe6f38d8ce474534a443d905-4"', 'Size': 30046679, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'cloud-team+paas-dev', 'ID': 'b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426'}},
                  {'Key': '/datasets/cloud-jira-tis-jsd-jsw-10users-groups.zip', 'LastModified': datetime.datetime(2021, 4, 6, 4, 13, 15), 'ETag': '"e18c2493a667269aeb575d5e71906721"', 'Size': 2218701, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'cloud-team+paas-dev', 'ID': 'b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426'}},
                  {'Key': '/datasets/mega-cloud-lab-15.jira-dev.com.zip', 'LastModified': datetime.datetime(2021, 4, 6, 16, 35, 7), 'ETag': '"5abe1e01bf816df4f0761009b84c2be1"', 'Size': 459538, 'StorageClass': 'STANDARD', 'Owner': {'DisplayName': 'cloud-team+paas-dev', 'ID': 'b538b2a112c83e40babc29e7a77fb3ab091f23c4869cf36317d0916e4599a426'}}],
     'Name': 'rps--ddev--demofactory--datasets', 'Prefix': '/datasets', 'MaxKeys': 1000, 'EncodingType': 'url'}


y={}
for item in z['Contents']:
    print(item['Key'])


