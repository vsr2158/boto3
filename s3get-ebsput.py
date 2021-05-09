import boto3
import random
import threading
import time

bucket = "137965528627-s3get-ebsput"
object_name = 'file'
file_name = object_name

def s3_get (file_name, bucket, object_name):
    s3 = boto3.client('s3')
    r = str(random.randrange(1,1000))
    object_name = object_name + r
    file_name = object_name
    try:
        s3.download_file(bucket,object_name, file_name)
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False

try:
    for i in range (25):
        threading.Thread(target=s3_get(file_name,bucket,object_name))

except:
   print ("Error: unable to start thread")

