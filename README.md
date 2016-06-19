# Workflows
A command line utility to quickly search and display text files in Terminal. *Workflows* can work with any .txt file, but it's specially made for those files with a title on the top line and list of tags on the bottom line—see below for an example. Written in Python 2.7 with unit and integration tests.

### Example *Workflows* text file

	Creating a workflow text file
	
	1. Open up Sublime Text
	2. Add the workflow name to the top line
	3. Enter in the workflow steps on subsequent lines
	4. On the bottom line, add relevant tags in the format "Tags: workflow, steps, how-to"
	5. Save the file as <anything>.txt
	
	Tags: workflow, steps, how-to, meta

### Example usage
To return a list of text files in *TestWorkflows* that have "git" and "commit" in the name (i.e., the top line of the file):
		
	python Workflows.py TestWorkflows -n git commit 
	
To return a list of text files in *TestWorkflows* that have "git" in the name and a "workflow" tag:
		
	python Workflows.py TestWorkflows -n git -t workflow

Note: All directories within *TestWorkflows* will be searched in both cases.

### Options
* -n: name keywords
* -b: body keywords
* -t: tag keywords
* -w: wild keywords *(i.e., can appear anywhere)*
* -s: smart keywords *(can be anywhere, but matches in the name are weighted highest and matches in the body are weighted lowest)*
