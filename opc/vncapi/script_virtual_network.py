
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


conn = get_vnc_conn()
create_virtual_network(conn, "sa-nw1", "12.1.1.0/28")

