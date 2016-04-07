#!/usr/bin python
# -*- coding: utf-8 -*-

import json
# from pylab import *
from scipy import stats
import matplotlib.pyplot as plt
from CdfQuantiles import cdf_quantiles

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
		self.MIN_SAMPLE_RATE = 10

		self.ip_addr = ip_addr	# here ip_addr is integer

		# in request.UserAgent, from httpagentparser.detect()
		self.os = {}				
		self.browser = {}
		self.service = {}

		# in session
		self.rtt_list = []			# Rtt
		self.retransrate = 0		# retransmit rate

		# in session.LatencyInfo
		self.latency_list = []		# .TcpLatency
		self.data_size_list = []	# .TransDataSize
		self.timeout = 0			# .TimeOut


	def __reqr__(self):
		return "ipdata()"

	def __str__(self):
		'''
		return the content of the ip
		'''
		ans = {
			'ip_addr':int_to_ip(self.ip_addr),
			'os':self.os,
			'browser':self.browser,
			'service':self.service,
			'retransrate':1.0 * self.retransrate / self.session_number(),	# average
			'timeout':1.0 * self.timeout / self.session_number(),	# average
			}
		if self.session_number() >= self.MIN_SAMPLE_RATE:
			ans['rtt'] 		= cdf_quantiles(self.rtt_list)
			ans['latency'] 	= cdf_quantiles(self.latency_list)
			ans['data_size']= cdf_quantiles(self.data_size_list)
		else:
			ans['rtt']		= self.rtt_list
			ans['latency']  = self.latency_list
			ans['data_size']= self.data_size_list

		return json.dumps(ans)

	def session_number(self):
		return len(self.rtt_list)

	def set_min_sample_rate(size):
		self.MIN_SAMPLE_RATE = size

	def update_os_browser(self, result):
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

	def update_service(self, service_name):
		if service_name not in self.service:
			self.service[service_name] = 0
		self.service[service_name] += 1

	def update_data_size(self, data_size):
		self.data_size_list.append(data_size)

	def update_rtt(self, rtt):
		self.rtt_list.append(rtt)

	def update_latency(self, latency):
		self.latency_list.append(latency)

	def update_from_session(self, ses):
		self.update_rtt(ses['Rtt'])
		for info in ses['LatencyInfo']:			
			self.update_latency(info['TcpLatency'])
			self.update_data_size(ses['TransmitSize'])
