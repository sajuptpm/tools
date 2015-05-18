export OS_HOST_IP=192.168.56.102
export OS_USERNAME=admin
export OS_PASSWORD=secret123
export OS_TENANT_NAME=admin
export OS_AUTH_URL=http://$OS_HOST_IP:35357/v2.0

CREDS=$(keystone ec2-credentials-list)
export ADMIN_EC2_ACCESS_KEY=$(echo "$CREDS" | awk '/ admin / { print $4 }')
export ADMIN_EC2_SECRET_KEY=$(echo "$CREDS" | awk '/ admin / { print $6 }')


