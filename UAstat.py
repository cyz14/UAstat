#!/usr/bin python
# -*- coding: utf-8 -*-

import sys
import json
import httpagentparser
import ipdata


def main():
	# print 'httpagentparser version', httpagentparser.__version__
	# print len(sys.argv)
	# raw_input()
	file_name = sys.argv[1]
	data_file = open(file_name, 'r')
	empty = 0
	hit   = 0
	for line in data_file:
		req = json.loads(line)
		if req["UserAgent"]:
			# print req["UserAgent"]
			hit += 1
			client_ip = ip_to_int(req['ClientIP'])
			# print req['ClientIP'], client_ip
			if int_to_ip(ip_to_int(req['ClientIP'])) != req['ClientIP']:
				print 'Error: function wrong'
				break
		else:
			empty += 1
	print empty, hit


def ip_to_int(ip_addr):
    array = ip_addr.split('.')
    if len(array) != 4:
        print 'Error: ip_addr not valid'
        return 0
    
    ans = 0
    for i in array:
        ans *= 256
        ans += int(i)
        
    return ans

def int_to_ip(ip_int):
	array = ['0', '0', '0', '0']
	ipv4_i = 3
	while ip_int:
		array[ipv4_i] = str(ip_int % 256)
		ip_int /= 256
		ipv4_i -= 1
	return '.'.join(array)

if __name__ == '__main__':
	main()