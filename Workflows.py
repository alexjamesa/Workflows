#!/usr/bin/env python

import sys
from Seeker import Seeker
from Workflow import Workflow
from Analyzer import Analyzer
from KeywordSet import KeywordSet

def main():	
	# Process inputs
	workflow_dir, keywords = parse_inputs(sys.argv[1:])
	matches = find_matches(workflow_dir, keywords)

	# Print menu for user
	print_menu( matches )
	selected_workflow = prompt_for_workflow( matches )

	# Display selected workflow
	print('\n\nWORKFLOW:\n-------------------')
	print( selected_workflow.as_string() )
	print('-------------------\n\n')

def parse_inputs( argv ):
	if len(argv) < 2:
		print("   > At least two inputs required")
		sys.exit()
	elif len(argv) == 2:
		workflow_dir = ""
	else:
		workflow_dir = argv[0]
	keywords = argv[1:]
	return workflow_dir, keywords

def find_matches( workflow_dir,keywords ):
	workflows = Workflow.workflows_for_filestrings( Seeker.file_strings( workflow_dir ) )
	keyword_set = KeywordSet( keywords )
	if keyword_set.is_valid() == False:
		print("   > Invalid keywords")
		sys.exit()
	return Analyzer.workflows_for_keywords( keyword_set,workflows )

def print_menu( workflows ):
	workflow_count = len(workflows)
	print("\n")
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