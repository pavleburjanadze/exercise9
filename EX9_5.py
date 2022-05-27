import boto3

ec2_client = boto3.client("ec2")

rt_id = "rtb-0f7ea1e64c36b7a46"
igw_id = "igw-078bd0e04151b0711"

def create_rt_with_route():
   response = ec2_client.create_route(
       DestinationCidrBlock='0.0.0.0/0',
       GatewayId=igw_id,
       RouteTableId=rt_id,
   )

def main():
   create_rt_with_route()


if __name__ == "__main__":
   main()

