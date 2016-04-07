#!/usr/bin python
# -*- coding: utf-8 -*-

import sys, getopt
import json
from httpagentparser import detect
from MergeSesReq import *
from ipdata import *
import numpy as np


ip_db = {}
log = open('req.log', 'w')

def error(error_info):
	print 'Error:', error_info
	return

def main():
	if len(sys.argv) < 2:
		error('No input file.')
		return -1
	
	file_name = sys.argv[1]
	work(file_name)
	write_stat(ip_db)


def process_request(req):
	"""
	update os, browser and service under ip
	"""
	client_ip = ip_to_int(req['ClientIP'])
	result = detect(req['UserAgent'])
	if client_ip not in ip_db:
		ip_db[client_ip] = ipdata(client_ip)
	# else ipdata(client_ip) already in ip_db

	if not ip_db[client_ip].update_os_browser(result):
		log.write(req['UserAgent'] + '\n' + str(result) + '\n\n')

	# ip_db[client_ip].update_data_size(req["BodyLen"])
	ip_db[client_ip].update_service(req["ServiceName"])


def process_session(ses):
	"""
	update rtt, retransrate, latencyinfo{ latency, data_size, timeout}
	"""
	client_ip = ip_to_int(ses['ClientIP'])
	
	if client_ip not in ip_db:
		ip_db[client_ip] = ipdata(client_ip)

	ip_db[client_ip].update_from_session(ses)


def deal_merged_file(file_name='session.request.json'):
	fin = open(file_name, 'r')
	if not fin:
		error('Error: Merged file not opened.')
		return

	for index, line in enumerate(fin):
		Log = json.loads(line)
		Reqs = Log['ReqLog']
		for req in Reqs:
			process_request(req)

		Ses = Log['SesLog']
		# print Ses['LatencyInfo'], type(Ses['LatencyInfo'])
		# if raw_input().lower().startswith('q'):
		# 	return
		process_session(Ses)

	fin.close()


def work(file_name):
	# deal_session_file()
	# deal_request_file()
	deal_merged_file(file_name)
	

def write_stat(db, file_name='stat.json'):
	stat_file = open(file_name, 'w')
	for ip_entry in db:
		stat_file.write(str(db[ip_entry])+'\n')

	stat_file.close()


if __name__ == '__main__':
	main()


def deal_request_file(file_name='request.json'):
	data_file = open(file_name, 'r')
	if not data_file:
		error('File not opened.')
		return -1

	empty = 0
	hit   = 0
	for line in data_file:
		req = json.loads(line)
		if req["UserAgent"]:
			hit += 1
			process_request(req)
		else:
			empty += 1
	print empty, hit
	
	data_file.close()
	return


def deal_session_file(file_name='session.json'):
	data_file = open(file_name, 'r')
	if not data_file:
		error('File not opened.')
		return -1

	for line in data_file:
		ses = json.loads(line)
		ses_id = ip_to_int(ses['ClientIP'])
		rtt = ses['Rtt']
		if ses_id not in ip_db:
			ip_db[ses_id] = ipdata(client_ip)
