import os.path

##  This module contains the following functions.
##
##  qaFilesCheck( ...)   looks for qa png file types, finding returns in list
##
##  fileExist( ...)      checks if a file is on the local drive
##
##  testReport( ...)     used by test functions to report success/failure
##
##  constructXmlRecord( ...)  base on input List with qa info, returns XML formatted
## 							  record
##
## def createXmlRecordForQuestion ( questionNumber):
##
##  constructXmlRecordForQuestion( ...)  search and return XML record for the question specified	
##
def qaFilesCheck( qPath, qNum, retList):	
	## qPath equals  ..\  for current directory
	qFilename = qPath + "q" + str(qNum) + ".png"
	
##	retList = [-1, -1, -1, -1, -1]
	retList[0] = qNum
	retList[1] = -1
	retList[1] = -1
	retList[1] = -1
	retList[1] = -1
	if fileExist(qFilename):
		retList[1]=1
	else:
		## look for q1a.png, q1b.png, q1c.png, etc
		## should loop from 'a' to 'e'
		## use 'a' and 'b' for dev mode
		qFilename = qPath + "q" + str(qNum) + 'a' + ".png"
		if fileExist(qFilename) :
			retList[1] = 1
		qFilename = qPath + "q" + str(qNum) + 'a' + ".png"
		if fileExist(qFilename) :
			retList[1] = 1 + retList[1] 
	
	if retList[1] == -1:  ## if q1.png and q1a.png not found, set to 0
		retList[1] = 0
				
	## look for answer file
	qFilename = qPath + "q" + str(qNum) + "ans" + ".png"
	if (fileExist(qFilename)) :
		retList[2] = 1
	else:
		retList[2] = 0

	## look for explanation file
	qFilename = qPath + "q" + str(qNum) + "exp" + ".png"
	if (fileExist(qFilename)) :
		retList[3] = 1
	else:
		retList[3] = 0
	
	## look for question type file
	qFilename = qPath + "q" + str(qNum) + "type" + ".png"
	if (fileExist(qFilename)):
		retList[4] = 1
	else:
		retList[4] = 0
	
	return				

	
	
def fileExist( filename):
	found = False
	found = os.path.isfile(filename)
	if found:
		print filename + " found"
	else:
		print filename + " NOT found"
	return found

def testReport (testName, expected, actual):
	print
	if (expected == actual):
		print 40*"="
		print "Test: " + testName + " passed."
	else:
		print 40*"?"
		print "Test: " + testName + " FAILED."
		print "   Expected: -->" 
		print expected
		print "   Actual:   -->" 
		print actual
		print 40*"?"
		print 

	return		


def constructXmlRecord ( qNum, qParts, qAns, qExp, qType):
	## qNum: question number 
	## qParts: how many parts, ie. {a,b,c,..}
	## qAns: answer file exist 
	## qExp: explanation file exist
	## qType:type of question file exist

	x1 = ["<QNUMBER>", "</QNUMBER>"  ]
	x2 = ["<QPARTS>"  , "</QPARTS>"  ]
	x3 = ["<QANSWER>" , "</QANSWER>" ]
	x4 = ["<QEXPLAIN>", "</QEXPLAIN>"]
	x5 = ["<QTYPE>"   , "</QTYPE>"   ]
	
	myCRString = '\r'
	myLinefeed = '\n'
	
	myEol = myLinefeed

	indent= "    "
	
	retString = indent + x1[0] + str(qNum)    + x1[1] + myEol
	retString+= indent + x2[0] + str(qParts)  + x2[1] + myEol	
	retString+= indent + x3[0] + str(qAns)    + x3[1] + myEol
	retString+= indent + x4[0] + str(qExp)    + x4[1] + myEol	
	retString+= indent + x5[0] + str(qType)   + x5[1] + myEol
	return retString
	
def testReturn ( qNumber, retList ):

	retList[0] = qNumber
	retList[1]=  qNumber + 100
	retList[2]=  qNumber + 200
	retList[3]=  qNumber + 300
	retList[4]=  qNumber + 400
	return True
			
def createXmlRecordForQuestion ( questionNumber):

	xmlRecord = "error in createXmlRecordForQuestion"
	resultList = list()
	resultList.append(111)
	resultList.append(222)
	resultList.append(333)
	resultList.append(444)
	resultList.append(555)

	qaFilesCheck ("", questionNumber, resultList)
	n1 = resultList[0]
	n2 = resultList[1]
	n3 = resultList[2]
	n4 = resultList[3]
	n5 = resultList[4]
	xmlRecord = constructXmlRecord( n1, n2, n3, n4, n5)
	
	return xmlRecord
	


def constructXmlRecordTested ( qNum, qParts, qAns, qExp, qType):
	## qNum: question number 
	## qParts: how many parts, ie. {a,b,c,..}
	## qAns: answer file exist 
	## qExp: explanation file exist
	## qType:type of question file exist

	x1 = ["<QNUMBER>", "</QNUMBER>"  ]
	x2 = ["<QPARTS>"  , "</QPARTS>"  ]
	x3 = ["<QANSWER>" , "</QANSWER>" ]
	x4 = ["<QEXPLAIN>", "</QEXPLAIN>"]
	x5 = ["<QTYPE>"   , "</QTYPE>"   ]
	
	indent= "    "
	
	myCRString = '\r'
	myLinefeed = '\n'
	
	myEol = myLinefeed
	
	retString = indent + x1[0] + str(qNum)    + x1[1] + myEol
	retString+= indent + x2[0] + str(qParts)  + x2[1] + myEol	
	retString+= indent + x3[0] + str(qAns)    + x3[1] + myEol
	retString+= indent + x4[0] + str(qExp)    + x4[1] + myEol	
	retString+= indent + x5[0] + str(qType)   + x5[1] + myEol
	return retString

## test 1  
testName = "constructXmlRecord test 1"
expected =  constructXmlRecordTested(1,2,3,4,5)
runResult = constructXmlRecord (1, 2, 3, 4, 5)
testReport( testName, expected, runResult) 

## -------------------------------------------------

## test 2 
testName = "constructXmlRecord test 2" 
expected =  constructXmlRecordTested(1,2,0,4,5)
runResult = constructXmlRecord (1, 2, 0, 4, 5)
testReport( testName, expected, runResult)

## -------------------------------------------------

		 
def testPngFilesExist():
	startNumber = 1
	lastNumber =  10
	resultList = list()
	resultList.append(111)
	resultList.append(222)
	resultList.append(333)
	resultList.append(444)
	resultList.append(555)


	## test 3
	testName = "qaFileCheck test 1"
	qaFilesCheck ("..\\", 999, resultList)
	expected = [999, 0, 0, 0, 0]
	actual = resultList
	testReport( testName, expected, actual)
	print "SFSDFSFSDFSDFDS"
	## -------------------------------------------------

	for curQuestion in range(startNumber, lastNumber):

		qPath= ""  ##  "..\\"
		status = qaFilesCheck( qPath, curQuestion, resultList)	

		print curQuestion 
		print status
		print resultList
		print 40*"-"

	return	

# retData = createXmlRecordForQuestion( 2)
# print retData
