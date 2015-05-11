#Script to list all "row keys" and its data, of a column family.

import sys, getopt
from pprint import pprint
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

HOST_AND_PORT = ['127.0.0.1:9160']

#KEYSPACE = 'config_db_uuid' #name of database
#COLUMN_FAMILY_NAME = 'obj_fq_name_table' #name of table

######################

#pool = ConnectionPool(KEYSPACE, HOST_AND_PORT)
#col_fam_conn = ColumnFamily(pool, COLUMN_FAMILY_NAME)

######################

def get_all_row_keys(col_fam_conn):
	row_keys = dict(col_fam_conn.get_range()).keys()
	print "Row Keys:==> ", pprint(row_keys), "\n\n"
	return row_keys

#row_keys = get_all_row_keys(col_fam_conn)

#####################

#row_key = "virtual_network"

#####################

def get_data_with_row_key(col_fam_conn, row_key):
	data = col_fam_conn.get(row_key)
	data = dict(data)
	print "Data of Row Key:%s: ==> " %(row_key), pprint(data), "\n\n"
	return data
#get_data_with_row_key(col_fam_conn, row_key)

#####################

def find_how_many_columns_are_in_a_row(col_fam_conn, row_key):
	num = col_fam_conn.get_count("virtual_network")
	print "Number of Columns in Row Key: %s ==> " %(row_key), num, "\n\n"
	return num
#find_how_many_columns_are_in_a_row(col_fam_conn, row_key)

#####################

def find_how_many_columns_are_in_list_of_rows(col_fam_conn, row_keys):
	res = dict(col_fam_conn.multiget_count(row_keys))
	print "Number of Columns in all Row Keys: ==> ", pprint(res), "\n\n"
	return res
#find_how_many_columns_are_in_list_of_rows(col_fam_conn, row_keys)

####################

#for rowkey in row_keys:
#	get_data_with_row_key(rowkey)

####################


def main(argv):

	KEYSPACE = None
	COLUMN_FAMILY_NAME = None

	optlist, args = getopt.getopt(argv, 'k:c:')
	for opt, arg in optlist:
		if opt == "-k":
			KEYSPACE = arg
		if opt == "-c":
			COLUMN_FAMILY_NAME = arg

	if not KEYSPACE or not COLUMN_FAMILY_NAME:
		usage()
		sys.exit(2)

	pool = ConnectionPool(KEYSPACE, HOST_AND_PORT)
	col_fam_conn = ColumnFamily(pool, COLUMN_FAMILY_NAME)
	
	row_keys = get_all_row_keys(col_fam_conn)	

	find_how_many_columns_are_in_list_of_rows(col_fam_conn, row_keys)

	for rowkey in row_keys:
		get_data_with_row_key(col_fam_conn, rowkey)

def usage():
	print "Usage: $python data_manager.py -k keyspace -c column_family"


if __name__ == "__main__":
	#Script to list all "row keys" and its data, of a column family.
	#$python data_manager.py -k keyspace -c column_family
	#$python data_manager.py -k config_db_uuid -c obj_fq_name_table
	#$python data_manager.py -k config_db_uuid -c obj_uuid_table
	main(sys.argv[1:])





