def collatz(it):
	if it%2 == 1:
		return int((3*it) + 1)
	else:
		return int(it/2)

string = str(input("Input: "))
numbers = string.split(" ") # from string to list
numbers = [int(i) for i in numbers] # casting list members to integer

# csn -> current starting number
# it -> iterator
csn = it = numbers.pop(0) # popping starting number

for i in range(len(numbers)):
	count = 0
	while True:
		#==========
		# changing starting number
		# when iterator reaches 1
		if it == 1:
			csn+=1
			it = csn
		#==================
		# collatz iteration
		it = collatz(it)
		count+=1
		#=======
		if count == numbers[i]:
			print(chr(int(it%128)), end="")
			break
		#==================================
		

print()
