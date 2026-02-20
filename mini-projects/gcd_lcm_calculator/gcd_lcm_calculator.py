number1=int(input("Enter the first number:"))
number2=int(input("Enter the second number:"))
smaller_number=min(number1,number2)
for i in range(smaller_number,0,-1):
    if(number1%i ==0 and number2%i ==0):
        gcd=i
        break
lcm=(number1*number2)/gcd
print(f"The GCD of {number1} and {number2} is {gcd}")
print(f"The LCM of {number1} and {number2} is {lcm}")