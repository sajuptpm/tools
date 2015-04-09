#!/bin/bash

SECURITY_GROUP_NAME=sec1

show=$(neutron security-group-show $SECURITY_GROUP_NAME)
if [ $? -eq 1 ]
then
	##Create a security group
	neutron security-group-create $SECURITY_GROUP_NAME
fi

##Create rules
for x in {1..95}
do
	#echo $x
	neutron security-group-rule-create --protocol tcp --port-range-min 22 --port-range-max 22 --direction ingress $SECURITY_GROUP_NAME
done

#Find number of rules in the security group
num_rules=$(neutron security-group-rule-list | awk '/sec1/' | wc -l)

echo ""
echo "number of rules in the security group:$SECURITY_GROUP_NAME is :$num_rules"
echo ""


