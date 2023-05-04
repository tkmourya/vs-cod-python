f = open('line.txt')
t = f.read()
if 'once' in t:
    print("once is present")
else:
    print("once is not present")
f. close()