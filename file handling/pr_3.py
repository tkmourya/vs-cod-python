with open("line.txt") as f:
    content = f.read()

content = content.replace("donkey", "$%^$$^@")

with open("line.txt", 'w') as f:
    f.write(content)

