letter = input()
vowel = ['a','e','i','o','u']
cons = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
letter = letter.lower()
if letter in vowel:
	print("Vowel")
elif letter in cons:
	print("Consonant")
else:
	print("Invalid")
