#!/usr/bin/env python

import os

class Seeker:

	@staticmethod
	def _text_filenames( txt_dir ):
		workflow_files = []
		for (dirpath, dirnames, all_filenames) in os.walk( txt_dir ):
			for filename in all_filenames:
				if filename.endswith(".txt"):
					workflow_filename = '%s/%s' % (dirpath,filename)
					workflow_files.append( workflow_filename )
		return workflow_files

	@staticmethod
	def _contents_of_file( txt_file ):
		with open(txt_file, 'r') as myfile:
			return myfile.read()

	@staticmethod
	def file_strings( txt_dir ):
		filenames = Seeker._text_filenames( txt_dir )
		file_strings = {}
		for filename in filenames:
			file_strings[filename] = Seeker._contents_of_file( filename )
		return file_strings
