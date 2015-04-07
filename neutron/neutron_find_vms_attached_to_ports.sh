#!/bin/sh
#Find Device/VM attached to all ports
#

#Find id of all ports
port_ids=$(neutron port-list | awk '{if($2!="id" && $2!="") print $2}')

for port_id in $port_ids;
do
	#Find device_id/vm of all port
	device_id=$(neutron port-show $port_id | awk '/device_id/ {print $4}')
	vm_name=$(nova show $device_id | awk '/ name/ {print $4}')
	echo "vm_name: $vm_name"
	echo "vm_id: $device_id"
	echo "port_id: $port_id"
	echo ""
	echo ""
done

