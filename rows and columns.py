# Lab 6 ProgramArcadeGames.com
# By Tim Griffith

def main():
	row = raw_input('How many rows do you want to print? ')
	row = int(row)
	#column = 1
	number = 10
	printThis = ''
	newResult = []

	for num in range(1, row + 1):
		result = range(number, number + num)
		newResult.append(result)
		number += num
	for item in newResult:
		item = ' '.join(str(e) for e in item).replace('[],', ' ')
		printThis += str(item) + '\n'
	print printThis
main()