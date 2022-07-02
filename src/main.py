print('welcome')
print('Created by Anyaele Destiny Chinaemerem')
print('we have three games ready')
Games = ['Guessing_Game','Rock Paper Scissors','Cows and Bulls','Hangman']
for num,Game in enumerate(Games) :
  print(num,' : ',Game)
tries,won = 0,0
import random, string
print('Enter Q anytime to quit')
def Guessing_Game() :
  global tries,won
  print('Good choice, welcome to Guessing Game')
  print('pick a number 0 - 9')
  while True :
    computer_guess = random.randrange(10)
    computer_guess = str(computer_guess)
    user_input = input('Enter your guess : ')
    if user_input == 'Q' :
      break
    for test in user_input :
      if (test in string.digits) == False :
        variable = True
        break   
    else :
      variable = False
    while variable :
      print('invalid input !!!')
      user_input = input('Enter your guess again : ')
      for test in user_input :
        if (test in string.digits) == False :
          variable = True
          break   
      else :
        variable = False
    if user_input == computer_guess :
      print('Correct 8-) ')
      print('Nice guess')
      print('\n')
      won += 1
    else :
      print('Wrong  :-( ')
      print(f'The answer was {computer_guess}')
      print('Keep trying')
      print('\n')
    tries += 1
def Rock_Paper_Scisssors_Game() :
  global tries,won
  pool = ('Rock','Paper','Scissors')
  print('Good choice, welcome to Rock Paper Scissors Game')
  while True :
    computer_choice = random.choice(pool)
    user_input = input('Enter your choice : ')
    if user_input == 'Q' :
      break
    user_input = user_input.title()
    if (user_input in pool) == True :
      error = False
    else :
      error = True
    while error :
      print('invalid input !!!')
      user_input = input('Enter your choice : ')
      user_input = user_input.title()
      if (user_input in pool) == True :
        error = False
      else :
        error = True
    if user_input == computer_choice :
       print('Draw')
    elif computer_choice == 'Rock' and user_input == 'Paper' :
       print('you lost')
    elif computer_choice == 'Paper' and user_input == 'Scissors' :
       print('you lost')
    elif computer_choice == 'Scissors' and user_input == 'Paper' :
       print('you lost')
    else :
       print('you won')
       won += 1
    tries += 1
def Cows_and_Bulls_Game() :
  print('Good choice')
  print('welcome to Cows and Bulls Game')
  while True :
    computer_choice = str(random.randint(1000,10000))
    user_input = input('Enter your guess : ')
    if user_input == 'Q' :
      break
    try :
      for i in user_input :
        if (i in string.digits) != True or len(user_input) > 4 or len(user_input) < 4 :
          raise Exception('only digits allowed or too long or too short input')
    except Exception as error_details :
      print(error_details)
      Cows_and_Bulls_Game()
    else :
      if computer_choice == user_input :
        print('You won :-) ')
      else :
        index,cows,bulls = 0,0,0
        while index <= 3 :
          if user_input[index] == computer_choice[index] :
            bulls += 1
          if (user_input[index] in computer_choice) == True :
            cows += 1
          index += 1
        print('bulls : ', bulls)
        print('cows : ',cows)
        print('The right guess was ',computer_choice)
    print('\n')
print('choose the number or the title of the game')
def Hangman_Game() :
  print('Good choice, welcome to Hangman')
  print('Enter 1 for Easy')
  print('Enter 2 for Medium')
  print('Enter 3 for Difficult')
  level = int(input('Select your difficulty : '))
  Easy_words = ['Dart','Fast','Make','Lamb']
  Medium_words = ['Snake','Peter','Skill','Hello']
  Hard_words = ['Drakes','Reason','Thanks','Quarry']
  def diagram_1() :
    for i in range(10) :
      print('_',end = '')
    print()
    for i in range(8) :
      print('|')
    for i in range(10) :
      print('_',end = '')
  def diagram_2() :
    for i in range(10) :
      print('_',end = '')
    print()
    for i in range(9) :
      if i == 5 :
        q = '      0\n'
      elif i == 6 :
        q = '    / | \ \n'
      elif i > 6 and i < 8 :
        q = '       | \n'
      elif i == 8 :
        q = '     / \ \n' 
      else :
        q = '\n'
      print('|',end = q) 
    for i in range(10) :
      print('_',end = '')
  def diagram_3() :
      for i in range(10) :
        print('_',end = '')
      print()
      for i in range(9) :
        if i < 2 :
          q = '       |\n'
        elif i == 5 :
          q = '      0\n'
        elif i == 6 :
          q = '    / | \ \n'
        elif i > 6 and i < 8 :
          q = '       | \n'
        elif i == 8 :
          q = '     / \ \n'
        else :
          q = '\n'
        print('|',end = q)
      for i in range(10) :
        print("'''",end = '')
  def diagram_4() :
      for i in range(10) :
        print('_',end = '')
      print()
      for i in range(9) :
        if i < 4 :
          q = '       |\n'
        elif i == 5 :
          q = '      0\n'
        elif i == 6 :
          q = '    / | \ \n'
        elif i > 6 and i < 8 :
          q = '       | \n'
        elif i == 8 :
          q = '     / \ \n'
        else :
          q = '\n'
        print('|',end = q)
      for i in range(10) :
        print("'''",end = '')
  def diagram_5() :
      for i in range(10) :
        print('_',end = '')
      print()
      for i in range(9) :
        if i < 4 :
          q = '       |\n'
        elif i == 4 :
          q = '      0\n'
        elif i == 5 :
          q = '    / | \ \n'
        elif i > 5 and i < 7 :
          q = '       | \n'
        elif i == 7 :
          q = '     / \ \n'
        else :
          q = '\n'
        print('|',end = q)
      for i in range(10) :
        print("'''",end = '')
  if level == 1 :
    num = 3
    selected_word = random.choice(Easy_words)
  elif level == 2 :
    num = 4
    selected_word = random.choice(Medium_words)
  else :
    num = 5
    selected_word = random.choice(Hard_words)
  hidden_letter = random.sample(selected_word,level)
  print('your word is : ',end = '')
  for i in selected_word :
    if (i in hidden_letter) == True :
      print('*',end = '')
    else :
      print(i,end = '')
  print()
  while num > 0 :
    print('you have',num,'guesses ,Good luck !!')
    user_guess = input('Enter your guess : ')
    if (user_guess in hidden_letter) == True :
      print('correct :-)')
      hidden_letter.remove(user_guess)
      if len(hidden_letter) == 0 :
        print('You won B-) ')
        break
      for  i in selected_word :
        if (i in hidden_letter) == True :
          print('*',end = '')
        else :
          print(i,end = '')
      print()
    else :
      print('wrong')
      if num == 5 :
        diagram_1()
      elif num == 4 :
        diagram_2()
      elif num == 3 :
        diagram_3()
      elif num == 2 :
        diagram_4()
      elif num == 1 :
        diagram_5()
        print('\nyou lost :-(')
        print('You were hanged')
        print('The word was ',selected_word)
      print()
      num -= 1
choice = input('What game do you want : ')
if __name__ == '__main__' and (choice == 'Guessing Game' or choice == '0') :
  Guessing_Game()
elif __name__ == '__main__' and (choice == 'Cows and Bulls' or choice == '2') :
  Cows_and_Bulls_Game()
elif __name__ == '__main__' and (choice == 'Hangman' or choice == '3') :
  Hangman_Game()
else :
  Rock_Paper_Scisssors_Game()
print('you won ',won,' times out of ',tries,' times')
