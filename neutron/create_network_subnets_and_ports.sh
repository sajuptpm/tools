neutron net-create nw1
neutron subnet-create ccddb5c4-ebb9-490a-9706-27462e854188 44.44.44.0/24
neutron subnet-create ccddb5c4-ebb9-490a-9706-27462e854188 88.88.88.0/24
#Create 10 ports in a subnet
for x in {1..10}; do neutron port-create --fixed-ip subnet_id=9e52dd17-48ad-4684-afa3-6e7a7ad86600 nw1; done
