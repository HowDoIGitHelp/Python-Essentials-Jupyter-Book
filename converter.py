print('Enter a float')
value = float(input())

conversion = (9/5) * value + 32

if value < 0:
	print(str(conversion) + ' degrees fahrenheit cold')
elif value > 100:
	print(str(conversion) + ' degrees fahrenheit hot')
else:
	print(str(conversion) + ' degrees fahrenheit')