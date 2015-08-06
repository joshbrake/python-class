# Hangman game
# Import random integer function from random module
from random import randint

# Create list of strings to use as hangman words
words = ["bear","righteous","holy","whiteboard","house","endocratic","judicial","window"]
#words = ["test"]

# Function to convert list to a string to print
def list2string(l):
  string = "".join(l)
  return string
  
# Function to setup the game by selecting a random word from the list and configure the display
def setup(words):

  # Generate random index to select random word from list "words"
  rand_index = randint(0,len(words)-1)
  
  # Choose the random word
  rand_word = words[rand_index]
  
  # Find the length of the random word to figure out how many blanks we need
  length_rand_word = len(rand_word)

  # Generate the display word full of blanks
  display_word_list = []
  
  # Append an underscore to words
  for x in range(0,length_rand_word):
    display_word_list.append("_")
  
  display_word = list2string(display_word_list)
  return rand_word,display_word_list

# Function to draw hangman shape and fill in the appropriate number of body parts for number of wrong letters guessed
def drawHangman(numWrong):
  
  numDisp = numWrong
  hangman_parts = ['O','|','\\','/','|','/','\\']
  
  hangman_disp = hangman_parts[0:numDisp] + [' '] * (len(hangman_parts)-numDisp)
  
  hangman_template = [
    "      ______    \n",
    "      |    |    \n",
    "      |    " + hangman_disp[0] + "     \n",
    "      |   " + hangman_disp[2] + hangman_disp[1] + hangman_disp[3] + "    \n",
    "      |    " + hangman_disp[4] + "     \n",
    "      |   " + hangman_disp[5] + " " + hangman_disp[6] + "     \n",
    "      |         \n",
    "      |         \n",
    "=============   \n"]
  print(''.join(hangman_template))
                   
# Run setup
(random_word,display_word_list) = setup(words)  

# Setup for loop to run the main game
keep_going = 1
num_wrong_letters = 0
max_num_wrong_letters = 7

# Print the display word to the screen
print(list2string(display_word_list))

# Enter the main program loop
while keep_going == 1:
  num_fails = 0
  user_guess = raw_input("Please pick a letter: ")
  for x in range(0,len(random_word)):
    if user_guess == random_word[x]:
      display_word_list[x] = user_guess
    #print x
    else:
      num_fails = num_fails + 1
      
    if num_fails == len(random_word):
      num_wrong_letters = num_wrong_letters + 1
      print("You guessed wrong! Try again.")
      drawHangman(num_wrong_letters)
      if num_wrong_letters == max_num_wrong_letters:
        keep_going = 0
      break
    
    num_letters_left = 0
    for x in range(0,len(random_word)-1):
      if display_word_list[x] == "_":
        num_letters_left = num_letters_left + 1
    
    if num_letters_left == 0:
      keep_going = 0
      break
      print("You guessed the word!")
      
        
  print(list2string(display_word_list))