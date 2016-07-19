#!/usr/bin/python
# coding: utf8

import time
import json
import requests

#payload = {'a':'杨','b':'hello'}

headers = {'content-type': 'application/json'}

#r = requests.post("http://httpbin.org/post", data=payload)
#r = requests.post("http://httpbin.org/post", data=json.dumps(payload), headers=headers )

#r = requests.post("http://httpbin.org/post", data=str(payload), headers=headers )
#print r.text

#============================================================

#token = "acb69eaa0d5f3f12e9ad519f51a8a3f7"

#url_db_create = "http://172.20.4.142:2470/api/ds/create?access_token=acb69eaa0d5f3f12e9ad519f51a8a3f7&name=test_kj&type=opends"
#r = requests.post(url_db_create)

#url_db_delelte = "https://open.bdp.cn/api/ds/delete?access_token=acb69eaa0d5f3f12e9ad519f51a8a3f7&ds_id=acb69eaa0d5f3f12e9ad519f51a8a3f7"
#r = requests.post(url_db_delelte)

token = "b0a9b37da708bc8bf4e774c682d2e4a1"
url_db_list = "http://172.20.4.142:2470/api/ds/list?access_token=" + token
r = requests.post(url_db_list)
#print r.text

ret = json.loads(r.text)

if ret["status"] == "0":
	for ii in ret["result"]["data_source"] :
		print "database name: " + ii["name"] + "\t\t ds_id: " + ii["ds_id"]
else:
        print  ret["errstr"]


#str_json = '''{"name": "admin_manage_log","ds_id": "ds_fedb39a951054775a0e30f6b15d0acc2","schema": [{"name": "numid","type":"number"},{"name": "logtype","type":"number"},{"name": "username","type":"string"},{"name": "userrole","type":"string"},{"name": "action","type":"string"},{"name": "ip","type":"string"},{"name": "description","type":"string"},{"name": "create_date","type":"string"}],"uniq_key": ["numid"]}'''

#url_table_create = "http://172.20.4.142:2470/api/tb/create?access_token=acb69eaa0d5f3f12e9ad519f51a8a3f7"

#r = requests.post(url_table_create, data=str(str_json), headers=headers )
#print r.text


#f = open('json_source.txt', 'r')
#result = list()
#for line in f.readlines():
#        line = line.strip()
#	print line
#	r = requests.post(url_table_create, data=str(line), headers=headers )
#	
#	time.sleep(2)
#	print r.text
#

#url_data_import = '''http://172.20.4.142:2470/api/tb/import''' 
#url_token = "?access_token=acb69eaa0d5f3f12e9ad519f51a8a3f7"
#url_tb = "&tb_id=tb_02d38fc160cc4f5aa1a1bcd996e7b7df"
#field = '''["id", "name", "age"]'''
#url_field = "&fields=" + field 
#get_path_enable = "&get_path=" + "1" 
#get_path_false = "&get_path=" + "0" 
#str_separator = "&separator=\,"


#url_import = url_data_import + url_token + url_tb + url_field + get_path_enable + str_separator 
#print url_import
#r = requests.post(url_import)

