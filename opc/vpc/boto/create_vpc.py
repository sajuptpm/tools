import os
import boto
import boto, boto.ec2

VPC_CIDR = '10.1.1.0/24'

print "\n\nPlease source 'source_admin_cred.sh' before running this script.\n\n"

region = boto.ec2.regioninfo.RegionInfo(name="nova",endpoint=os.environ['OS_HOST_IP'])

conn = boto.connect_vpc(aws_access_key_id=os.environ['ADMIN_EC2_ACCESS_KEY'],
                        aws_secret_access_key=os.environ['ADMIN_EC2_SECRET_KEY'],
                        is_secure=False,
                        region=region,
                        port=8773,
                        path="/services/Cloud")

vpcs = conn.get_all_vpcs()
vpc = conn.create_vpc(VPC_CIDR)
vpcs = conn.get_all_vpcs()
print vpcs


