print('Enter three values:')

value1 = float(input())
value2 = float(input())
value3 = float(input())

mean = (value1 + value2 + value3)/3

if mean < 0:
	print('Negative mean')
elif mean > 0:
	print('Positive mean')
else:
	print('Zero mean')
