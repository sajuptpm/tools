#!/bin/bash

#### To fix network issue in the contrail setup vm ####
#sudo rm /etc/udev/rules.d/70-persistent-net.rules

#### To fis provision issue ####
#sudo vim /etc/nova/nova-compute.conf

#[DEFAULT]
#compute_driver=libvirt.LibvirtDriver
#[libvirt]
#virt_type=kvm

#sudo service nova-compute restart

##############

export OS_USERNAME=admin
export OS_PASSWORD=secret123
export OS_TENANT_NAME=admin
export OS_AUTH_URL=http://127.0.0.1:35357/v2.0

image_file=cirros-0.3.2-x86_64-disk.img

if [ -f "$image_file" ]
then
    echo "File $image_file exist"
    echo ""
else
    echo "Downloading cirros-0.3.2-x86_64-disk.img ....."
    echo ""
    wget http://download.cirros-cloud.net/0.3.2/cirros-0.3.2-x86_64-disk.img
fi

echo "Uploading image cirros-0.3.2-x86_64-disk.img ....."
glance image-create --progress --name cirros-0.3.2 --disk-format qcow2 --container-format bare --is-public True --file $image_file




