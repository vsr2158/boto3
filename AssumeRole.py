import boto3
ACCOUNT_LIST = [1234567890,0123456789,0912345678]
ROLE_NAME = 'role-sq1'

sts_client = boto3.client('sts')
for A in ACCOUNT_LIST:
    A = str(A)
    RoleArn = "arn:aws:iam::"+A+":role/"+ROLE_NAME

    print(RoleArn)
    assumed_role_object=sts_client.assume_role(
        RoleArn=RoleArn,
        RoleSessionName="AssumeRoleSession1"
    )
