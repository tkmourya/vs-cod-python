words = ["donkey",'kaddu',"mote"]

with open("line.txt",) as f:
    content = f.read()
for word in words:
    content = content.replace(word, "$%^$$^@")

with open("line.txt", 'w') as f:
    f.write(content)

