#!/usr/bin/env python

import sys
from Seeker import Seeker
from Workflow import Workflow
from Analyzer import Analyzer
from KeywordSet import KeywordSet

workflow_dir = "TestWorkflows"

def main():	
	
	# Find matching workflows
	workflows = find_workflows()
	keyword_set = KeywordSet( sys.argv[1:] )
	matches = find_matches( workflows, keyword_set )

	# Print menu for user
	print('\n\nKEYWORDS:')
	print(keyword_set)
	print_menu( matches )
	selected_workflow = prompt_for_workflow( matches )

	# Display chosen workflow
	print('\n\n-------------------')
	print( selected_workflow.as_string() )
	print('-------------------\n\n')

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

def print_menu( workflows ):
	workflow_count = len(workflows)
	if workflow_count == 0:
		print('No workflows found!\n')
		sys.exit()
	print('MENU:')
	for i, workflow in enumerate(workflows):
		print(workflow.as_menu_item( i+1 ))

def prompt_for_workflow( workflows ):
	workflow_count = len(workflows)
	user_input = raw_input('   > Select workflow ({0}-{1}, q): '.format(1,workflow_count))
	if user_input == 'q':
		print('   > Bye!\n')
	elif user_input.isdigit() == False:
		print('   > Bad input! Please try again with a number between {0} and {1}\n'.format(1,workflow_count))
	elif (1 <= int(user_input) <= workflow_count) == False:
		print( '   > Sorry! Bad selection, must be between {0} and {1}\n'.format(1,workflow_count) )
	else:
		return workflows[int(user_input) - 1]
	sys.exit()

if __name__ == '__main__':
	main()