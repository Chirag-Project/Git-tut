# find the vowel from the sentences

n=input("enter the character:")

vowel=0

for i in n:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowel=vowel+1
print("no. of vowel:",vowel)

# find the length of sentences

x=len(n)
print(x)


