import logging
import boto3
from botocore.exceptions import ClientError
'''
This script will take a single file from your filesystem and upload to the specified S3 bucket
During each upload the filename is appended with a number making the objects unique
change the next three variables to match your environment
bucket = "-s3get-ebsput"
file_name = "file"
max_objects = 10
'''

bucket = "<BucketName>"
file_name = "s3-putobjects.py"
max_objects = 20000

i = 0
def upload_file(file_name, bucket, object_name):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name
    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
while i < max_objects:
    print ("Starting upload: " + str(i))
    i += 1
    object_name = "replication-" + str(i)
    upload_file(file_name,bucket,object_name)


