#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, sys, os

class JsonPretty():
	"""docstring for JsonPretty"""
	def __init__(self, file_name):
		self.file_name = file_name
	
	def set_file_name(self, file_name):
		self.file_name = file_name

	def pretty_file(self):
		tmp_file = open('__tmp.json', 'w')

		for line in open(self.file_name, 'r'):
			req = json.loads(line)
			tmp_file.write( json.dumps( req, indent=2, separators=( ',', ':' ) ) + '\n')

		os.rename( self.file_name, ''.join( [ self.file_name , '.bak' ]))
		os.rename( '__tmp.json' , self.file_name )


def main():
	file_name = sys.argv[1]
	jsonpretty = JsonPretty(file_name)
	jsonpretty.pretty_file()

if __name__ == '__main__':
	main()