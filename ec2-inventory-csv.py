import sys
import botocore
import boto3
import json
import csv
csv_columns = ['Region' ,'ImageId', 'AMIDescription','InstanceId','InstanceType']
csv_file = "ec2-inventory.csv"
# Get list of regions
ec2_client = boto3.client("ec2")
regions = [region['RegionName']
           for region in ec2_client.describe_regions()['Regions']]

print ("######### List of all regions to be iterated #########")
print(regions)
final_list = []
for region in regions:
    ec2 = boto3.client("ec2", region_name = region)
    print(f'######### Going to check {region} #########')
    # Get list of Ec2 instances
    response = ec2.describe_instances()
    list_instance = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            # This sample print will output entire Dictionary object
            # This will print will output the value of the Dictionary key 'InstanceId'
            print(instance["InstanceId"])
            required_fields = ['ImageId','InstanceId','InstanceType']
            new_dict = {key:value for key, value in instance.items() if key in required_fields}
            print (new_dict)
            list_instance.append(new_dict)
    print(list_instance)
    #now lets get the AMI description added to the list
    for i in list_instance:
        image_id = (i["ImageId"])
        describe_images = ec2.describe_images(ImageIds = [image_id])
        image_description = (describe_images.get("Images")[0].get("Description"))
        i["AMIDescription"] = image_description
        i["Region"] = region
        print (i)
       # lets create a new list
        final_list.append(i)

print (final_list)
try:
    with open(csv_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for i in final_list:
            # print (i)
            writer.writerow(i)
except IOError:
    print("I/O error")