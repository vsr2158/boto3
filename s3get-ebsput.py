import boto3
import datetime as datetime
BUCKET_NAME = "137965528627-s3get-ebsput"
OBJECT_NAME = 'file1'
FILE_NAME = OBJECT_NAME

def s3_get (BUCKET_NAME,OBJECT_NAME):
    s3 = boto3.client('s3')
    try:
        s3.download_file('BUCKET_NAME', 'OBJECT_NAME', str(current_utc_time))
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False

current_utc_time = datetime.datetime.utcnow()
s3_get(BUCKET_NAME, OBJECT_NAME)

