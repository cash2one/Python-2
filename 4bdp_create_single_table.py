#!/usr/bin/python

import requests


headers         = {'content-type': 'application/json'}
token = "b0a9b37da708bc8bf4e774c682d2e4a1 "
url_table_create = "http://172.20.4.142:2470/api/tb/create?access_token=" + token

table_json = '''{"uniq_key": [["numid"]], "ds_id": "ds_fedb39a951054775a0e30f6b15d0acc2", "name": "terminal_error_stack", "schema": [{"type": "number", "name": "numid"}, {"type": "number", "name": "counts"},{"type": "string", "name": "stack_info_md5"},{"type": "string", "name": "stack_info"}, {"type": "date", "name": "create_date"}]}'''

table_field = '''["numid", "counts", "stack_info_md5", "stack_info", "create_date"]'''

r = requests.post(url_table_create, data=str(table_json), headers=headers )
print r.text
