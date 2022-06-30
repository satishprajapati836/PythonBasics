try:
    with open('test11.txt','r') as reader:
        reader.read()
# except: This is used to write our customized message when code goes into except bloc
   # print("Reached to this block because testcase failed in try section")

# Catch the Python default message and print in in python we will use except in place of catch.

except Exception as e:
    print(e)