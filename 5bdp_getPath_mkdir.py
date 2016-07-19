#!/usr/bin/python
# coding: utf8

import sys
import time
import json
import requests
import MySQLdb

database = ""

if len(sys.argv) < 2 :
        print "please input the database name"

else:
        database = sys.argv[1]
        print "the database name is : " + database


headers = {'content-type': 'application/json'}

token = "b0a9b37da708bc8bf4e774c682d2e4a1"
url_data_import = '''http://172.20.4.142:2470/api/tb/import''' 
url_token = "?access_token=" + token
url_tb = "&tb_id="
#tab_id = "tb_02d38fc160cc4f5aa1a1bcd996e7b7df"
field = '''["id", "name", "age"]'''
url_field = "&fields="
get_path_enable = "&get_path=" + "1" 
get_path_false = "&get_path=" + "0" 
str_separator = "&separator=\,"

field = '''["id", "cnum", "ip"]'''


f_hdfs_mkdir = open('/tmp/hdfs_mkdir.txt', 'a')
f_hdfs_mv = open('/tmp/hdfs_mv.txt', 'a')

mysql_host      = '172.20.3.158'
mysql_port      = 3306
mysql_user      ='mysql'
mysql_passwd    = 'KangJia*mysql'
mysql_database_record = "test"

conn1= MySQLdb.connect(
        host    = mysql_host,
        port    = mysql_port,
        user    = mysql_user,
        passwd  = mysql_passwd,
        db      = mysql_database_record,
)

conn_dst = conn1.cursor()

sql = "select * from bdp_table_info1;"
ret = conn_dst.execute(sql)
for ii in conn_dst.fetchall():
	table_name = ii[3]
	table_id = ii[4]
	field = ii[6]
	url_import = url_data_import + url_token + url_tb + table_id + url_field + field + get_path_enable + str_separator
	print url_import
	
	r = requests.post(url_import)
	#print r.text
	ret_json = json.loads(r.text)
	path = ret_json["result"]
	print path
	sql_update_field = "update bdp_table_info1 set path='" + path + "' where tb_id='" + table_id + "';"
	print sql_update_field
	conn_dst.execute(sql_update_field)

	f_hdfs_mkdir.write("hadoop fs -mkdir -p " + path + "\n")
	f_hdfs_mv.write("hadoop fs -mv " + "/mysql_data/" + table_name + ".txt " + path + "\n")
	
	
