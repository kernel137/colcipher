import sys
#---------
key: int = 0
custom_key_flag: bool = False
#----------------------
encrypt_flag: bool = True
decrypt_flag: bool = False
#-------------------
output_to_file_flag: bool = False
#--------------------------
input_string: str = ""
input_filename: str = ""
#------------------
output_list: list = []
output_string: str = ""
output_filename: str = "output.txt"
#-----------------------------

def collatz(it):
	if it%2 == 1: return 3*it + 1
	else: return it//2

def encrypt(sentence):
	csn = it = int(sum([ord(letter) for letter in sentence])) if not custom_key_flag else key
	out = [csn] if not custom_key_flag else []
	for letter in sentence:
		numFound = False
		count = 0
		while not numFound:
			if it == 1:
				csn += 1
				it = csn
			while it > 1:
				it = collatz(it)
				count+=1
				if it % 128 == ord(letter):
					numFound = True
					out.append(count)
					break
	return out

def decrypt(string):
	numbers = string.split(" ")
	numbers = [int(i) for i in numbers] 
	csn = it = numbers.pop(0) if not custom_key_flag else key
	out = ""
	for i in range(len(numbers)):
		count = 0
		while True:
			if it == 1:
				csn+=1
				it = csn
			it = collatz(it)
			count+=1
			if count == numbers[i]:
				out += chr(int(it%128))
				break
	return out
#========================================================================

if(len(sys.argv) == 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help"):
	helpPage = """Usage: colcipher [-edsh] [-k number] [INPUT]
Encrypt or decrypt text utilizing collatz iteration.
Allowed input is text through command-line arguments or files.

With no flags, first and only argument is used as text and is encrypted by
default and printed to the console.

  -t, --text        Reads text from next command-line argument as input
  [-t "text"] [--text "text"]
  -f, --file        Takes input from file and outputs to file
  [-f "input.txt"] [--file "input.txt"]
  -o, --output      Output to file and choose file name
  [-o "output.txt"] [--output "output.txt"]
  -e, --encrypt     Encrypt input
  -d, --decrypt     Decrypt input
  -k, --key         Choose custom key for encryption or decryption
  [-k number] [--key number]
  -s                Output to console instead of file.
  -h, --help        Print this text and exit

Keys are usually integers but can also be ASCII text.
When ASCII text is used as a key, the ASCII values of each character
are summed up and the integer is then used as the key.

Default output filename is "output.txt". If used twice or more times with 
the same filename, output will overwrite the file.

Use -s if you're reading from a file but want the output in the console.

Examples:
  colcipher "Test input text"         Encodes text and prints output to console.
  colcipher -d -t "448 26 14 613 123" Decodes text and prints output to console.
  colcipher -e -f "./plain.txt" -o "secret.txt"           Takes input from file 
  "plain.txt" and outputs encoded text into secret.txt in the same directory.
  colcipher -e -k 2953 -f "plain.txt" -o "encrypted.txt"  Encrypts "plain.txt"
  using custom key and outputs into "encrypted.txt".
"""
	print(helpPage)
	exit()
#==============[Options Processing]==============
if(len(sys.argv) == 2):
	input_string = sys.argv[1]

if("-t" in sys.argv or "--text" in sys.argv):
	input_string = sys.argv[sys.argv.index("-t")+1] if "-t" in sys.argv else sys.argv[sys.argv.index("--text")+1]

elif("-f" in sys.argv or "--file" in sys.argv):
	output_to_file_flag = True
	input_filename = sys.argv[sys.argv.index("-f")+1] if "-f" in sys.argv else sys.argv[sys.argv.index("--file")+1]
	with open(str(input_filename)) as file:
		input_string = str(file.read())
	

if("-o" in sys.argv or "--output" in sys.argv):
	output_to_file_flag = True
	output_filename = sys.argv[sys.argv.index("-o")+1] if "-o" in sys.argv else sys.argv[sys.argv.index("--output")+1]

if("-e" in sys.argv or "--encrypt" in sys.argv):
	encrypt_flag = True
	decrypt_flag = False

elif("-d" in sys.argv or "--decrypt" in sys.argv):
	encrypt_flag = False
	decrypt_flag = True

if("-k" in sys.argv or "--key" in sys.argv):
	custom_key_flag = True
	key = str(sys.argv[sys.argv.index("-k")+1]) if "-k" in sys.argv else str(sys.argv[sys.argv.index("--key")+1])
	if(key.isnumeric()): key = int(key)
	else: key = int(sum([ord(letter) for letter in key]))

if("-s" in sys.argv):
	output_to_file_flag = False
#==================[Processing]==================
if(encrypt_flag):
	output_list = encrypt(input_string)
	output_string = ' '.join([str(x) for x in output_list])
elif(decrypt_flag):
	output_string = decrypt(input_string)
#====================[Output]====================
if(output_to_file_flag):
	with open(str(output_filename), "w") as file:
		file.write(output_string)
else:
	print(output_string)