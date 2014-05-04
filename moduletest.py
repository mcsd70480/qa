import os.path
import pngQuestScan
##  
##  module:   PngQuestScan 
##
##  qaFilesCheck( ...)   looks for qa png file types, finding returns in list
##			def qaFilesCheck( qPath, qNum, retList):	
##
##  fileExist( ...)      checks if a file is on the local drive
##			def fileExist( filename):
##
##
##  testReport( ...)     used by test functions to report success/failure
##
##  constructXmlRecord( ...)  base on input List with qa info, returns XML formatted
## 							  record
##			def constructXmlRecordTested ( qNum, qParts, qAns, qExp, qType):
##

print "testing if import ok"

f = "q1.png"
fileFound = pngQuestScan.fileExist( f)
print f + " found: " 
print fileFound

f = "q1a.png"
fileFound = pngQuestScan.fileExist( f)
print f + " found: " 
print fileFound

	 
def testPngFilesExist():
	startNumber = 1
	lastNumber =  10
	resultList = list()
	resultList.append(111)
	resultList.append(222)
	resultList.append(333)
	resultList.append(444)
	resultList.append(555)

	for curQuestion in range(startNumber, lastNumber):

		qPath= ""  ##  "..\\"
		status = pngQuestScan.qaFilesCheck( qPath, curQuestion, resultList)	

		print curQuestion 
		print status
		print resultList
		print 40*"-"

	return	

def createQaXmlFile():
	myCRString = '\r'
	myLinefeed = '\n'
	
	myEol = myLinefeed

	xmlFileName = "questions.xml"
	file = open( xmlFileName, "w")
##	xmlHeader =  '<?xml version="1.0" encoding="UTF-8"?>'
##	file.write( xmlHeader + myEol) 
	
	xmlRootTag   = ["<ALL>",  "</ALL>" ]
	xmlRecordTag = ["<QUESTION>", "</QUESTION>" ]
	
	file.write( xmlRootTag[0])
	
	## cycle through all the questions and look for support files
	startQuestion = 1
	lastQuestion = 20
	for curQuestNum in range( startQuestion, lastQuestion):
		## write opening tag XML data group 
		file.write (xmlRecordTag[0] + myEol)

		xmlForCurrentQuestion = pngQuestScan.createXmlRecordForQuestion( curQuestNum )
		file.write( xmlForCurrentQuestion + myEol)

		## write closing tag for XML data group
		file.write( xmlRecordTag[1] + myEol )
	
	file.write( xmlRootTag[1]) 
	file.close()
	return

	
testPngFilesExist()


myCRString = '\r'
myLinefeed = '\n'
	
myEol = myLinefeed

xmlFileName = "xmltest.xml"
file = open( xmlFileName, "w")
xmlGroupTag = ["<QUESTIONS>", "</QUESTIONS>" ]

xmlTestData= "<AGE>45</AGE>"

file.write (xmlGroupTag[0] + myEol)
file.write (xmlTestData + myEol)
file.write (xmlGroupTag[1] + myEol)
file.close()
print "wrote to XML file " + xmlFileName 


createQaXmlFile() 


##  XML
##
##  write XML header to file
##     cycle through the pngs
##  write out closing XML tag
##  verify if correct

##  JSON
##
##  write JSON header
##    cycle through the pngs
##  write closing JSON mark
##  verify if JSON is correct



