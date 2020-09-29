print("Title of program: MCQ revision program")
print()

counter = 0
score = 0
total_num_of_qn = 3


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "find y if 8x2+4/y=22?")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "24":
    output = "correct!:)")
    score +=1
  else answer == "1-999":
    output = "Wrong. Clue:4/y=22-8x2."
    score -=1

    
  
  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  


counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "how many atoms are there in NaHCO3 represents")
  print("   a) 7")
  print("   b) 12")
  print("   c) 6")
  print("   d) 4")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "wrong. Clue:chemical symbols start with a capital letter."
    tracker =1
    score -=1
  elif answer == "b":
    output = "Wrong. clue:are you sure it is (NaHCO)3??."
    score -=1
  elif answer == "c":
    output = "Correct!:)"
    score +=1
    
  elif answer == "d":
    output = "Wrong. clue: I think you forgot about the 3."
    score -=1
  else:
    output = "Please choose a, b, c or d only."

  print()
  print(output)
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
  

counter +=1
tracker = 0

while tracker !=1:
  
  print("Q"+str(counter)+") "+ "Which represents the electronic configuration of a non-metal?")
  print("   a) 2,1")
  print("   b) 2,8,3")
  print("   c) 2,8,8,2")
  print("   d) 2,7")
  answer = input("Your answer: ")
  answer = answer.lower()
  if answer == "a":
    output = "Wrong. Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "b":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
  elif answer == "c":
    output = "Wrong.  Think again - how many electron shells are filled, and which group is this in?"
    score -=1
    
  elif answer == "d":
    output = "Yes, that's right!"
    tracker =1
    score +=1
  else:
    output = "Please choose a, b, c or d only."

  

  print()
  print(output.lower())
  print()
  print("Your current score: " + str(round((score/total_num_of_qn*100),1)) + "%"  )
  print()
  print()
  
print("End of quiz!:)")
  
