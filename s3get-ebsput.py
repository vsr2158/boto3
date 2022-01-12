import boto3
import random
import threading
import time
'''
This script will get objects form the specified S3 bucket and store in filesystem.
The script randomizes the object names to be retrieved from S3 to distribute the load on S3
It also runs 500 threads parallel to stress the network, use thread_count variable to adjust this.
change the next four variables to match your environment
bucket = "s3get-ebsput"
object_name = 'file'
file_name = object_name
thread_count = 500
'''

bucket = "s3get-ebsput"
object_name = 'file'
file_name = object_name
thread_count = 25

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
    for i in range (100000):
        for i in range (thread_count):
            thr = threading.Thread(target=s3_get, args=(file_name,bucket,object_name))
            thr.start()
except:
   print ("Error: unable to start thread")

