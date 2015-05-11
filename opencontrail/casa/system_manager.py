#Script to list all keyspaces and its column families
#https://pycassa.github.io/pycassa/api/pycassa/system_manager.html

from pprint import pprint
from pycassa.system_manager import SystemManager

sys_mr = SystemManager('127.0.0.1:9160')

def get_all_keyspaces():
	#List all keyspaces
	keyspaces = sys_mr.list_keyspaces()
	#print "keyspaces:", keyspaces
	return keyspaces

def get_keyspace_column_families(keyspace):
	column_families = sys_mr.get_keyspace_column_families(keyspace)
	#print column_families
	return column_families


keyspaces = get_all_keyspaces()
print "Keyspaces:==> ", pprint(keyspaces), "\n\n"

Keyspace_and_column_families_dict = {}
for keyspace in keyspaces:
	column_family = get_keyspace_column_families(keyspace) 
	#print "Column Families of keyspace:%s:==> " %(keyspace), pprint(column_family), "\n\n"
        Keyspace_and_column_families_dict[keyspace] = column_family.keys()
	
print "Keyspace and its Column Families:==> ", pprint(Keyspace_and_column_families_dict), "\n\n"

