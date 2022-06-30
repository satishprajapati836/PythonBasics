# Program Read the file
# Reverse the file content
# Write Reversed content in the file

with open('test.txt','r') as reader:
    content = reader.readlines()
    print(content)

    with open('test.txt','a') as writer:
        for line in reversed(content):
         writer.write(line)
