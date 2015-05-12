import sys, getopt
from pprint import pprint
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily

HOST_AND_PORT = ['127.0.0.1:9160']


def get_data_with_row_key(col_fam_conn, row_key):
        data = col_fam_conn.get(row_key)
        data = dict(data)
        print "Data of Row Key:%s: ==> " %(row_key), pprint(data), "\n\n"
        return data

def get_data_with_row_key_filter_by_columns(col_fam_conn, row_key, columns):
        data = col_fam_conn.get(row_key, columns=columns)
        data = dict(data)
        print "Data of Row Key:%s: ==> " %(row_key), pprint(data), "\n\n"
        return data

def get_data_with_row_key_filter_by_start_and_end_column(col_fam_conn, row_key, columns):
        data = col_fam_conn.get(row_key, column_start='parent:project', column_finish='parent:project')
        data = dict(data)
        print "Data of Row Key:%s: ==> " %(row_key), pprint(data), "\n\n"
        return data


#KEYSPACE = 'config_db_uuid' #name of database
#COLUMN_FAMILY_NAME = 'obj_uuid_table' #name of table

#pool = ConnectionPool(KEYSPACE, HOST_AND_PORT)
#col_fam_conn = ColumnFamily(pool, COLUMN_FAMILY_NAME)



#row_key="1fd037a4-95af-4ae2-bd41-36ad5c1fc6dc"
#columns=['parent_type', 'prop:display_name']
#columns=['prop']

#col_fam_conn.get(row_key, columns=columns)


#get_data_with_row_key(col_fam_conn, row_key)
#get_data_with_row_key_filter_by_columns(col_fam_conn, row_key, columns)
#get_data_with_row_key_filter_by_start_and_end_column(col_fam_conn, row_key, columns)


def main(argv):
	KEYSPACE = None
	COLUMN_FAMILY_NAME = None
	ROW_KEY = None
	COLUMNS = []

        optlist, args = getopt.getopt(argv, 'k:c:r:f:')
        for opt, arg in optlist:
        	if opt == "-k":
        		KEYSPACE = arg
        	if opt == "-c":
        		COLUMN_FAMILY_NAME = arg
		if opt == "-r":
			ROW_KEY = arg
		if opt == "-f":
			COLUMNS.append(arg)

	if not KEYSPACE or not COLUMN_FAMILY_NAME or not ROW_KEY:
		usage()
		sys.exit(2)
        pool = ConnectionPool(KEYSPACE, HOST_AND_PORT)
	col_fam_conn = ColumnFamily(pool, COLUMN_FAMILY_NAME)
	
	if COLUMNS:
		get_data_with_row_key_filter_by_columns(col_fam_conn, ROW_KEY, COLUMNS)
	else: 	
		get_data_with_row_key(col_fam_conn, ROW_KEY)	


def usage():
	print "Usage: $python data_manager.py -k keyspace -c column_family -r row_key"

if __name__ == "__main__":
        #$python get_data.py -k keyspace -c column_family -r row_key
        #$python get_data.py -k config_db_uuid -c obj_fq_name_table -r virtual_network
        #$python get_data.py -k config_db_uuid -c obj_uuid_table -r row_key
        main(sys.argv[1:])





