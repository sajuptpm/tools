import os
import boto
import boto, boto.ec2

SUBNET_CIDRS = ['10.1.1.0/29', '10.1.1.8/29']

print "\n\nPlease source 'source_vpc_cred.sh' before running this script.\n\n"

region = boto.ec2.regioninfo.RegionInfo(name="nova",endpoint=os.environ['OS_HOST_IP'])

conn = boto.connect_vpc(aws_access_key_id=os.environ['VPC_USER_EC2_ACCESS_KEY'],
                        aws_secret_access_key=os.environ['VPC_USER_EC2_SECRET_KEY'],
                        is_secure=False,
                        region=region,
                        port=8773,
                        path="/services/Cloud")

vpcs = conn.get_all_vpcs()
print vpcs
subnets = conn.get_all_subnets()
print subnets

for subnet_cidr in SUBNET_CIDRS:
    conn.create_subnet(vpcs[0].id, subnet_cidr)
    conn.create_subnet(vpcs[0].id, subnet_cidr)

subnets = conn.get_all_subnets()

images = conn.get_all_images()
print images

for subnet in subnets: 
    conn.run_instances(image_id="ami-00000001", instance_type="m1.tiny", subnet_id=subnet.id)


