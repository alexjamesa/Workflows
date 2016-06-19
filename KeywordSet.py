#!/usr/bin/env python

class KeywordSet:
	def __init__( self,keyword_string ):
		self.name = KeywordSet._arguments_for_option( keyword_string,'--n' )
		self.body = KeywordSet._arguments_for_option( keyword_string,'--b' )
		self.tags = KeywordSet._arguments_for_option( keyword_string,'--t' )
		self.wild = KeywordSet._arguments_for_option( keyword_string,'--w' )
		self.smart = KeywordSet._arguments_for_option( keyword_string,'--s' )

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

	@staticmethod
	def _arguments_for_option( arg_string,option ): # This could be more tidy
		i_option = arg_string.find(option)
		if i_option < 0:
			return []
		i_start = i_option + len(option)

		i_next_option = arg_string[i_start:].find(' -')
		i_end = i_next_option + i_start if i_next_option >= 0 else len(arg_string)
		if i_start >= i_end:
			return []

		return arg_string[i_start:i_end].strip().replace(","," ").split(" ")