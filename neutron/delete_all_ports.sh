#!/bin/bash
#Delete all ports one by one

for x in $(neutron port-list | awk  '{print $2}'); 
do
neutron port-delete $x; 
done

