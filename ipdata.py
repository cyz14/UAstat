
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
	
	def update(self, result):
		self.update_os(result['os'])
		self.update_browser(result['browser'])
		

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
