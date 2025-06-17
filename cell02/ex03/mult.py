num1 = int(input("Enter tne first number: "))
num2 = int(input("Enter the second number "))
result = num1*num2 
print(f"{num2} X {num2} - {num1 * num2}")
if num1 * num2> 0:
    print("The result ls positive.")
elif num1 * num2 <0:
    print("The result ls negative")  
else:
    print("The result is positive and negative")      