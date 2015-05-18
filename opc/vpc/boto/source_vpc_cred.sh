VPC_ID=vpc-af9bbb83
USER_NAME="user2"


TENANT_LIST=$(keystone tenant-list)
TENANT_ID=$(echo "$TENANT_LIST" | awk  "/ $VPC_ID /" | awk '{ print $2 }')
if [ -z $TENANT_ID ]
then
    echo "TENANT_ID is empty"
    exit 2
fi

ROLE_LIST=$(keystone role-list)
ADMIN_ROLE_ID=$(echo "$ROLE_LIST" | awk '/ admin / { print $2 }')
if [ -z $ADMIN_ROLE_ID ]
then
    echo "ADMIN_ROLE_ID is empty"
    exit 2
fi


USER_LIST=$(keystone user-list)
USER_ID=$(echo "$USER_LIST" | awk  "/ $USER_NAME /" | awk '{ print $2 }')
if [ -z $USER_ID ]
then
    echo "Creating new user ...."
    CREATE_USER=$(keystone user-create --name $USER_NAME --tenant $TENANT_ID --pass password --enabled true)

    USER_ID=$(echo "$CREATE_USER" | awk '/ id / { print $4 }')
    if [ -z $USER_ID ]
    then
        echo "USER_ID is empty"
        exit 2
    fi

    USER_ROLE_ADD=$(keystone user-role-add --user $USER_ID --role $ADMIN_ROLE_ID --tenant $TENANT_ID)

    $(echo "$USER_ROLE_ADD")

    EC2_CRED_CRE=$(keystone ec2-credentials-create --user-id $USER_ID --tenant-id $TENANT_ID)

    export VPC_USER_EC2_ACCESS_KEY=$(echo "$EC2_CRED_CRE" | awk '/ access / { print $4 }')

    export VPC_USER_EC2_SECRET_KEY=$(echo "$EC2_CRED_CRE" | awk '/ secret / { print $4 }')
else
    echo "User already exist, Finding Access and Secret Access Keys"
    CREDS=$(keystone ec2-credentials-list)
    export VPC_USER_EC2_ACCESS_KEY=$(echo "$CREDS" | awk '/ USER_NAME / { print $4 }')
    export VPC_USER_EC2_SECRET_KEY=$(echo "$CREDS" | awk '/ USER_NAME / { print $6 }')
fi



