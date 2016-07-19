#!/usr/bin/python
# coding: utf8

import time
import json
import requests
import MySQLdb


headers = {'content-type': 'application/json'}
url_data_import = '''http://172.20.4.142:2470/api/tb/import''' 
url_token = "?access_token=acb69eaa0d5f3f12e9ad519f51a8a3f7"
url_tb = "&tb_id="
tab_id = "tb_02d38fc160cc4f5aa1a1bcd996e7b7df"
url_field = "&fields="
get_path_enable = "&get_path=" + "1" 
get_path_false = "&get_path=" + "0" 
str_separator = "&separator=\,"

field = '''["id", "name", "age"]'''


conn= MySQLdb.connect(
        host='172.20.3.158',
        port = 3306,
        user='root',
        passwd='zP3zqx',
        db ='test',
        )

cur = conn.cursor()

#ret = cur.execute("use test;");
#ret = cur.execute("show databases;");
#ret = cur.execute("show tables;");

#ret = cur.execute("select * from bdp_table_info where name='adv_log';");
#for ii in cur.fetchall():
#       print "====" + ii[0] + "====="

#        print "1111111111"
#        print ii[3]


#url_import = url_data_import + url_token + url_tb + url_field + get_path_enable + str_separator 
#print url_import
#r = requests.post(url_import)

i=0
#f = open('table_id_new.txt', 'r')
#f = open('table_id_field_2.txt', 'r')

#f = open('table_id_field_to_import.txt', 'r')
f = open('table_all.txt', 'r')
for line in f.readlines():
	#i += 1
	#if(i<=3):
	#	continue

	#str_id_field = line.split('|')
	
	table = line.strip()

        #print str_id_field[0] + "====" + str_id_field[1]
	#print line
	#print "seq: " + str(i) + " table name: " + str_id_field[0].strip()
	#table = str_id_field[0].strip()
	#line = str_id_field[1].strip()
	#field = str_id_field[2].strip()
	
	sql = "select * from bdp_table_info where name='" + table + "';"
	ret = cur.execute(sql)
	for ii in cur.fetchall():
		tab_id = ii[2]	
		path = ii[3]
		field = ii[4]
		enable = ii[5]

	if int(enable) == 0 :
		print "\nhadoop fs -cp /mysql_data/" + table + ".txt " + path
		#'''
		print "===============the table %s is importing==========" % (table)
		url_import = url_data_import + url_token + url_tb + tab_id + url_field + field + get_path_false + str_separator
		print url_import
		r = requests.post(url_import)
        	print r.text

		sql_update = "update bdp_table_info set enable=1 where name='" + table + "';"
		print sql_update

		#'''		
		i += 1
		if (i>10):
			break
		
	else:
		print "the table %s had import" % (table)
		#rint "\n" + sql + " |||| " + path

        #line = line.strip()
        #r = requests.post(url_table_create, data=str(line), headers=headers )
	
#	sql_update = "update bdp_table_info set enable=1 where name='" + table + "';"
#	ret = cur.execute(sql)
#	print ret
#	print sql_update
	

	#break
        #time.sleep(2)

