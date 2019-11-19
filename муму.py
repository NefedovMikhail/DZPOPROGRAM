    with open('C:/python/mumu.txt', encoding='utf-8') as f:
	text=f.read()
	length = len(text)
	lower = upper = 0
	for i in text :
		if i.islower():
			lower += 1
		elif i.isupper():
			upper += 1
	per_lower = lower / length * 100
	per_upper = upper / length * 100
	print('Upper: %.2f%%' % per_upper)
