'''
	The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

	P   A   H   N
	A P L S I I G
	Y   I   R

	And then read line by line: "PAHNAPLSIIGYIR"
'''

# class Solution(object):
def convert(s, numRow):
	if numRow == 1:
		return s

	result = ["" for _ in range(numRow)]
	print('result : ', result)
	row, down = 0, 1
	for char in s:
		result[row] += char
		if row == numRow - 1:
			down = 0
		if row == 0:
			down = 1
		
		if down:
			row+=1
		else:
			row-=1
	final_string = ""
	for value in result:
		final_string += value
	return final_string

print(convert("PAYPALISHIRING",3))

'''Output:
PAHNAPLSIIGYIR
'''