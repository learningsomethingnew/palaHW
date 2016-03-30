#import statistics stuff for easier calculations
from statistics import mean, median, mode, stdev

###program that keeps track of user input.
###      Ask user to enter a number
###      Ask while user inputs a number
###     If user enters a blank, the program finishes
###     Program outputs count of numbers input, sum of all numbers, and average.

#list for tracking the numbers
numTracker=[]
#list for tracking the strings
strTracker=[]

#user input for tracking
def promptUser():
    run = True
    while run == True:
        userInput = input("Input>> ")

        if userInput == "":
            statsGen()
            run = False
        #Test for type of input
        try:
            float(userInput)
            trackNumbers(float(userInput))
            deBuggerHelp("USER inputted a number")
        except ValueError:
            deBuggerHelp("USER inputted non-number")
        #Adds string to the string list
            trackString(userInput)
            deBuggerHelp("USER inputted a string " + userInput)


#Generic greeter for this app
def greeting():
    linebreak = "-------------------------------------------------------"
    print(linebreak)
    print("Welcome to Input Statistics")
    print("Please input either a string or number to start tracking")
    print("To quit submit an empty line")
    print(linebreak + "\n")

#Adds the numbers to one list for easier manipulation
def trackNumbers(fltUserInput):
    deBuggerHelp("User tracked "+ str(fltUserInput))
    numTracker.append(fltUserInput)

#Tracks the strings to one list
def trackString(strUserInput):
    deBuggerHelp("User has tracked " + strUserInput)
    strTracker.append(strUserInput)
    for word in strTracker:
        deBuggerHelp(word)

#when the user is done with the app, this will crunch the stats that the user wanted
def statsGen():
    linebreak = "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    #varify how many items I have in each list
    deBuggerHelp("THE NUMTRACKER LENGTH IS " + str(len(numTracker)))
    deBuggerHelp("THE STRTRACKER LENGTH IS " + str(len(strTracker)))


    if len(numTracker) >= 1:
        print('\n' + linebreak)
        print("                     NUMBER STATS")
        print(linebreak)
        print("User, you entered " + str(len(numTracker))+ " numbers")
        print("The sum of these numbers are " + str(sum(numTracker)))
        print("The mean of the inputs are " + str(mean(numTracker)))
        print(str(findMode()))
        print("The median of the inputs are " + str(median(numTracker)))
        print("The standard deviation of the inputs are " + str(stdev(numTracker)))
    if len(strTracker) >= 1:
        print('\n' + linebreak)
        print("                     WORD STATS")
        print(linebreak)
        print("User, you entered " + str(len(strTracker))+ " strings")
        print("The largest string(s) you entered was " + str(longestWordsList()))
        print("The shortest string(s) you entered was " + str(shortestWordsList()))
        print("The average string length you entered was " + str(meanLenString()))
        print("The number of times 'e' was entered " + str(numOfEs()))


#attempts to find the mode
def findMode():
    try:
        return ("The mode of the inputs is " + str(mode(numTracker)))
    except ValueError:
        return "There is no mode"



#returns the largest word(s) in the initial list
#grabbed core idea functionality from SO
def longestWordsList():
    longWord = max(strTracker, key=len)
    #list to store large words of equal size
    listOfLongWords = []

    deBuggerHelp("THE LONGEST WORD IS " + longWord)
    for word in strTracker:
        deBuggerHelp("FOR LOOP WORD " + word)
        if len(word) == len(longWord):
            listOfLongWords.append(word)
    return str(listOfLongWords).strip('[]')

#returns the shortest words in the initial list
def shortestWordsList():
    shortWord = min(strTracker, key=len)
    #list to store short words of equal size
    listOfShortWords = []

    deBuggerHelp("THE LONGEST WORD IS " + shortWord)
    for word in strTracker:
        deBuggerHelp("FOR LOOP WORD " + word)
        if len(word) == len(shortWord):
            listOfShortWords.append(word)
    return str(listOfShortWords).strip('[]')

#determine the average string length
def meanLenString():
    lenOfWords = 0
    for word in strTracker:
        lenOfWords += len(word)
    return lenOfWords/len(strTracker)

#determine how many times was 'e' entered
#idea of implementation from tutorialspoint.com
def numOfEs():
    eCount = 0
    #what are we looking for?
    sub = 'e'
    for word in strTracker:
        eCount += word.count(sub, 0,len(word))
    return eCount

#Debugger help text. Simple comment out of this will block annoying text
def deBuggerHelp(helpText):
    linebreak = "*******************************************************"

greeting()
promptUser()