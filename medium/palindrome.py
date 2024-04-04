# Question 1: Write a Python program to check if a string is a palindrome.
# https://medium.com/@nikitasilaparasetty/python-interview-coding-questions-with-solutions-for-beginners-7f6d782defac
def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string

# Test the function
word = "carac"
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")