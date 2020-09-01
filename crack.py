import hashlib
import platform

if (int(platform.python_version_tuple()[0]) < 3):
	try: input = raw_input
	except NameError: raw_input = input

flag = 0

pass_hash = input("Enter md5 hash : ")
wordlist = input("Enter wordlist file name : ")

try:
	pass_file = open(wordlist, "r")
except:
	print("\nWordlist file not found !\n")
	quit()

for word in pass_file:
	
	enc_word = word.encode('utf-8')
	digest = hashlib.md5(enc_word.strip()).hexdigest()

	if digest == pass_hash:
		print("\nPassword found!")
		print("Password is : " + word + "\n")
		flag = 1
		break

if flag == 0:
	print("\nPassword not found in wordlist\n")
