# file = open('FilesInPython\HelloWorld.txt', 'r')
# # content = file.read()
# content2 = file.readline()
# # print(content)
# print(content2)
# file.close()

with open('FilesInPython\HelloWorld.txt', 'r') as file:
    contents = file.read()

print(contents)

# for line in contents:
#     print(line.strip())
with open('FilesInPython\HelloWorld.txt', 'w') as file:
    file.write('Hello it is new 2nd line added.')

with open('FilesInPython\HelloWorld.txt', 'a') as file:
    file.write('\nHello it is second3rd line added.')