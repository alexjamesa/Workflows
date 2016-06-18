#!/usr/bin/env python

import unittest
from Workflows import Seeker

class SeekerTests(unittest.TestCase):
 
    def setUp(self):
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

if __name__ == '__main__':
    unittest.main()