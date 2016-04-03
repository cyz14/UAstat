#!/usr/bin python
# -*- coding: utf-8 -*-

import sys
import json
from httpagentparser import detect
from ipdata import *

def error(error_info):
	print 'Error:', error_info
	return

ip_db = {}


def main():
	if len(sys.argv) < 2:
		error('No input file.')
		return -1
	
	file_name = sys.argv[1]
	work(file_name)


def work(file_name):
	data_file = open(file_name, 'r')
	if not data_file:
		error('File not opened.')
		return -1
	
	log = open('req.log', 'w')

	empty = 0
	hit   = 0
	for line in data_file:
		req = json.loads(line)
		if req["UserAgent"]:
			hit += 1
			client_ip = ip_to_int(req['ClientIP'])
			result = detect(req['UserAgent'])
			ip_db[client_ip] = ipdata(client_ip)
			if not ip_db[client_ip].update(result):
				log.write(req['UserAgent'] + '\n' + str(result) + '\n\n')

			ip_db[client_ip].update_data_size(req["BodyLen"])
			ip_db[client_ip].update_service(req["ServiceName"])
			
		else:
			empty += 1
	print empty, hit
	write_stat(ip_db)
	log.close()
	data_file.close()


def write_stat(db, file_name='stat.json'):
	stat_file = open(file_name, 'w')
	for ip_entry in db:
		stat_file.write(str(db[ip_entry])+'\n')

	stat_file.close()



if __name__ == '__main__':
	main()



