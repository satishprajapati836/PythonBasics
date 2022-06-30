try:
    with open('test.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("Finally block code executed")