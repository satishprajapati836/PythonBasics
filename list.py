data = [1, 2, 10, 34, "Satish", "Ruhan", 55]

print(data[2]) # It will print value on the second index = 10

print(data[1:5]) # It will print values from 1 to 4 index - 5th index is excluded => 2,10,34,"Satish"

print(data[-1]) # Print values on last index

data.append("Nilam")
print(data)

data.insert(1,"Prajapati")
print(data)

data[2] = "PRAJAPATI"
print(data)

del data[2]
print(data)