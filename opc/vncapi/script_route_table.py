
import os
import time
import uuid
from vnc_api_client import get_vnc_conn##SM
from vnc_api import vnc_api

def create_virtual_network(conn, vn_name, vn_subnet):
	vn_obj = vnc_api.VirtualNetwork(name=vn_name)
	ipam_fq_name = ['default-domain', 'default-project', 'default-network-ipam']
	ipam_obj = conn.network_ipam_read(fq_name=ipam_fq_name)
	cidr = vn_subnet.split('/')
	pfx = cidr[0]
	pfx_len = int(cidr[1])
	subnet_info = vnc_api.IpamSubnetType(subnet=vnc_api.SubnetType(pfx, pfx_len))
	subnet_data = vnc_api.VnSubnetsType([subnet_info])
	vn_obj.add_network_ipam(ipam_obj, subnet_data)
	conn.virtual_network_create(vn_obj)
	vn_obj.clear_pending_updates()
	return vn_obj

def create_routetable_with_routes(conn, vnw1, route_table_name):
        rt = vnc_api.RouteTable(route_table_name)
        conn.route_table_create(rt)
        vnw1.add_route_table(rt)
        conn.virtual_network_update(vnw1)
        routes = vnc_api.RouteTableType()
        route = vnc_api.RouteType(prefix="5.5.5.5/28", next_hop="default-domain:demo:web-net:web-net")
        routes.add_route(route)
        rt.set_routes(routes)
        conn.route_table_update(rt)	 


def get_existing_network(conn, fq_name):
	return conn.virtual_network_read(fq_name)


conn = get_vnc_conn()

####Create a route table with one route and add to an existing network ####
fq_name = ["default-domain", "demo", "nw1"]
vnw1 = get_existing_network(conn, fq_name)
create_routetable_with_routes(conn, vnw1, "my-route-table4")






