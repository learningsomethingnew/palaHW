import re
from time import sleep
import sys

def is_palindrome(aString):
    # TODO: return True or False if the sentence is or isn't a palindrome
    aString = regex_function(aString)
    if len(aString) != 0 and aString[0] == aString[-1]:
        is_palindrome(aString[1:-1])
    else:
        return False
    return True
    #compare the string to see if same back to front

def is_palindrome_iterative(aString):
    aString = regex_function(aString)

    while len(aString) != 0:
        if aString[0] == aString[-1]:
            aString=aString[1:-1]
            continue
        else:
            return False
    return True


#Regex Function to remove special characters
#All that we care about is standard characters
def regex_function(aString):
    #pattern to search for
    patternRegex = r'[^A-Za-z]'

    #Regex operation
    aString = re.sub(patternRegex, '', aString).lower()
    return aString

# Takes input from the user
def prompt_user():
    # catches the user's input for testing
    user_input = input(">>>")
    if user_input == "quit" or user_input == "Quit":
        sys.exit(0)
    return str(user_input)

# displays text as if someone is typing
def print_text(a_string, a_is_slow):
    if a_is_slow:
        for words in a_string + "\n":
            sys.stdout.write(words)
            sys.stdout.flush()
            sleep(.03)
    else:
        print(a_string)

def greeting():
    print_text("Hello user, please enter a word to see if it is a palindrome", True)
    print_text("Type 'quit' to end the program at anytime", True)

def main():
    # TODO: put your input/output code here
    run = True

    greeting()

    while run == True:
        userString = prompt_user()
        if is_palindrome(userString) == True and is_palindrome_iterative(userString) == True:
            print_text("Your string is a palidrome", True)
        else:
            print_text("Your string is not a palidrome", True)



if __name__ == '__main__':
    main()

