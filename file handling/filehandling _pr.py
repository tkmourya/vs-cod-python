# r  use read
# w  use write new text file
# a use for append   adding lines




f = open("gy.txt", "r")
data = f.read()
print(data)
f.close()