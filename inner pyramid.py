# Part 6.3 ProgramArcadeGames.com
# by Tim Griffith


def main():
	start = 0
	space = 5
	answer = raw_input('Enter the pyramid size please. (1-9): ')
	result = []
	
	count = 1
	while len(result) != int(answer):
	    if count % 2 != 0:
	        result.append(count)
	        count += 1
	    else:
	        count += 1
	        continue
			
	newResult = ' '.join(str(e) for e in result).replace('[],', ' ')
	end = len(newResult)
			
	for index, num in enumerate(newResult):
	    if num == ' ':
	        continue
	    elif index == 0 or index == (len(newResult) * 2) - 1:
	        print newResult[start:] + ' ' + newResult[::-1]
	        start += 1
	    else:
	        printME=newResult[index:]+(' ' * space)+newResult[:index - 1:-1]
	        print printME
	        if start != len(result) - 1:
	            space += 4
	            start += 1
	    if int(num) == end:
	        #space = 17
	        for place, digit in enumerate(newResult):
	            #if digit == '':
	            #    continue
	            if place != len(newResult) * 2:
	                if index == 0:
	                    print newResult + ' ' + newResult
	                    break
	                else:
	                    printME = newResult[index:] + (' ' * space) + newResult[:index - 1:-1]
	                    print printME
	                space -= 4
	                index -= 2
	            else:
	                break
		
main()