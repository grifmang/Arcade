# Part 6.2 ProgramArcadeGames.com
# by Tim Griffith

def main():
	counter = 1
	answer = int(raw_input('How big of a box do you want? '))
	double = int(answer * 2)
	minus = int(double) - 2
	for num in range(1, int(answer) + 1):
		if counter == 1 or counter == answer:
			print 'o' * double
			counter += 1
		else:
			print 'o' + (' ' * minus) + 'o'
			counter += 1

main()