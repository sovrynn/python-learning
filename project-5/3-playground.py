# Reading Files
file = open('txt-files/5-read-file.txt', 'r')
print(file.read())
file.close()

# Appending to Files
file = open('txt-files/5-append-file.txt', 'a')
file.write('This is extra file content')
file.close()

# Writing to Files
file = open('txt-files/5-write-file.txt', 'w')
file.write('Overwriting file content')
file.close()
