#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, sys, os

class JsonPretty():
	"""docstring for JsonPretty"""
	def __init__(self, file_name, indent = 2, bak = False):
		self.file_name = file_name
		self.set_indent(indent)
		self.bak = bak
	
	def set_file_name(self, file_name):
		self.file_name = file_name

	def set_indent(self, indent):
		self.indent = indent

	def pretty_file(self):
		ori_file = open(self.file_name, 'r')
		tmp_file = open('__tmp.json', 'w')

		for line in ori_file:
			req = json.loads(line)
			tmp_file.write( json.dumps( req, indent=self.indent, separators=( ',', ':' ) ) + '\n')

		ori_file.close()
		if self.bak:
			os.rename( self.file_name, self.file_name + '.bak' )
		else:
			os.remove(self.file_name)

		tmp_file.close()
		os.rename( '__tmp.json' , self.file_name )


def main():
	file_name = sys.argv[1]
	jsonpretty = JsonPretty(file_name)
	jsonpretty.pretty_file()

if __name__ == '__main__':
	main()