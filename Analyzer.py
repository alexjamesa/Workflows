#!/usr/bin/env python

class Analyzer:
	def __init__( self, workflows ):
		self._workflows = workflows;

	def __repr__(self):
		return 'Analyzer: %d workflows' % len(self._workflows);

	def workflows_for_keywords( self,keyword_set ):
		return self._workflows[:2];