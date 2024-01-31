def collatz(it):
	if it%2 == 1:
		return int((3*it) + 1)
	else:
		return int(it/2)

sentence = str(input("Input: "))

# =[Generating starting number]=
# csn -> current starting number
csn = it = int(sum([ord(letter) for letter in sentence]))
# it -> iterator
#==================
print(csn, end=' ')
#======================
for letter in sentence:
	numFound = False
	count = 0
	while not numFound:
		if it == 1:
			csn += 1
			it = csn
		while it > 1:# collatz cycles at 4, 2, 1
			# collatz iteration
			#==================
			it = collatz(it)
			#================
			count+=1
			#=======
			if it % 128 == ord(letter):
				numFound = True
				print(count, end=" ")
				break
#====================
print()