letter = '''dear <|name|>,
you are selected

date: <|date|>
'''
name = input("enter your name\n")
date = input("enter date\n")
letter = letter.replace("<|name|>",name)
letter = letter.replace("<|date|>",date)
print(letter)

