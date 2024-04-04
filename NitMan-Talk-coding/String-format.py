# Modify String Format:
# Input = I_Am_A_Coder
# OutPou = i.aM.a.cOODER

# Input = This_Is_Goodd_Morngin
# Output= tHIS.iS.gOOD.mORNING

'''
CHANGEs _ to .
First_upper_letter = remaining_upper_letter
'''

# Using List
def string_format(s):
    l = []
    temp = s.split('_')
    for i in temp:
        l.append(i[0].lower() + i[1:].upper())
    s = '.'.join(l)
    print(s)

s = 'I_Am_A_Coder'
string_format(s)


# Using string
def string_format2(s):
    new_s = ''
    temp = s.split('_')
    for i in temp:
        new_s = new_s+i[0].lower()+i[1:].upper()+'.'
    new_s = new_s[:-1] # remove last dot .
    print(new_s)

s = 'This_Is_Good_Morngin'
string_format2(s)