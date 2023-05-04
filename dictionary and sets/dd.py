myDict = {
"fast": 'in a quick manner',
"harry": 'a coder',
"marks": [2,3,3],
"anto": {"ho": "lle"}
}
print(myDict['fast'])
print(myDict["anto"])
print(list(myDict.keys()))
print(list(myDict.values()))
print(myDict.items())
print(myDict)
updateDic = {"y": "u"}

myDict.update(updateDic) # updates the dictionary by adding key_value pairs from updateDict
print(myDict)
# The different between .get and []

print(myDict.get("harry2"))  #Retrun None as harry2 is not present in the dictionary
print(myDict["harry2"])  # throw an error as harry2 is not present in the dictionary
