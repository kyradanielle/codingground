file = open("newfile.txt", "w")

file.write("hello world")

file.close()

file = open('newfile.txt', 'r')

print file.read()


file = open("blank.txt", "w")

file.write(" ")
file.close()

fh = open("blank.txt","w")
fh.write("newfile.txt")
fh.close()