# Important: this syntax will create an empty dictionary and not an empty set 
a = {}
print(type(a))
   

   # An empty set can be created using the below syntex:
b = set()
print(type(b))

#  Adding value an aempty set
b.add(4)
b.add(5)
b.add(5)
b.add(5)  # Adding a value repeatedly does not change a set
# b.add([3,2,5])  not add list
# b.add({4:5}) not add dictionary
b.add((4,5))
print(b)
print(len(b))

# remove item
b.remove(5)  # remove 5 from b
b.remove(11) #  throw key error not remove 11 becouse 11 not exist in b
print(b)
