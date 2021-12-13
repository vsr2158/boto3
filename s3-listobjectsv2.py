import boto3
import time
from botocore.exceptions import ClientError
'''
This script will list all objects from the bucket 1000 keys at a time
'''

bucket = "<BucketName>"

s3_client = boto3.client('s3')
KEY_FIRST = ''
KEY_LAST = 'file'
TIME_LIST = []
TOKEN = ''
while KEY_LAST != KEY_FIRST:
    print('++++++++++++++++++++++++++++++++++++')
    print(time.time())
    TIME_LIST.append(time.time())
    if len(TOKEN) !=0:
        try:
            response = s3_client.list_objects_v2(
                Bucket=bucket,
                Delimiter=',',
                EncodingType='url',
                ContinuationToken=TOKEN,
                MaxKeys=1000
            )
        except ClientError as e:
            logging.error(e)
    else:
        try:
            response = s3_client.list_objects_v2(
                Bucket=bucket,
                Delimiter=',',
                EncodingType='url',
                MaxKeys=1000
            )
        except ClientError as e:
            logging.error(e)

    CONTENTS = response.get('Contents')
    METADATA = response.get('ResponseMetadata')
    print(METADATA)
    TOKEN = response.get('NextContinuationToken')
    if TOKEN is None:
        TIME_DELTA = TIME_LIST[-1] - TIME_LIST[0]
        print('We got last File, total time taken: ' + str(TIME_DELTA))
        quit()


    if not CONTENTS:
        TIME_DELTA = TIME_LIST[-1] - TIME_LIST[0]
        print('We got last file, total time taken: ' + str(TIME_DELTA))

        break
    else:
        OBJ_FIRST = CONTENTS[0]
        KEY_FIRST = OBJ_FIRST.get('Key')

        OBJ_LAST = CONTENTS[-1]
        KEY_LAST = OBJ_LAST.get('Key')

        print('First File : ' + KEY_FIRST)
        print('Last File : '+ KEY_LAST)
        print('-----------------------')





