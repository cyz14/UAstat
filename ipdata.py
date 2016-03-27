class ipdata():
	"""store the info of os, browser, service type and data size 
	distribution belonging to a specific ip address"""
	def __init__(self, ip_addr):
		self.ip_addr = ip_addr
		self.os = {}
		self.browser = {}
		self.data_size = {}
		self.service = {}
	
	
	def update(self, result):
		update_os(self, result['os'])

	def update_os(self, os_name):
		if not self.os[os_name]:
			self.os[os_name] = 0
		self.os[os_name] += 1

	def update_browser(self, browser_name):
		if not self.browser[browser_name]:
			self.browser[browser_name] = 0
		self.browser[browser_name] += 1

	def update_data_size(self, data_size):
		if not self.data_size[data_size]:
			self.data_size[data_size] = 0
		self.data_size[data_size] += 1

	def update_service(self, service):
		if not self.service[service];
			self.service[service] = 0
		self.service[service] += 1