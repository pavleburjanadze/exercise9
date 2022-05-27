import boto3

ec2_client = boto3.client("ec2")

route_table_id = "rtb-0f7ea1e64c36b7a46"
subnet_id = "subnet-07a546f23890f753f"

def associate_route_table_to_subnet(route_table_id, subnet_id):
   response = ec2_client.associate_route_table(
       RouteTableId=route_table_id,
       SubnetId=subnet_id
   )


def main():
    associate_route_table_to_subnet(route_table_id, subnet_id)


if __name__ == "__main__":
   main()

