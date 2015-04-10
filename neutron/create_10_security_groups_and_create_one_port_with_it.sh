#!/bin/bash

##Create 10 security groups
##This loop will create 10 security groups from mygroup1, mygroup2, mygroup3, .... mygroup10
for x in {1..10}
do 
neutron security-group-create mygroup$x
done


##Create a port with 10 security groups which we created
neutron port-create --fixed-ip subnet_id=c10eb471-8fb0-415c-a6d3-ae1a92d7e24c $(for x in {1..11}; do echo "--security-group mygroup$x"; done) 6968d367-ee79-4b55-9aba-b5b74882f108

#Uses a for loop in port-create commad to append/specify 10 security groups like --security-group mygroup1, --security-group mygroup2, ....
#10eb471-8fb0-415c-a6d3-ae1a92d7e24c is subnet id
#6968d367-ee79-4b55-9aba-b5b74882f108 is network id



