'''Create a python program based on the get input_list = [1,2,3,4,5,6,7,8,9] and we want the list as output
output_list = [1,8,3,6,5,4,7,2,9]'''

#swap two elements in list

# Swap function
def swapList(sl,pos1,pos2,pos3,pos4):      
    sl[pos1], sl[pos2] = sl[pos2], sl[pos1]  
    sl[pos3], sl[pos4] = sl[pos4], sl[pos3]
    return sl
      
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

pos1, pos2 = 2,8
pos3, pos4 = 4,6
print("Given List: ", given_list)
print("Swapp List: ",swapList(given_list,pos1-1,pos2-1,pos3-1,pos4-1))

## outpur:
# Given List:  [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Swapp List:  [1, 8, 3, 6, 5, 4, 7, 2, 9]


print('-------------------------')
input_list = [1,2,3,4,5,6,7,8,9]
output_list = []

for i in range(len(input_list)):
    if i % 2 == 0:
        output_list.append(input_list[i])
        print('In if output_list', output_list)
    else:
        output_list.insert(i-1, input_list[i])
        print('In else output_list', output_list)

print(output_list)
# [2, 1, 4, 3, 6, 5, 8, 7, 9]