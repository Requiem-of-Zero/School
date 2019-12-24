sentence = ""
#user input is empty 
userInput = ""
#loop through the input while user doesnt enter space 
while(userInput != " "):
  #assign and storing user input to variable 
  userInput = input("Please enter a word or nothing to quit: ")
  #
  sentence = sentence + userInput + " "
  print(sentence)
  if(userInput == " "):
    print(sentence)
    break



  
