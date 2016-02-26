import os
import random

def main():
	os.system('cls')
	print 'Welcome to Camel!\n'
	print 'You have stolen a camel to make your way across the great Mobi desert.\n'
	print 'The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.\n'
	
	done = False
	miles_traveled = 0
	thirst = 0
	camel_tiredness = 0
	natives_traveled = -20
	canteen = 3
	oasis = 7
	
	while not done:
		print 'A: Drink from your canteen.'
		print 'B: Ahead moderate speed.'
		print 'C: Ahead full speed.'
		print 'D: Stop for the night.'
		print 'E: Status check.'
		print 'Q: Quit.\n'
		
		choice = raw_input('Choose an option: ').lower()
		
		if choice == 'q':
			done = True
		elif choice == 'e':
			print 'Miles traveled: ' + str(miles_traveled)
			print 'Drinks in canteen: ' + str(canteen)
			print 'The natives are ' + str(natives_traveled) + ' miles behind you.\n'
		elif choice == 'd':
			camel_tiredness = 0
			print 'The camel is happy.\n'
			natives_traveled += random.randint(7,15)
		elif choice == 'c':
			miles_traveled += random.randint(10,21)
			print 'User traveled ' + str(miles_traveled) + '\n'
			thirst += 1
			camel_tiredness += random.randint(1,4)
			natives_traveled += random.randint(7,15)
		elif choice == 'b':
			miles_traveled += random.randint(5,13)
			print 'User traveled ' + str(miles_traveled) + '\n'
			thirst += 1
			camel_tiredness += 1
			natives_traveled += random.randint(7,15)
		elif choice == 'a':
			if canteen > 0:
				print 'Drinking...\n'
				canteen -= 1
				thirst = 0
			else:
				print 'No more water.\n'
		if thirst > 4:
			print 'You are thirsty.\n'
		elif thirst > 6:
			print 'You died of thirst!\n'
			print 'Game Over!\n'
			raw_input('Press Enter to continue!')
			done = True
		if camel_tiredness > 5:
			print 'Your camel is tired.\n'
		elif camel_tiredness > 8:
			print 'Your camel is dead.\n'
			print 'Game Over!\n'
			raw_input('Press Enter to continue!')
			done = True
		if natives_traveled >= miles_traveled:
			print 'Player was caught!\n'
			print 'Game Over!\n'
			raw_input('Press Enter to continue!')
			done = True
		elif natives_traveled < miles_traveled and natives_traveled >= miles_traveled - 15:
			print 'The natives are getting close!\n'
		if miles_traveled >= 200 and camel_tiredness < 8 and natives_traveled != miles_traveled and thirst < 6:
			print 'You win!\n'
			raw_input('Press Enter to continue!')
		
		chance = random.randint(1,21)
		if chance == oasis:
			print 'User found an oasis!\n'
			print 'Refill canteen.\n'
			canteen = 3
			print 'Reset thirst.\n'
			thirst = 0
			print 'Camel rested.\n'
			camel_tiredness = 0
		

		
while True:
	os.system('cls')
	play = raw_input('Would you like to start a new game? ')
	if play.lower() == 'y':
		main()
	elif play.lower() == 'n':
		break
	else:
		continue