import boto3

REGION = "us-east-1"

AMI_ID = "ami-081b0a6eac00b4f53"

ec2 = boto3.client("ec2", region_name=REGION)

response = ec2.run_instances(
    ImageId=AMI_ID,
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1
)

instance_id = response["Instances"][0]["InstanceId"]

print("EC2 server launched!")
print("Instance ID:", instance_id)