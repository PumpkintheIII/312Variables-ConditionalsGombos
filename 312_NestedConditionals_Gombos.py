#step 25 logical operators
"""
# and operator 
sleep = 8         #Modify this number to see how it changes the output 
breakfast = True  #Modify this number to see how it changes the output 
print (sleep>=8 and breakfast==True) 

# or operator 
food = "cake"     #Modify this food to see how it changes the output 
print(food=="cake" or food=="muffins") 

# not operator 
movie = "like"    #Modify this to say "dislike" to see how it changes the output 
print (movie!="like")
#prediction: true, true, false
#output: true, true, false
"""
#step 29 nested conditionals
guesses = 3  # Change this number to see how the code output changes. 

if guesses >= 1: #checks if you have guesses left
  x = int(input("pick a number:")) #prompts user to guess a number, and sets the number to the 'x' variable
  if x < 10: #checks if x is less then 10
    print("too low") #if number is less then 10, tells user to guess higher
  else: #checks if x is greater than 10
    print("too high") #if x is greater then 10, tells user to guess lower
else: #if user has no guesses left, tells user that they are out of guesses
  print("You have run out of guesses!") 
#prediction: will check if the user has enough remaining guesses, if they do it will prompt the user to guess a number.it will then check if the number is higher or lower than the number and respond acordingly 
#output: ^