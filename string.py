str1 = "Satish.com"
str2 = "Prajapati"
str3 = "SatishRuhan"
str4 = "  Nilam  "
# Print third character of the str1 string

print(str1[2])

# Print 1 to 4 number character only from whole string

print(str1[1: 5])

# Add means concat two string

print(str1 + str2)

# Check whether particular string is present in the string or not.

print(str1 in str3)

# Trim the String

print(str4.strip())

# Split the String

print(str1.split("."))

# Remove only left side white space

print(str4.lstrip())

# Remove only Right side white space

print(str4.rstrip())

# Replace the string.


print(str4.replace("Nilam","Replace Nilam with Mansi"))
