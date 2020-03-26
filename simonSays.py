import random
import time
import tty
import sys
import os

def numToLetter(num):
  if (num == 0):
    return 'r'
  elif (num == 1):
    return 'b'
  elif (num == 2):
    return 'g'
  else:
    return 'y'

def letterToColor(letter):
  if (letter == 'r'):
    return 'red   '
  elif (letter == 'b'):
    return 'blue  '
  elif (letter == 'g'):
    return 'green '
  elif (letter == 'y'):
    return 'yellow'
  else:
  	print("INVALID LETTER")

def main():
	os.system('clear')
	time.sleep(0.5)
	correct = True
	pattern = []

	# while correct:
	while correct == True:
		# generate random letter
		randNum = random.randint(0,4)
		letter = numToLetter(randNum)
		# store in array
		pattern.append(letter)
		# output pattern
		showPattern(pattern)
		
		# player's attempt
		player = input("Your turn! Type in the pattern and press enter: ")

		# first check if user input the right number of colors
		if len(player) != len(pattern):
			correct = False
		else:
			# check user input
			for i in range(0, len(pattern)):
				# if wrong
				if (pattern[i] != player[i]):
					correct = False
		# if right
		if (correct == True):
			print("Correct!")

		# clear the system so user cannot see their previous answers
		time.sleep(0.5)
		os.system('clear')
		time.sleep(0.5)

	print("GAME OVER! Your score is " + str(len(pattern)-1))


def showPattern(pattern):

  for p in pattern:
    # show letter
    print("\rRepeat after me! >> " + str(letterToColor(p)), end='')
    sys.stdout.flush()
    time.sleep(1)
    # hide pattern
    print("\rRepeat after me! >>       ", end='')
    sys.stdout.flush()
    time.sleep(.1)
  print()

# def test():
#   correct = True
#   while correct:
#     tty.setcbreak(sys.stdin)  
#     key = ord(sys.stdin.read(1))  # key captures the key-code 
#     # based on the input we do something - in this case print something
#     if key==97:
#         print ("you pressed a")
#     else:
#         correct = False
#         break


# def test():
#     correct = True
#     counter = 1
    # while correct and not at length
        # check for buttons
        # red -> if GPIO.buttonRED == 1
            # verify()
        # green
            # verify()
        # blue
            # verify()
        # yellow
            # verify()

# def verify()
# if wrong
#   correct = False
# else
#   counter++


# test()
main()