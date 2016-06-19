#!/usr/bin/env python

import unittest
from Workflows import Seeker, Workflow, KeywordSet, Analyzer, parse_inputs, find_matches

class SeekerTests( unittest.TestCase ):
 
    def setUp( self ):
        pass
 
    def test_that_it_returns_file_strings_for_known_directory( self ):
    	test_directory = "TestWorkflows/More"

    	actual = Seeker.file_strings( test_directory )
        
    	expected = {"TestWorkflows/More/workflow4.txt" : "Workflow #4 - Committing to GIT\n\n1. Commit something\n\n2. ??\n\nTags: GIT, commit, workflow, Fashion",
    				"TestWorkflows/More/workflow5.txt" : "Workflow #5 - Committing to GIT\n\n1. Commit something\n\n2. Commit again\n\nTags: GIT, commit, workflow, Fashion",
    				"TestWorkflows/More/Even more/workflow6.txt" : "#6 - Committing to GIT variant\n\n1. Commit something\n\n2. aoesthu, land before time\n\nTags: GIT, commit, workflow, Fashion"}
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

	def test_that_it_returns_workflow_set( self ):
		test_filename1 = "testpath1.txt"
		test_content1 = "Title1\nSome content1\nTags: 1" 
		test_filename2 = "testpath2.txt"
		test_content2 = "Title2\nSome content2\nTags: 2" 
		file_strings = { test_filename1 : test_content1 , test_filename2 : test_content2 }

		actual = Workflow.workflows_for_filestrings( file_strings )

		expected = [TestWorkflow( "testpath2.txt", "Title2", "Some content2", "2"),
					TestWorkflow( "testpath1.txt", "Title1", "Some content1", "1")]
		self.assertEqual(actual,expected)



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

	def test_that_it_returns_valid_for_good_keywords( self ):
		keyword_set = KeywordSet( "-b blerv -w -s pineapple moose mouse -n git commit".split() )
		self.assertEqual(keyword_set.is_valid(), True)

	def test_that_it_returns_invalid_for_bad_keywords( self ):
		keyword_set = KeywordSet( "aoeu -b -w -s -n -t".split() )
		self.assertEqual(keyword_set.is_valid(), False)


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
		self.test_workflows = [self.test_xcodetrouble, self.test_xcodesetup, self.test_itunesconnect]
		

	def test_that_it_returns_workflows_for_name_only_keywords( self ):
		keyword_set = TestKeywordSet( ["troubleshoot"], [], [], [], [])
		workflows = Analyzer.workflows_for_keywords( keyword_set,self.test_workflows )
		self.assertEqual(len(workflows),1)
		self.assertEqual(workflows,[self.test_xcodetrouble])

	def test_that_it_returns_workflows_for_body_only_keywords( self ):
		keyword_set = TestKeywordSet( [], ["xcode"], [], [], [])
		workflows = Analyzer.workflows_for_keywords( keyword_set,self.test_workflows )
		self.assertEqual(len(workflows),1)
		self.assertEqual(workflows,[self.test_xcodesetup])

	def test_that_it_returns_workflows_for_tags_only_keywords( self ):
		keyword_set = TestKeywordSet( [], [], ["xcode"], [], [])
		workflows = Analyzer.workflows_for_keywords( keyword_set,self.test_workflows )
		self.assertEqual(len(workflows),2)
		self.assertEqual(workflows,[self.test_xcodesetup,self.test_xcodetrouble])

	def test_that_it_returns_workflows_for_wild_only_keywords( self ):
		keyword_set = TestKeywordSet( [], [], [], ["xcode","project"], [])
		workflows = Analyzer.workflows_for_keywords( keyword_set,self.test_workflows )
		self.assertEqual(len(workflows),1)
		self.assertEqual(workflows,[self.test_xcodesetup])

	def test_that_it_returns_workflows_for_smart_only_keywords( self ):
		keyword_set = TestKeywordSet( [], [], [], [], ["project"])
		workflows = Analyzer.workflows_for_keywords( keyword_set,self.test_workflows )
		self.assertEqual(len(workflows),2)
		self.assertEqual(workflows,[self.test_xcodesetup, self.test_itunesconnect])

	def test_that_it_returns_workflows_for_mixed_keywords( self ):
		keyword_set = TestKeywordSet( ["xcode"], [], ["project","workflow"], [], [])
		workflows = Analyzer.workflows_for_keywords( keyword_set,self.test_workflows )
		self.assertEqual(len(workflows),1)
		self.assertEqual(workflows,[self.test_xcodesetup])

	def test_that_it_returns_workflows_for_mixed_keywords_variant( self ):
		keyword_set = TestKeywordSet( ["project"], ["1."], [], ["open"], ["project"])
		workflows = Analyzer.workflows_for_keywords( keyword_set,self.test_workflows )
		self.assertEqual(len(workflows),2)
		self.assertEqual(workflows,[self.test_xcodesetup, self.test_itunesconnect])

	
class IntegrationTests( unittest.TestCase ):
	def setUp( self ):
		pass

	def test_that_it_returns_single_workflow_for_mixed_keywords( self ):
		argv = "Workflows TestWorkflows -n workflow -b land before time".split()
		workflow_dir, keywords = parse_inputs(argv[1:])
		actual = find_matches(workflow_dir, keywords)

		expected = [TestWorkflow( "TestWorkflows/workflow3.txt", \
			"Workflow #3 - More workflows re: computers variant", \
			"154323\n\n1. Buy computer\n\n2. Land before time\n\n3. Linux",
			"ubuntu, horse, cabbage, peacock, git" )]
		self.assertEqual(actual,expected)

	def test_that_it_returns_multiple_workflows_for_mixed_keywords( self ):
		argv = "Workflows TestWorkflows -n variant -b land before time -t git".split()
		workflow_dir, keywords = parse_inputs(argv[1:])
		actual = find_matches(workflow_dir, keywords)

		expected = [TestWorkflow( "TestWorkflows/More/Even more/workflow6.txt", \
				"#6 - Committing to GIT variant", \
				"1. Commit something\n\n2. aoesthu, land before time", \
				"git, commit, workflow, fashion" ), \
		TestWorkflow( "TestWorkflows/workflow3.txt", \
			"Workflow #3 - More workflows re: computers variant", \
			"154323\n\n1. Buy computer\n\n2. Land before time\n\n3. Linux",
			"ubuntu, horse, cabbage, peacock, git" )]
		self.assertEqual(len(actual),len(expected))
		self.assertEqual(actual[1],expected[1])


if __name__ == '__main__':
    unittest.main()


# FUTURE FEATURES:
#  - Make sure tied matches are sorted by name (e.g., sort by name first, then score)