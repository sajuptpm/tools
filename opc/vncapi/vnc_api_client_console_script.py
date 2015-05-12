
"""
export OS_USERNAME=admin
export OS_PASSWORD=contrail123
export OS_TENANT_NAME=admin
export OS_AUTH_URL=http://10.140.218.21:35357/v2.0

"""

import os
import time
import uuid
from vnc_api import vnc_api

auth_url= os.environ['OS_AUTH_URL']
username= os.environ['OS_USERNAME']
password= os.environ['OS_PASSWORD']
tenant_name= os.environ['OS_TENANT_NAME']
auth_protocol = auth_url.split(':')[0]
auth_host = auth_url.split(':')[1].split("/")[2]
auth_port = auth_url.split(':')[2].split("/")[0]

#Contrail API Server IP and Port
api_server_ip = "10.140.218.12"
api_server_port = 8082

vnc_conn = vnc_api.VncApi(username, password, tenant_name, 
			api_server_ip, api_server_port,
			auth_host=auth_host, auth_port=auth_port, auth_protocol=auth_protocol)


project_id = str(uuid.UUID("68df249de3994dcaa1046e4c953f03c1"))
vnc_conn.project_read(id=project_id)




