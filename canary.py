import random
import sys

def canary(text):
	start_index = None
	for i, x in enumerate(text):
		if x == "{":
			start_index = i
		if x == "}":
			if start_index == None:
				print("File was inproperly formatted!")
				exit(0)
			return canary(text[:start_index] + random.choice(text[start_index+1:i].split("|")) + text[i+1:])
	return text

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print("usage: provide an argument of a templated file to read")
		exit(0)
	print(canary(open(sys.argv[1],"r").read()))