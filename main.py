#Import the os module
import os

#Roman numeral dictionary
romanNumerals = {
  "I" : 1,
  "V" : 5,
  "X" : 10,
  "L" : 50,
  "C" : 100,
  "D" : 500,
  "M" : 1000
}

#Functions used for data validation
def isValid(romanNumeralString):
  #Variables
  _isValid = True

  #Iterate through the string
  for char in romanNumeralString:
    if not char in romanNumerals:
      _isValid = False
      break
  
  #Return if it's valid or not 
  return _isValid

#Function used to "digest" the roman numeral string and return pairs of roman numerals, this makes the calculating part easier
def digestString(string):
  #Variables
  _result = []

  #Prepare variables for the iteration process
  _stringLength = len(string)
  _nextVerifiedNumber = 0

  #Iterate through the string length
  for num in range(_stringLength):
    #Make sure num is safe to process
    if num == _nextVerifiedNumber:
      #Variables
      _char1 = string[num]
      _char2 = "" #This is verified in the next step

      #Make sure _char2 doesn't go out of the index range
      if num+1 <= _stringLength-1:
        _char2 = string[num+1]
      else:
        _char2 = "RANEND"

      #Check if 2 characters make a pair like 'IV', which is 4
      if _char2 != "RANEND" and romanNumerals[_char1] < romanNumerals[_char2]:
        _result.append(_char1 + _char2)
        _nextVerifiedNumber += 2
      else:
        _result.append(_char1)
        _nextVerifiedNumber += 1

  #Return the result
  return _result
  
#Main loop
while True:
  #Ask the user to input roman numerals
  user_Input = input("Please type roman numerals:\n> ").upper()

  #Data validation
  while not isValid(user_Input):
    #Display that it's an invalid answer
    print("\nINVALID INPUT! PLEASE TYPE ROMAN NUMERALS ONLY")
    
    #Ask the user to input roman numerals
    user_Input = input("\nPlease type roman numerals:\n> ")

  #Digest roman numeral string
  digested = digestString(user_Input)

  #Iterate through the digest and calculate the result
  result = 0
  for pair in digested:
    #Check if the pair is like 'IV', it has 2 characters
    if len(pair) == 2:
      result+= (romanNumerals[pair[1]] - romanNumerals[pair[0]])
    else:
      result += romanNumerals[pair]
  
  #Output the result
  print(f"\n{user_Input} to a number is {str(result)}")

  #Ask the user if they want to go again
  doAgain = input("\nWould you like to use this program again? (Y/N)\n> ").lower()

  #Data validation
  while doAgain != "y" and doAgain != "n":
    #Display invalid input
    print("\nINVALID ANSWER, PLEASE TYPE A Y OR AN N")

    #Ask the user if they want to go again
    doAgain = input("\nWould you like to use this program again? (Y/N)\n> ").lower()
  
  #Check if the user wants to do it again
  if doAgain == "y":
    os.system('clear')
  else:
    print("\nGoodbye!")
    break
