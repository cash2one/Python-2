#!/usr/bin/python
# coding: utf8

import sys
import time
import datetime
import json
#import simplejson
import requests
import MySQLdb

import re

#file_table_name_id	= "/tmp/table_name_id_map.txt"

mysql_host      = '172.20.3.158'
mysql_port      = 3306
mysql_user      ='mysql'
mysql_passwd    = 'KangJia*mysql'
#mysql_database  = 'KKUSER'
mysql_database  = 'KKSTATISTIC'

mysql_database_record = "test"

token = "b0a9b37da708bc8bf4e774c682d2e4a1 "
url_table_create= "http://172.20.4.142:2470/api/tb/create?access_token=" + token
headers 	= {'content-type': 'application/json'}
#ds_id		= "ds_fedb39a951054775a0e30f6b15d0acc2"
#ds_id		= "ds_0a99df7b62ea4de8be124d505b4aaf91"
#ds_id		= "ds_cf3f7e49f52641e188038881626dc0f7"

ds_id = ""

if len(sys.argv) < 2 :
    	print "please input the ds_id"
	exit()
else:
	ds_id = sys.argv[1]
	print "the ds_id is : " + ds_id

db_name = sys.argv[1]
url_db_list = "http://172.20.4.142:2470/api/ds/list?access_token=" + token
r = requests.post(url_db_list)
#print r.text


ret = json.loads(r.text)

if ret["status"] == "0":
        for ii in ret["result"]["data_source"] :
		if ii["name"] == db_name:
                	print "database name: " + ii["name"] + "\t\t ds_id: " + ii["ds_id"]
			ds_id = ii["ds_id"]
else:
        print  ret["errstr"]

####################################################################

#f_table_name_id = open(file_table_name_id,'a')

conn1= MySQLdb.connect(
        host    = mysql_host,
        port    = mysql_port,
        user    = mysql_user,
        passwd  = mysql_passwd,
        db      = mysql_database_record,
)

conn_dst = conn1.cursor()


conn2= MySQLdb.connect(
        host    = mysql_host,
        port    = mysql_port,
        user    = mysql_user,
        passwd  = mysql_passwd,
        db      = mysql_database,
)

conn_src = conn2.cursor()
sql_show_table = "show tables;"

conn_src.execute(sql_show_table)


ret = conn_src.fetchall()
for ii in ret:
        print "\n=========================="

	table_dict = {
	        "name": "",
	        "ds_id": ds_id,
	        "schema": [],
	        "uniq_key": ["numid"]
	}

	
	field_dict = []

        table_name = ii[0]
	
	#'''
	if table_name == "terminal_error_stack":
		print "create single table: " + table_name
		
	else:
		print "11111111111111"
		continue
	#'''

	table_dict["name"] = table_name

        sql_des_table = "desc " + ii[0]
        conn_src.execute(sql_des_table)

        for field in conn_src.fetchall():
		# field[1] 表示desc table1 的第二列中的某个字段
		field_dict.append(field[0])
		print field
		ret1 = field[1].find("int")
                if ret1 == 0 :
                        #print field[1] + " match int successful"
                        test = {
                                "name": field[0],
                                "type": "number"
			}

			table_dict.get("schema").append(test)


                ret2 = field[1].find("char")
                if ret2 == 0 :
                        #print field[1] + " match varchar successful"

                        test = {
                                "name": field[0],
                                "type": "string"
                        }

                        table_dict.get("schema").append(test)

                ret3 = field[1].find("timestamp")
                if ret3 == 0 :
			#print field[1] + " match timestamp successful"

                        test = {
                                "name": field[0],
                                "type": "date"
                        }

                        table_dict.get("schema").append(test)

                ret3 = field[3].find("PRI")
                if ret3 == 0 :
                        table_dict.get("uniq_key")[0] = [field[0]]

                ret4 = field[1].find("text")
                if ret4 == 0 :
                        #print field[1] + " match varchar successful"

                        test = {
                                "name": field[0],
                                "type": "string"
                        }

                        table_dict.get("schema").append(test)

		table_json = json.dumps(table_dict)
		table_field = json.dumps(field_dict)
	print table_json
	print table_field

	r = requests.post(url_table_create, data=str(table_json), headers=headers )
	print r.text
 
	ret = json.loads(r.text)
	if ret["status"] == "0":
		#f_table_name_id.write(ds_id + "|" + table_name + "|" + ret["result"]["tb_id"] + "\n")
		tb_id = ret["result"]["tb_id"]
		print tb_id
		sql_record_update = "insert into bdp_table_info1 (`db_name`, `ds_id`, `table_name`, `tb_id`, `field` ) VALUES ('" + db_name  + "','" + ds_id + "','" + table_name  + "','" + tb_id + "','" + table_field + "');"
		print sql_record_update
		conn_dst.execute(sql_record_update)
	else:
		print  ret["errstr"]

	#f_table_name_id.write(table_json + '\n')

	#break

#f_table_name_id.write("################" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "################\n")
#f_table_name_id.close()


