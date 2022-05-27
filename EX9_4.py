import boto3

ec2_client = boto3.client("ec2")

vpc_id = "vpc-0c652bad8c3b51ae9"

def create_rt(vpc_id):
   response = ec2_client.create_route_table(VpcId=vpc_id)
   route_table = response.get("RouteTable")
   route_table_id = route_table.get("RouteTableId")
   print(route_table_id)

def main():
   create_rt(vpc_id)


if __name__ == "__main__":
   main()

