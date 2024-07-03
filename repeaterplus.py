print('Enter a string')
s = input()
print('Enter an integer')
n = int(input())

repeatedString = s * n

if len(repeatedString) <= 20:
	print(repeatedString)
else:
	print('Too long cannot print')