#!/usr/bin/env python

class KeywordSet:
	def __init__( self, keyword_inputs ):
		self.name = ['NameKey1','NameKey2'];
		self.body = ['BodyKey1','BodyKey2','BodyKey3'];
		self.tag = [];
		self.wild = ['WildKey1','WildKey2','WildKey3'];
		self.smart = ['SmartKey1'];

	def __repr__( self ):
		return 'KeywordSet:' + \
		'\n  name:  ' + ', '.join( self.name ) + \
		'\n  body:  ' + ', '.join( self.body ) + \
		'\n  tag:   ' + ', '.join( self.tag ) + \
		'\n  wild:  ' + ', '.join( self.wild ) + \
		'\n  smart: ' + ', '.join( self.smart );