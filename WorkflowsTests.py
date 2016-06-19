#!/usr/bin/env python

import unittest
from Workflows import Seeker, Workflow, KeywordSet, Analyzer

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
	def setUp( self ):
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


class TestKeywordSet(KeywordSet):
	def __init__( self,name,body,tags,wild,smart ):
		self.name = name
		self.body = body
		self.tags = tags
		self.wild = wild
		self.smart = smart


class KeywordSetTests( unittest.TestCase ):
	def setUp( self ):
		pass

	def test_that_it_yields_multiple_name_keywords( self ):
		actual = KeywordSet( ["-n","git","commit"] )
		expected = TestKeywordSet( ["git","commit"], [], [], [], [])
		self.assertEqual(actual,expected)

	def test_that_it_yields_multiple_body_keywords( self ):
		actual = KeywordSet( ["-b","git","commit"] )
		expected = TestKeywordSet( [], ["git","commit"], [], [], [])
		self.assertEqual(actual,expected)

	def test_that_it_yields_multiple_tag_keywords( self ):
		actual = KeywordSet( ["-t","git","commit"] )
		expected = TestKeywordSet( [], [], ["git","commit"], [], [])
		self.assertEqual(actual,expected)

	def test_that_it_yields_multiple_wild_keywords( self ):
		actual = KeywordSet( ["-w","git","commit"] )
		expected = TestKeywordSet( [], [], [], ["git","commit"], [])
		self.assertEqual(actual,expected)

	def test_that_it_yields_multiple_smart_keywords( self ):
		actual = KeywordSet( ["-s","git","commit"] )
		expected = TestKeywordSet( [], [], [], [], ["git","commit"] )
		self.assertEqual(actual,expected)

	def test_that_it_yields_all_expected_keywords( self ):
		actual = KeywordSet( "-n git commit -w hats -s pineapple moose mouse -t xcode -b blerv".split() )
		expected = TestKeywordSet( ["git","commit"], ["blerv"], ["xcode"], ["hats"], ["pineapple","moose","mouse"])
		self.assertEqual(actual,expected)

	def test_that_it_yields_all_expected_keywords_variant( self ):
		actual = KeywordSet( "-b blerv -w -s pineapple moose mouse -n git commit".split() )
		expected = TestKeywordSet( ["git","commit"], ["blerv"], [], [], ["pineapple","moose","mouse"])
		self.assertEqual(actual,expected)


class AnalyzerTests( unittest.TestCase ):
	def setUp( self ):
		self.test_xcodetrouble = TestWorkflow( "testpath1.txt",\
			"Troubleshooting Xcode",\
			"1. Restart the app\n2. Cross your fingers",\
			"xcode, troubleshoot, workflow, " )
		self.test_xcodesetup = TestWorkflow( "testpath2.txt",\
			"Setting up a project in Xcode",\
			"1. Open Xcode\n2. Press New\n3. etc.",\
			"workflow, xcode, new, project" )
		self.test_itunesconnect = TestWorkflow( "testpath3.txt",\
			"A new project in iTunes Connect",\
			"1. Open your web browser\n2. Go to itunesconnect.?\n3. Start a project",\
			"workflow, safari, itunes, connect" )
		test_workflows = [self.test_xcodetrouble, self.test_xcodesetup, self.test_itunesconnect]
		self.analyzer = Analyzer( test_workflows )

	def test_that_it_returns_workflows_for_name_only_keywords( self ):
		keyword_set = TestKeywordSet( ["troubleshoot"], [], [], [], [])
		workflows = self.analyzer.workflows_for_keywords( keyword_set )
		self.assertEqual(len(workflows),1)
		self.assertEqual(workflows,[self.test_xcodetrouble])

	def test_that_it_returns_workflows_for_body_only_keywords( self ):
		keyword_set = TestKeywordSet( [], ["xcode"], [], [], [])
		workflows = self.analyzer.workflows_for_keywords( keyword_set )
		self.assertEqual(len(workflows),1)
		self.assertEqual(workflows,[self.test_xcodesetup])

	def test_that_it_returns_workflows_for_tags_only_keywords( self ):
		keyword_set = TestKeywordSet( [], [], ["xcode"], [], [])
		workflows = self.analyzer.workflows_for_keywords( keyword_set )
		self.assertEqual(len(workflows),2)
		self.assertEqual(workflows,[self.test_xcodesetup,self.test_xcodetrouble])

	def test_that_it_returns_workflows_for_wild_only_keywords( self ):
		keyword_set = TestKeywordSet( [], [], [], ["xcode","project"], [])
		workflows = self.analyzer.workflows_for_keywords( keyword_set )
		self.assertEqual(len(workflows),1)
		self.assertEqual(workflows,[self.test_xcodesetup])

	def test_that_it_returns_workflows_for_smart_only_keywords( self ):
		keyword_set = TestKeywordSet( [], [], [], [], ["project"])
		workflows = self.analyzer.workflows_for_keywords( keyword_set )
		self.assertEqual(len(workflows),2)
		self.assertEqual(workflows,[self.test_xcodesetup, self.test_itunesconnect])

	def test_that_it_returns_workflows_for_mixed_keywords( self ):
		keyword_set = TestKeywordSet( ["xcode"], [], ["project","workflow"], [], [])
		workflows = self.analyzer.workflows_for_keywords( keyword_set )
		self.assertEqual(len(workflows),1)
		self.assertEqual(workflows,[self.test_xcodesetup])

	def test_that_it_returns_workflows_for_mixed_keywords_variant( self ):
		keyword_set = TestKeywordSet( ["project"], ["1."], [], ["open"], ["project"])
		workflows = self.analyzer.workflows_for_keywords( keyword_set )
		self.assertEqual(len(workflows),2)
		self.assertEqual(workflows,[self.test_xcodesetup, self.test_itunesconnect])

	# NT: Integration tests, error cases for inputs (like if no options, or just options)

if __name__ == '__main__':
    unittest.main()


# FUTURE FEATURES:
#  - Make sure tied matches are sorted by name (e.g., sort by name first, then score)