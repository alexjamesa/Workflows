#!/usr/bin/env python

class Workflow:
	def __init__( self, path, content ):
		self.name = Workflow._name_for_content( content )
		self.body = Workflow._body_for_content( content )
		self.tags = Workflow._tags_for_content( content )
		self.path = path

	def __repr__(self):
		workflow_string = 'Workflow: ' + self.name;
		return workflow_string

	def __eq__( self, other ):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	@staticmethod
	def workflows_for_filestrings( file_strings ):
		workflows = []
		for filename, file_string in file_strings.items():
			workflows.append( Workflow(filename, file_string) )
		return workflows

	@staticmethod
	def _name_for_content( content ):
		return content.strip("\n").split("\n")[0].strip()

	@staticmethod
	def _tags_for_content( content ):
		i_tags = content.lower().rfind("tags:")
		return content[i_tags+5:].strip("\n").strip().lower()

	@staticmethod
	def _body_for_content( content ):
		i_after_title = content.strip("\n").find("\n")
		i_tags = content.lower().rfind("tags:")
		return content[i_after_title:i_tags].strip("\n").strip()

	def as_menu_item( self,index ):
		return '{0}. {1}'.format( index,self.name )

	def as_string( self ):
		return '{0}\n\n{1}\n\nTags: {2}'.format( self.name,self.body,self.tags )