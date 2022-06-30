# To Read or Write in file you have to first open the file

file = open('test.txt')

# Read all the content from file
#file.read()

#print(file.read())

# Read n number of character by passing parameter

#print(file.read(5))

# Read one single line at a time from file

print(file.readline())
file.close()