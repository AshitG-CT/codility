'''
	Given a string, find the length of the longest substring without repeating characters.

	Examples:

	Given "abcabcbb", the answer is "abc", which the length is 3.

	Given "bbbbb", the answer is "b", with the length of 1.

	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def lengthOfLongString(s):
    
    temp, result = 0, 0
    mapDict = {}
    for char in range(len(s)):
        print('s[char] : ',s[char])
        if s[char] in mapDict:
            print('1st temp', temp)
            temp = max(mapDict[s[char]], temp)
            print('2nd char, temp', char, temp)
        result = max(result, char-temp+1)
        print('result: ', result)
        mapDict[s[char]] = char+1
        print('mapDict: ',mapDict)
    return result

# print(lengthOfLongString("abcabcbb"))
# print(lengthOfLongString("bbbbb"))
print(lengthOfLongString("pwwkew"))