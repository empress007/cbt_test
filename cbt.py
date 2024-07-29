#  write a python programme that sets cbt. score participate and also return the total score at the end of the test. 

def cbt():
  questions = (    ("1. Who is the current President of Nigeria"),
      ("2. Which continent is Nigeria in"),  ("3. Full Meaning of CBN"),('4. What is the capital of Oyo')
      )
  options = (
      ("A. Bola Ahmed Tinubu","B. Joe Biden","C. Elon Musk"),    ("A. Europe","B. Asia","C. Africa"),
      ("A. Central Bank of Nigeria","B. Center Bank of Niger","C. Center of Excellence"),('A. Fiditi','B. Ibadan','C. lagos'))
  answers = ('A','C','A','B') # correct answer 
  index = 0
  scores = 0

  # for loop to run the questions
  for question in questions:
      print('------------------------------- \n')
      print(question)
      for option in options[index]:        
          print(option)
      userInput = input('What is your answer: ').upper()    
      ''' Check answer and score'''
      if userInput == answers[index]:        
          print('You got it right \n')
          scores += 25
          print(f'scores = {scores}%')
      else:       
          print('You didnt get it right \n')
          print(f'scores = {scores}%')
      index += 1
  print(f'{scores}%')
cbt()