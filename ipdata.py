#!/usr/bin python
# -*- coding: utf-8 -*-

import json

def ip_to_int(ip_addr):
    array = ip_addr.split('.')
    if len(array) != 4:
        error('ip_addr not valid.')
        return 0
    
    ans = reduce(lambda x, y: int(x)*256 + int(y), array)
    return ans


def int_to_ip(ip_int):
	array = ['0', '0', '0', '0']
	ipv4_i = 3
	while ip_int:
		array[ipv4_i] = str(ip_int % 256)
		ip_int /= 256
		ipv4_i -= 1
	return '.'.join(array)


class ipdata():
	"""store the info of os, browser, service 
	type and data size distribution belonging 
	to a specific ip address"""
	
	def __init__(self, ip_addr):
		"""
		Store the info of os, browser, service type and data size 
		distribution belonging to a specific ip address
		"""
	# super(ipdata, self).__init__()
		self.ip_addr = ip_addr
		self.os = {}
		self.browser = {}
		self.data_size = {}
		self.service = {}

	def __reqr__(self):
		return "ipdata()"

	def __str__(self):
		'''
		return the content of the ip object
		'''
		return json.dumps(
			{'ip_addr': int_to_ip(self.ip_addr),
			'os':self.os, 
			'browser':self.browser, 
			'data_size':self.data_size, 
			'service':self.service});
	
	def update(self, result):
		ans = True
		if 'os' not in result and 'browser' not in result:
			self.update_browser({'name':None})
			self.update_os({'name':None})
			return False

		try:
			self.update_os(result['os'])
		except Exception, e:
			# print 'Error:', e
			if e == KeyError:
				try:
					self.update_os(result['platform'])
				except Exception, e:
					if e == KeyError:
						self.update_os({'name':None})
					else:
						print 'Error:', e
						ans = False

		try:
			self.update_browser(result['browser'])
		except Exception, e:
			# print 'Error:', e
			if 'browser' not in result:
				if not self.special_browser(result):
					self.update_browser({'name':None})
					ans = False
		
		return ans


	def special_browser(self, result):
		if 'iOS' in result['os']['name'] or 'iOS' in result['platform']['name']:
			self.update_browser({'name':'Safari'})
			return True
		else:
			return False
		

			


	def update_os(self, os):
		if os['name'] not in self.os:
			self.os[os['name']] = 0
		self.os[os['name']] += 1

	def update_browser(self, browser):
		if browser['name'] not in self.browser:
			self.browser[browser['name']] = 0
		self.browser[browser['name']] += 1

	def update_data_size(self, data_size):
		if data_size not in self.data_size:
			self.data_size[data_size] = 0
		self.data_size[data_size] += 1

	def update_service(self, service_name):
		if service_name not in self.service:
			self.service[service_name] = 0
		self.service[service_name] += 1

