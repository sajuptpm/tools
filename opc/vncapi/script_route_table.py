
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

def create_routetable_with_routes(conn, vnw, route_table_name, routes):
        rt = vnc_api.RouteTable(route_table_name)
        conn.route_table_create(rt)
        vnw.add_route_table(rt)
        conn.virtual_network_update(vnw)
        routes = vnc_api.RouteTableType()
	for route in routes:
        	route = vnc_api.RouteType(prefix=route["prefix"], next_hop=route["next_hop"])
        	routes.add_route(route)
        rt.set_routes(routes)
        conn.route_table_update(rt)	 


def get_existing_network(conn, fq_name):
	return conn.virtual_network_read(fq_name)

def get_existing_routing_instance(conn, fq_name):
	return conn.routing_instance_read(fq_name)


conn = get_vnc_conn()

####Create a route table with one route and add to an existing network ####
project_name = "demo"
network_name = "rtnw1"
route_table_name = "my-route-table5"
routes = [{"prefix":"192.168.6.3/32", "next_hop":"default-domain:demo:rtnw2:rtnw2"}]
####network_fq_name = ["default-domain", "demo", "rtnw1"]
network_fq_name = ["default-domain", project_name, network_name]
#vnw1 = get_existing_network(conn, network_fq_name)
#create_routetable_with_routes(conn, vnw1, route_table_name, routes)
####routing_instance_fq_name = ["default-domain", "demo", "rtnw1", "rtnw1"]
#routing_instance_fq_name = ["default-domain", project_name, network_name, network_name]
#rt_instance1 = get_existing_routing_instance(conn, routing_instance_fq_name)
#print rt_instance1
#print rt_instance1.get_static_route_entries()


def delete_all_route_tables(conn):
	route_tables = conn.route_tables_list()
	for rt in route_tables['route-tables']:
		print rt['fq_name'], rt['uuid']
		try:	
			conn.route_table_delete(id=str(rt['uuid']))
		except Exception as ex:
			print ex
			pass
####
#delete_all_route_tables(conn)


def route_table_read(conn, id=None, fq_name=None):
	if id:
		return conn.route_table_read(id=id)
	elif fq_name:
		return conn.route_table_read(fq_name=fq_name)


def get_routes_of_all_route_tables(conn):
	route_tables = conn.route_tables_list()
	for rt in route_tables['route-tables']:
		rt_obj = route_table_read(conn, id=rt['uuid'])
		#print rt_obj.serialize_to_json()
		#print rt_obj.dump()	
		print rt_obj.get_virtual_network_back_refs()
        	print "\n\nRoute Table:"
		print rt_obj.get_fq_name()
        	print "Routes:"
		for r in rt_obj.get_routes().route:
			print r.get_prefix(), "----", r.get_next_hop(), "----", r.get_next_hop_type()
####
get_routes_of_all_route_tables(conn)



def route_tables_delete_backrefs(conn):
        route_tables = conn.route_tables_list()
        for rt in route_tables['route-tables']:
                rt_obj = route_table_read(conn, id=rt['uuid'])
		#for bkref in rt_obj.backref_fields:
		#	print bkref
		for vnw_bkref in rt_obj.get_virtual_network_back_refs():
			vn = get_existing_network(conn, vnw_bkref['to'])
			vn.del_route_table(rt_obj)
			conn.virtual_network_update(vn)
####
#route_tables_delete_backrefs(conn)




def list_route_table_refs_of_all_virtual_networks(conn):
	vnws = conn.virtual_networks_list()
	for vn in vnws['virtual-networks']:
		#print vn['fq_name'], "----", vn['uuid']
		vn_obj = conn.virtual_network_read(id=vn['uuid'])
		route_table_refs = vn_obj.get_route_table_refs()
		print "\n\nVirtaul Network:"
		print vn['fq_name']
		print "Route Table refs:"
		print route_table_refs
		#if route_table_refs:
		#	for rt_ref in route_table_refs:
		#		#help(vn_obj.del_route_table)
		#		#rt_obj = conn.route_table_read(id=rt_ref['uuid'])
        	#		vn_obj.del_route_table(rt_obj)
       		# 		conn.virtual_network_update(vn_obj)
####
list_route_table_refs_of_all_virtual_networks(conn)


def list_all_ports_or_interfaces_with_its_ip_connected_toa_logical_router(conn):
    logical_routers = conn.logical_routers_list()
    if logical_routers:
            for lrt in logical_routers['logical-routers']:
                    lrt_obj = conn.logical_router_read(id=lrt['uuid'])
                    #print dir(lrt_obj)
                    print "\n\nRouter:"
                    print lrt['fq_name']
                    print "Ports/Interfaces:"
                    ports = lrt_obj.get_virtual_machine_interface_refs()
                    if ports:
                            for port in ports:
                                    port_obj = conn.virtual_machine_interface_read(id=port['uuid'])
                                    instance_ips = port_obj.get_instance_ip_back_refs()
                                    if instance_ips:
                                            for instance_ip in instance_ips:
                                                    instance_ip_obj = conn.instance_ip_read(id=instance_ip['uuid'])
                                                    print port['uuid'], "----", instance_ip_obj.get_instance_ip_address()
####
list_all_ports_or_interfaces_with_its_ip_connected_toa_logical_router(conn)



