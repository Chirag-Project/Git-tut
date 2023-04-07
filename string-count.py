#taking string as an input from the user
string = input("Enter a String : ")
alphabets=0
digits=0
specialChars=0
#checks for each character in the string
for i in string: 
	#if character of the string is an alphabet
    if i.isalpha():
       	alphabets=alphabets+1
    elif i.isdigit():
        digits=digits+1
    else: #if character of the string is a special character
        specialChars=specialChars+1
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)
