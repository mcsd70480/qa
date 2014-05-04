

import os.path

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
	
	retString = x1[0] + str(qNum)    + x1[1] + myEol
	retString+= x2[0] + str(qParts)  + x2[1] + myEol	
	retString+= x3[0] + str(qAns)    + x3[1] + myEol
	retString+= x4[0] + str(qExp)    + x4[1] + myEol	
	retString+= x5[0] + str(qType)   + x5[1] + myEol
	return retString
	
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
	
	myCRString = '\r'
	myLinefeed = '\n'
	
	myEol = myLinefeed
	
	retString = x1[0] + str(qNum)    + x1[1] + myEol
	retString+= x2[0] + str(qParts)  + x2[1] + myEol	
	retString+= x3[0] + str(qAns)    + x3[1] + myEol
	retString+= x4[0] + str(qExp)    + x4[1] + myEol	
	retString+= x5[0] + str(qType)   + x5[1] + myEol
	return retString

## test 1  
testName = "constructXmlRecord test 1"
expected =  constructXmlRecordTested(1,2,3,4,5)
runResult = constructXmlRecord (1, 2, 3, 4, 5)

if (expected != runResult):
    print 40*"?"
    print "Test " + testName + "  failed: "
    print 40*"?"
    print "   Expected: -->" + expected + "<--"
    print "   Actual:   -->" + runResult + "<--"
else:
    print 40*"="
    print "Test " + testName + " passed."	


## test 2 
testName = "constructXmlRecord test 2" 
expected =  constructXmlRecordTested(1,2,0,4,5)
runResult = constructXmlRecord (1, 2, 0, 4, 5)

if (expected != runResult):
    print 40*"?"
    print "Test " + testName + "  failed: "
    print 40*"?"
    print "   Expected: -->" + expected + "<--"
    print "   Actual:   -->" + runResult + "<--"
else:
    print 40*"="
    print "Test " + testName + " passed."	



	