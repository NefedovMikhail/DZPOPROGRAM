Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i=input('введите слово:')
введите слово:aaaaaaaaaaaaa
>>> while len(i)>=6:
	print(i[len(i)])
	break
	if len(i)>6:
		print(i[len(i)//2])
		break

	
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    print(i[len(i)])
IndexError: string index out of range
>>> 
