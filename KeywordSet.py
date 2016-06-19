#!/usr/bin/env python

class KeywordSet:
	def __init__( self,keyword_args ):
		self.name = KeywordSet._arguments_for_option( keyword_args,'-n' )
		self.body = KeywordSet._arguments_for_option( keyword_args,'-b' )
		self.tags = KeywordSet._arguments_for_option( keyword_args,'-t' )
		self.wild = KeywordSet._arguments_for_option( keyword_args,'-w' )
		self.smart = KeywordSet._arguments_for_option( keyword_args,'-s' )

	def __repr__( self ):
		return ('> name:  ' + ', '.join( self.name ) + '\n' if len(self.name) > 0 else "") +\
		('> body:  ' + ', '.join( self.body ) + '\n' if len(self.body) > 0 else "") +\
		('> tags:  ' + ', '.join( self.tags ) + '\n' if len(self.tags) > 0 else "") +\
		('> wild:  ' + ', '.join( self.wild ) + '\n' if len(self.wild) > 0 else "") +\
		('> smart: ' + ', '.join( self.smart ) + '\n' if len(self.smart) > 0 else "")

	def __eq__( self, other ):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		else:
			return False

	def is_valid( self ):
		total_keywords = len(self.name + self.body + self.tags + self.wild + self.smart)
		return total_keywords > 0

	@staticmethod
	def _arguments_for_option( args,option ): # This could be more tidy
		these_args = []
		in_arg = False 
		for arg in args:
			if arg == option:
				in_arg = True
			elif in_arg == True:
				if arg.startswith("-"):
					break
				these_args.append(arg)
		return these_args