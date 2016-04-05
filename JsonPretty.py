#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, os

class JsonPretty(object):
	"""docstring for JsonPretty"""
	def __init__(self, file_name):
		self.file_name = file_name
	
	def set_file_name(self, file_name):
		self.file_name = file_name

	def pretty_file(self):
		tmp_file = open('.tmp.json', 'w')

		for line in open(self.file_name, 'r'):
			req = json.loads(line)
			tmp_file.write( json.dumps(req, separators=(',', ':')) + '\n')

		# os.rename(self.file_name, '_' + self.file_name)
		# os.rename('.tmp.json', self.file_name)


if __name__ == '__main__':
	main()