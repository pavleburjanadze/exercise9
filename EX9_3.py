import boto3

ec2_client = boto3.client("ec2")

vpc_id = "vpc-0c652bad8c3b51ae9"

def create_igw(vpc_id):
   response = ec2_client.create_internet_gateway()
   igw = response.get("InternetGateway")
   igw_id = igw.get("InternetGatewayId")
   response = ec2_client.attach_internet_gateway(
       InternetGatewayId=igw_id,
       VpcId=vpc_id
   )
   print(igw_id)

def main():
   create_igw(vpc_id)


if __name__ == "__main__":
   main()

