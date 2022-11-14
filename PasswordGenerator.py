import random

def randomPasswordGenerate():
  lenOfPass = 0
  randPassword = ""
  while lenOfPass <= randPassLength:
    randPassword += random.choice(charList)
    lenOfPass += 1
  print("Thank you for using the random password geneator. Your secure password is"  ,randPassword  , )

charList = ["a", "b", "c" "d", "e", "f", "g", "h" , "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", " ", "#", "$", "%", "^", "&", "(" ")", "-", "=", "_", "+", ";" ":", "'", "<", ",", "/", ".", ">", "?", "[", "]"]

print("Hello. Welcome to my random password generator. With so much of our lives being protected by passwords, it is important to make them as secure as possible")

randPassLength = int(input("How long would you like your secure password to be?   "))

if randPassLength <= 8:
  print("Warning: This password isn't secure. It should be more than 8 characters in length.")
  shortPassWarning = input("Would you like to continue with this short, dangerous password?   ")
  if shortPassWarning.lower() == "no":
    randPassLength = int(input("How long would you like your secure password to be?   "))
  if shortPassWarning.lower() == "yes":
    randomPasswordGenerate()

if randPassLength >= 8:
  randomPasswordGenerate()
