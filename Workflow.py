#!/usr/bin/env python

class Workflow:
	def __init__( self, path, content ):
		self.name = 'Test Workflow';
		self.body = content;
		self.tags = 'Test tags';
		self.path = path;

	def __repr__(self):
		workflow_string = 'Workflow: ' + self.name;
		return workflow_string

	def as_menu_item( self,index ):
		return ' {0}. {1}'.format( index+1,self.name )

	def as_string( self ):
		return '# {0}\n\n{1}\n\nTags: {2}'.format( self.name,self.body,self.tags )