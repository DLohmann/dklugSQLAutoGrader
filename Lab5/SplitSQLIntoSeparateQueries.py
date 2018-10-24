#!/usr/bin/env python

import re #regex for removing comments

# comment_remover(text) was modified from: https://stackoverflow.com/questions/241327/python-snippet-to-remove-c-and-c-comments
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return " " # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)

#takes out all comments from a file, using regex

def remove_line_comments (str):
	#newStr = re.sub(str, "--.+\n|--.+\z", "")	# remove any single line comments, including any comment at the end of the file
	# newStr = re.sub(str,    "--.+\n", "")	# remove all single line comments
	# newStr = re.sub(newStr, "--.+\z", "")	# remove any single line comment at the end of file
	# newStr = re.sub(newStr, "", "")	# remove all multi-line comments
	# /\*[a-zA-Z0-9\ ]+ \*/
	#lineCommentRe = re.compile ("--\ ?^Q.+$")	#"--.+\n|--.+\z")
	lineCommentRe = re.compile ("--.+\n|--.+\z")
	newStr = re.sub(lineCommentRe, "\n", str)
	return newStr

	
#Read "Lab_3_Queries", take out comments, and save into "Lohmann_Lab_3_Queries"
'''
#rf = open ("Lab_3_Queries", "r", encoding="utf-8")
#fileStr = rf.read()
#rf.close()
fileStr =open("Lab_3_Queries", "r", encoding="utf-8").read()#.replace("--.+\n|--.+\z", "")

fileStr = comment_remover(fileStr)
#fileStr = removeComments (fileStr)


wf = open ("Lohmann_Lab_3_Queries.sql", "w", encoding="utf-8")
wf.write(fileStr)
wf.close()
'''



#Create array of strings, where each string is a separate query

#rf = open("Lohmann_Lab_3_Queries", "r", encoding="utf-8")
'''
fileStr =open("Lab_3_Queries", "r", encoding="utf-8").read()

pattern = re.compile (r";$", re.DOTALL | re.MULTILINE)
queryStrings = re.split(pattern, fileStr) #splits by ';' character followed by newline
queryList = [query + ";" for query in queryList if (len(query) > 5)] # add back the ';' character, and remove any short, garbage strings created by regex
'''

# fileStr =open(r"C:\Users\david\OneDrive\Documents\Classes\CURRENT-SEMESTER\CSE 111 Database Systems\CSE111\Lab-3\Lohmann_Lab_3_Queries.sql", "r", encoding="utf-8").read()
fileStr =open(r"Lohmann_Lab_5_Queries.sql", "r").read()
fileStr = comment_remover(fileStr)
fileStr = remove_line_comments(fileStr)
pattern = re.compile(';', re.MULTILINE|re.DOTALL)
queryList = re.split (pattern, fileStr)
queryList = [query + ";" for query in queryList if (len(query) > 5)]

#Write each query to separate files
for i in range (len(queryList)):
	print ("\n\n\nQuery # ", (i+1), " is:\n")
	print (queryList[i])
	wf = open("Results/" + str(i+1) + ".sql", "w")
	wf.write(queryList[i])
	wf.close()
