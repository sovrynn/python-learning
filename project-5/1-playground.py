# Split by whitespace
str1 = 'the first apple off the tree.'
words = str1.split()
print(words)

# What happens if we have multiple whitespaces in a row?
str2 = '  so    many  whitespaces   !'
words = str2.split()
print(words)

# We can specify the separator
str3 = 'words, separated,  by, commas'
words = str3.split(',')
print(words)

# What happens if we have multiple separators in a row?
str4 = ',many,, commas,,, here'
words = str4.split(',')
print(words)
