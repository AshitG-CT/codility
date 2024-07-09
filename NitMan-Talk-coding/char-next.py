'''input: a4k3b2 
output:aeknbd'''
# abcd e fghijklm n bc d
def strTranform(s):
    output = ''
    for x in s:
        if x.isalpha():
            output = output+x
            previous = x
        elif x.isdigit():
            print('ord ', ord(previous))
            print('chr ',chr(ord(previous)))
            newch = chr(ord(previous)+int(x)) 
            output = output+newch
    return output

print(strTranform('a4k3b2'))


''''''