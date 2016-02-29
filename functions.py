# Lab 9 Functions ProgramArcadeGames.com
# by Tim Griffith

import random

def min3(a,b,c):
	lowest = 0
	if a < b and a < c:
		lowest = a
	elif b < a and b < c:
		lowest = b
	else:
		lowest = c
	return lowest
	
def box(a,b):
	for num in range(1, int(a) + 1):
		print '*' * int(b)
			
def find(list, number):
	for index, num in enumerate(list):
		if num == number:
			print 'Found ' + str(number) + ' at position ' + str(index)

def create_list(list_size):
	result = []
	for num in range(1, int(list_size) + 1):
		result.append(random.randint(1,6))
	return result
	
def count_list(list, number):
	count = 0
	for num in list:
		if num == number:
			count += 1
	return count
	
def average_list(list):
	average = len(list) 
	sum = 0
	for num in list:
		sum += num
	return sum / average
	
bigList = create_list(10000)
print count_list(1)
print count_list(2)
print count_list(3)
print count_list(4)
print count_list(5)
print count_list(6)
print average_list(bigList)