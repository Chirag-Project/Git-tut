# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

# =======================

# clear()	Removes all the elements from the dictionary

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# dict.clear()
# print(dict)

# copy()	Returns a copy of the dictionary

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# dict.copy()
# print(dict)

# fromkeys()	Returns a dictionary with the specified keys and value

# x=("key1","key2","key3")
# y=1
# x=dict.fromkeys(x,y)
# print(x)

# get()	Returns the value of the specified key

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# x=dict.get("key2")
# print(x)

# items()	Returns a list containing a tuple for each key value pair

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# x=dict.items()
# print(x)

# keys()	Returns a list containing the dictionary's keys

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# x=dict.keys()
# print(x)

# values()	Returns a list containing the dictionary's values

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# x=dict.values()
# print(x)

# pop()	Removes the element with the specified key

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# dict.pop("key2")
# print(dict)

# popitem()	Removes the last inserted key-value pair

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# dict.popitem()
# print(dict)

# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value

dict={"key1":"value1","key2":"value2","key3":"value3"}
x=dict.setdefault("key2","cbhcb")
print(x)

# update()	Updates the dictionary with the specified key-value pairs

# dict={"key1":"value1","key2":"value2","key3":"value3"}
# dict.update({"key5":"cbhcb"})
# print(dict)

# n=11
# print(oct(n))

# t=("a","b","c")
# # x=list(t)
# t.append("d")
# # y=tuple(x)
# print(t)

# dict={"key1":"value1","key2":"value1"}
# dict.pop("key1")
# print(dict)