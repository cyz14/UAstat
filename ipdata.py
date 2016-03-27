class ipdata():
	"""store the info of os, browser, service 
	type and data size distribution belonging 
	to a specific ip address"""
	
	def __init__(self, ip_addr):
	#	super(ipdata, self).__init__()
		self.ip_addr = ip_addr
		self.os = {}
		self.browser = {}
		self.data_size = {}
		self.service = {}
		
	
	def update_os(os):
		pass

	def update_browser(browser):
		pass

	def update_data_size(size):
		pass

	def update_service(service):
		pass