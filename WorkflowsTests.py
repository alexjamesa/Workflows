#!/usr/bin/env python

import unittest
from Workflows import Seeker, Workflow

class SeekerTests( unittest.TestCase ):
 
    def setUp( self ):
        pass
 
    def test_that_it_returns_file_strings_for_known_directory( self ):
    	test_directory = "TestWorkflows/More"

    	actual = Seeker.file_strings( test_directory )
        
    	expected = {"TestWorkflows/More/workflow4.txt" : "Workflow #4 - Committing to GIT\n\n1. Commit something\n\n2. ??\n\nTags: GIT, commit, workflow, Fashion",
    				"TestWorkflows/More/workflow5.txt" : "Workflow #5 - Committing to GIT\n\n1. Commit something\n\n2. Commit again\n\nTags: GIT, commit, workflow, Fashion",
    				"TestWorkflows/More/Even more/workflow6.txt" : "Workflow #6 - Committing to GIT\n\n1. Commit something\n\n2. aoesthu\n\nTags: GIT, commit, workflow, Fashion"}
        self.assertEqual(actual, expected)


    def test_that_it_returns_nothing_for_unknown_directory( self ):
    	test_directory = "TestWorkflowsMore"

    	actual = Seeker.file_strings( test_directory )
        
    	expected = {}
        self.assertEqual(actual, expected)


class TestWorkflow(Workflow):
	def __init__( self,path,name,body,tags ):
		self.name = name
		self.body = body
		self.tags = tags
		self.path = path

class WorkflowTests( unittest.TestCase ):

	def setup( self ):
		pass

	def test_that_it_returns_expected_menu_item( self ):
		test_filename = "testpath.txt"
		test_content = "Title\nSome content\nMore content\nTags: Workflow, cat, horse" 
		test_workflow = Workflow( test_filename, test_content )
		test_index = 3

		actual = test_workflow.as_menu_item( test_index )

		expected = "3. Title"
		self.assertEqual(actual, expected)

	def test_that_it_returns_expected_string( self ):
		test_filename = "testpath.txt"
		test_content = "  Title  \n Some content\nMore content\n   Tags:Workflow, cat, horse   \n\n" 
		test_workflow = Workflow( test_filename, test_content )

		actual = test_workflow.as_string()

		expected = "Title\n\nSome content\nMore content\n\nTags: workflow, cat, horse" 
		self.assertEqual(actual, expected)

	def test_that_it_yields_workflow_with_expected_properties( self ):
		test_filename = "testpath.txt"
		test_content = "  Title  \n Some content\nMore content\n   Tags:Workflow, cat, horse   \n\n" 
		
		actual = Workflow( test_filename, test_content )

		expected = TestWorkflow( "testpath.txt","Title","Some content\nMore content","workflow, cat, horse" )
		self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()