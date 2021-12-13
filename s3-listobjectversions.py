import boto3
import time
import pprint
from botocore.exceptions import ClientError
'''
This script will list all object version from the bucket 1000 keys at a time
'''

bucket = "<BucketName>"

s3_client = boto3.client('s3')
KEY_FIRST = ''
KEY_LAST = 'file'
TIME_LIST = []
while KEY_LAST != KEY_FIRST:
    print('-----------------------')
    print(time.time())
    TIME_LIST.append(time.time())
    try:
        response = s3_client.list_object_versions(
            Bucket=bucket,
            Delimiter=',',
            EncodingType='url',
            KeyMarker=KEY_LAST,
            MaxKeys=1000,
        )
    except ClientError as e:
        logging.error(e)
    print('KeyMarker: ' + KEY_LAST)
    #pprint.pprint(response)
    VERSIONS = response.get('Versions')
    METADATA = response.get('ResponseMetadata')
    #print("Matadeta: " + str(METADATA))
    #print('Contents: ' + str(CONTENTS))

    if not VERSIONS:
        TIME_DELTA = TIME_LIST[-1] - TIME_LIST[0]
        print('We got last file, total time taken: ' + str(TIME_DELTA))
        break
    else:
        OBJ_FIRST = VERSIONS[0]
        KEY_FIRST = OBJ_FIRST.get('Key')

        OBJ_LAST = VERSIONS[-1]
        KEY_LAST = OBJ_LAST.get('Key')

        print('First File : ' + KEY_FIRST)
        print('Last File : '+ KEY_LAST)
        print('-----------------------')





