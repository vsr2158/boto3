import logging
import boto3
from botocore.exceptions import ClientError

bucket = "137965528627-s3get-ebsput"
file_name = "/Users/raovi/Downloads/rpm"
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
while i < 10:
    print ("Starting upload: " + str(i))
    i += 1
    object_name = "file" + str(i)
    upload_file(file_name,bucket,object_name)


