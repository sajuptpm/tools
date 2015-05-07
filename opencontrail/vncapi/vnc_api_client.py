#
#Dependencies
#
#$ find /usr -name vnc_api
#/usr/local/lib/python2.7/dist-packages/cfgm_common/uve/vnc_api
#/usr/local/lib/python2.7/dist-packages/vnc_api
#
#$ find /usr -name cfgm_common
#/usr/local/lib/python2.7/dist-packages/cfgm_common
#

import os
import time
import uuid
from vnc_api import vnc_api


def get_vnc_conn():

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

	# Retry till a api-server is up
	while True:
		try:
			vnc_conn = vnc_api.VncApi(username, password, tenant_name, 
						api_server_ip, api_server_port,
						auth_host=auth_host, auth_port=auth_port, auth_protocol=auth_protocol)
			return vnc_conn
		except requests.exceptions.RequestException as e:
			time.sleep(3)
#print "Connected to Contrail API Server:", get_vnc_conn()



def get_project(proj_id):
	conn = get_vnc_conn()
	#print dir(conn)
	proj_obj = conn.project_read(id=proj_id)
	#print proj_obj
	#print dir(proj_obj)
	return proj_obj
#project_id = str(uuid.UUID("68df249de3994dcaa1046e4c953f03c1"))
#get_project(project_id)
	


def get_quota(project_id):
	proj_obj = get_project(project_id)
	quota = proj_obj.get_quota()
	#print vars(quota)
	return quota
#project_id = str(uuid.UUID("68df249de3994dcaa1046e4c953f03c1"))
#get_quota(project_id)


def set_quota(project_id):
	conn = get_vnc_conn()
	proj_obj = get_project(project_id)
	quota = get_quota(project_id)
	quota.virtual_machine_interface = 3
	proj_obj.set_quota(quota)
	conn.project_update(proj_obj)
project_id = str(uuid.UUID("68df249de3994dcaa1046e4c953f03c1"))
set_quota(project_id)


















