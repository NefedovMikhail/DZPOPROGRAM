Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
>>> 
>>> print
<built-in function print>
>>> print matrix
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(matrix)?
>>> print (matrix)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		print(matrix[i][j], end=' ')
	print()

	
1 2 3 
4 5 6 
7 8 9 
>>> name = list('иван')
>>> print(name)
['и', 'в', 'а', 'н']
>>> print()

>>> print(list)
<class 'list'>
>>> for i in range(len(name)):
	for j in range(len(name[i])):
		print(name[i][j], end=' ')
	print()

	
и 
в 
а 
н 
>>> name = list('иван')
>>> name1 = name([i][j]=len(name)
	     print ()
	     
SyntaxError: invalid syntax
>>> print(name1)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(name1)
NameError: name 'name1' is not defined
>>> matrix = list('иван')
>>> for i in range(len(matrix)):
	for j in range(len(matrix[i])):
		print(matrix[i][j], end=' ')
	print()

	
и 
в 
а 
н 
>>> enumerate (matrix)
<enumerate object at 0x00F7B268>
>>> print(matrix)
['и', 'в', 'а', 'н']
>>> print list(matrix)
SyntaxError: invalid syntax
>>> list(matrix)
['и', 'в', 'а', 'н']
>>> enumerate (matrix)
<enumerate object at 0x00F76B08>
>>> for elem in matrix:
	print(elem)

	
и
в
а
н
>>> name=input('введите имя: ')
введите имя: иван
>>> name1 = list(name)
>>> name1 = [name1 *  len(name1) for name1 in 'list']
>>> name1
['l', 'i', 's', 't']
>>> name1 = [name1 *  len(name1) for name1 in (name)]
>>> 
>>> name1
['и', 'в', 'а', 'н']
>>> name1 = [name1*len(name1) for name1 in (name)]
>>> name1
['и', 'в', 'а', 'н']
>>> name1 = [name1 *  len(name) for name1 in (name)]
>>> name1
['ииии', 'вввв', 'аааа', 'нннн']
>>> for i in range(len(name1)):
	for j in range(len(name1[i])):
		print(name1[i][j], end=' ')
	print()

	
и и и и 
в в в в 
а а а а 
н н н н 
>>> name2 = list(name1)
>>> print(name2[2::11])
['аааа']
>>> print(name2[2-11, ::2])
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print(name2[2-11, ::2])
TypeError: list indices must be integers or slices, not tuple
>>> print(name2)
['ииии', 'вввв', 'аааа', 'нннн']
>>> name2= list(name1) in range 1
SyntaxError: invalid syntax
>>> name2=list(name1) in range(1)
>>> print(name2)
False
>>> print(name1)
['ииии', 'вввв', 'аааа', 'нннн']
>>> list.reverse(name1)
>>> print(name1)
['нннн', 'аааа', 'вввв', 'ииии']
>>> list.reverse(name1)
>>> print(name1)
['ииии', 'вввв', 'аааа', 'нннн']
>>> print(name1) in range (1)
['ииии', 'вввв', 'аааа', 'нннн']
False
>>> name2=list(name1) in step (1)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    name2=list(name1) in step (1)
NameError: name 'step' is not defined
>>> name2=list.count(name)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    name2=list.count(name)
TypeError: descriptor 'count' for 'list' objects doesn't apply to a 'str' object
>>> 
