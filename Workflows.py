#!/usr/bin/env python

import sys
from Seeker import Seeker
from Workflow import Workflow
from Analyzer import Analyzer
from KeywordSet import KeywordSet

workflow_dir = "/TestWorkflows"

def main():	
	# Find matching workflows
	workflows = find_workflows()
	keyword_set = KeywordSet( sys.argv[1:] )
	matches = find_matches( workflows, keyword_set )

	# Print menu for user
	selected_workflow = prompt_for_workflow( matches )

	# Display chosen workflow
	print('\n-------------------')
	print( selected_workflow.as_string() )
	print('-------------------\n')

def find_workflows():
	file_strings = Seeker.file_strings(workflow_dir)
	workflows = []
	for filename, file_string in file_strings.items():
		workflows.append(Workflow(filename, file_string))
	return workflows

def find_matches( workflows, keyword_set ):
	analyzer = Analyzer(workflows)
	matches = analyzer.workflows_for_keywords(keyword_set)
	return matches

def prompt_for_workflow( workflows ):
	workflow_count = len(workflows)
	print('')
	for i, workflow in enumerate(workflows):
		print(workflow.as_menu_item( i ))
	selected_workflow_index = int(raw_input('\n > Select workflow ({0}-{1}): '.format(1,workflow_count))) - 1
	if selected_workflow_index < 0 or selected_workflow_index >= workflow_count:
		print( '   > Sorry! Bad selection, must be between {0} and {1}'.format(1,workflow_count) )
		sys.exit()
	return workflows[selected_workflow_index]

if __name__ == '__main__':
	main()