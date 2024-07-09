file = open("FilesInPython\data.txt", "a")

while True:
    name = input('Enter name to be added: ')
    file.write('\n'+name+'\n')
    choice = input("Do you want to add more names? (y/n)")
    if choice == 'n':
        file.close()
        break

# write code to read all the names in the file and capitalize them.
file = open("FilesInPython\data.txt", "r")
lines = file.readlines()

for line in lines:
    print(line.strip().capitalize())
    # capitalize every line