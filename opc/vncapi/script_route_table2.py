
import os
import time
import uuid
from vnc_api_client import get_vnc_conn##SM
from vnc_api import vnc_api


def get_existing_network(conn, fq_name):
        return conn.virtual_network_read(fq_name)


def get_existing_routing_instance(conn, fq_name):
        return conn.routing_instance_read(fq_name)


def project_read(conn, proj_id=None, fq_name=None):
	proj_obj = conn.project_read(id=proj_id, fq_name=fq_name)
	return proj_obj


def create_or_update_route_table_with_routes(conn, rt_q, oper):
    #contrail-controller/src/config/vnc_openstack/vnc_openstack/neutron_plugin_db.py
    if oper == "CREATE":
        project_id = str(uuid.UUID(rt_q['tenant_id']))
        project_obj = project_read(conn, proj_id=project_id)
	print "===project_obj===", project_obj
        rt_vnc = vnc_api.RouteTable(name=rt_q['name'],
                            parent_obj=project_obj)

        if not rt_q['routes']:
            return rt_vnc

        for route in rt_q['routes']['route']:
	    print "=====route======", route
            try:
                vm_obj = conn.virtual_machine_read(id=route['next_hop'])
		print "======vm_obj=====", vm_obj
                si_list = vm_obj.get_service_instance_refs()
		print "=======si_list=======", si_list
                if si_list:
                    fq_name = si_list[0]['to']
	            print "======fq_name======", fq_name		 
                    si_obj = conn.service_instance_read(fq_name=fq_name)
		    print "====si_obj=====", si_obj	
                    route['next_hop'] = si_obj.get_fq_name_str()
	 	    print "====si_obj.get_fq_name_str()=======", si_obj.get_fq_name_str()	
            except Exception as e:
                pass
        rt_vnc.set_routes(vnc_api.RouteTableType.factory(**rt_q['routes']))
    else:
	##Update
        rt_vnc = conn.route_table_read(id=rt_q['id'])

        for route in rt_q['routes']['route']:
            try:
                vm_obj = conn.virtual_machine_read(id=route['next_hop'])
                si_list = vm_obj.get_service_instance_refs()
                if si_list:
                    fq_name = si_list[0]['to']
                    si_obj = conn.service_instance_read(fq_name=fq_name)
                    route['next_hop'] = si_obj.get_fq_name_str()
            except Exception as e:
                pass
        rt_vnc.set_routes(vnc_api.RouteTableType.factory(**rt_q['routes']))
    return rt_vnc



###############

route_table_name = "my-toute-table10"
tenant_id = "2d628eeaba9944ca8b20208510f9f231"
route1_cidr ="192.168.6.3/32"

route_dict = {'route': [{'prefix': route1_cidr,
                         'next_hop': "tap7bb2858f-b4",
                         'next_hop_type': None}]}

route_table = {'name': route_table_name, 'tenant_id': tenant_id, 'routes': route_dict}

conn = get_vnc_conn()
route_table_vnc_obj = create_or_update_route_table_with_routes(conn, route_table, "CREATE")
#conn.route_table_create(route_table_vnc_obj)






project_name = "demo"
network_name = "rtnw2"
network_fq_name = ["default-domain", project_name, network_name]
vnw1 = get_existing_network(conn, network_fq_name)

#vnw1.add_route_table(route_table_vnc_obj)
#conn.virtual_network_update(vnw1)



irt = conn.interface_route_table_read([u'default-domain', u'demo', u'my-route-table11'])
print irt
print "bbbb", [vars(r) for r in irt.get_interface_route_table_routes().get_route()]
vnw1.add_route_table(irt)
conn.virtual_network_update(vnw1)



routing_instance_fq_name = ["default-domain", project_name, network_name, network_name]
rt_instance1 = get_existing_routing_instance(conn, routing_instance_fq_name)
print rt_instance1
print rt_instance1.get_static_route_entries()







