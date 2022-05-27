import boto3

ec2 = boto3.resource('ec2')

vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')

def create_subnet():
    subnet = ec2.create_subnet(CidrBlock = '10.0.20.0/24', VpcId= vpc.id)
    print(subnet.id)
    subnet = ec2.create_subnet(CidrBlock = '10.0.80.0/24', VpcId= vpc.id)
    print(subnet.id)

def create_igw():
   response = ec2_client.create_internet_gateway()
   igw = response.get("InternetGateway")
   igw_id = igw.get("InternetGatewayId")
   response = ec2_client.attach_internet_gateway(
       InternetGatewayId=igw_id,
       VpcId=vpc.id
   )

def create_route_table_with_route():
   response = ec2_client.create_route_table(VpcId=vpc.id)
   route_table = response.get("RouteTable")
   pprint(route_table)
   route_table_id = route_table.get("RouteTableId")
   ec2_client.create_tags(
       Resources=[route_table_id],
       Tags=[{"Key": "Name", "Value": "my-route-table"},],
   )
   response = ec2_client.create_route(
       DestinationCidrBlock='0.0.0.0/0',
       GatewayId=igw_id,
       RouteTableId=route_table_id,
   )


def main():
   create_subnet()
   create_igw()
   create_route_table_with_route()


if __name__ == "__main__":
   main()









