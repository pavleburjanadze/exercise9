import boto3

ec2_client = boto3.client("ec2")

vpc_id = "vpc-0c652bad8c3b51ae9"

def create_subnet(vpc_id):
   response = ec2_client.create_subnet(VpcId=vpc_id, CidrBlock="10.10.1.0/24")
   subnet = response.get("Subnet")
   subnet_id = subnet.get("SubnetId")
   print(subnet_id)

def main():
   create_subnet(vpc_id)


if __name__ == "__main__":
   main()

