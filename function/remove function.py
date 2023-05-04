def remove_and_split(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

this = "  tarun is a good   "
n = remove_and_split(this, "tarun")
print(n)