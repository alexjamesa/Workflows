# Workflows
A command line utility in Python to search and display text files. Tailored to text files with three sections: 
* name: top line
* tags: last line, starting with "Tags:"
* body: everything in between

## Example usage
To returns a list of text files in SearchDirectory that have "git" and "commit" in the name (i.e., the top line):
	Workflows SearchDirectory -n git commit 