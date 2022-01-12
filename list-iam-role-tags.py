import boto3
import json
iam = boto3.client("iam")
roles = iam.list_roles()
print (roles)
roles_name = roles.get("Roles").("RoleName")
print(roles_name)