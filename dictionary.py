#creating dictionary
a = {'apple': 55, 'banana': 10, 'orange': 8}

#adding key-value pair "grape"
a['grape'] = 12

#remove key-value "banana"
a.pop("banana")

#Checking If a is still there
if "apple" in a:
    print("Apple exists in the dictionary.")
else:
    print("Apple does not exist in the dictionary.")

#Printing both the keys and the values together
print("Keys and Values:", a.items())

