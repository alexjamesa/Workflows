#!/usr/bin/env python

import sys
from Seeker import Seeker
from Workflow import Workflow
from Analyzer import Analyzer
from KeywordSet import KeywordSet

workflow_dir = "/TestWorkflows"

def main():
	
	# Find matching workflows
	file_strings = Seeker.file_strings(workflow_dir)
	workflows = []
	for filename, file_string in file_strings.items():
		workflows.append(Workflow(filename, file_string))
	analyzer = Analyzer(workflows)
	keyword_set = KeywordSet( sys.argv[1:] )
	matches = analyzer.workflows_for_keywords(keyword_set)

	# Print menu for user
	workflow_count = len(matches)
	print('')
	for i, workflow in enumerate(matches):
		print(workflow.as_menu_item( i ))
	selected_workflow_index = int(raw_input('\n > Select workflow ({0}-{1}): '.format(1,workflow_count))) - 1
	if selected_workflow_index < 0 or selected_workflow_index >= workflow_count:
		print( '   > Sorry! Bad selection, must be between {0} and {1}'.format(1,workflow_count) )
		sys.exit()

	# Display chosen workflow
	print('\n-------------------')
	print( matches[selected_workflow_index].as_string() )
	print('-------------------\n')

if __name__ == '__main__':
	main()