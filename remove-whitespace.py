# Removing White Space from the string ( we use n.strip())

n="        bd bnb sbnds "

x=n.strip()
print(x)


# Removing Space between the string by taking input with user

n = input("Enter a String : ")
r=""

for i in n:
    if i != " ":
        r+=i
print("String after removing the spaces :",r)



# Removing Space between the string by giving input

n = "msdbhshshs bbs bbvf bb b"
r=""

for i in n:
    if i != " ":
        r+=i
print(r)