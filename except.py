try:
    num = int(input("Enter numerator: "))
    den = int(input("Enter denominator: "))
    result = num/den
except ZeroDivisionError as e:
    # print(e)
    print("You can't devide a number by zero.")
except ValueError as e:
    # print(e)
    print("You can't devide a number by character or special charater value.")
else:
    print(result)
finally:
    print("hello world")

