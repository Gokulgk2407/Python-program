def calculator():
    print("Select Operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Division")
    print("5.Square")
    print("6.Modulus")
    choice=input("Enter choice (1/2/3/4/5/6):")
    if choice in ['1','2','3','4','5']:
        num1=int (input("Enter the First Number:"))
        num2=int (input("Enter the Second Number:"))
    if choice=='1':
        print(f"{num1}+{num2}={num1+num2}")
    elif choice=='2':
        print(f"{num1}-{num2}={num1-num2}")
    elif choice=='3':
         print(f"{num1}*{num2}={num1*num2}")
    elif choice=='4':
         print(f"{num1}/{num2}={num1/num2}")
    elif choice=='6':
         print(f"{num1}%{num2}={num1%num2}")
    elif choice=='5':
        num=int(input("Enter the Number"))
        print(f"The square of {num} is={num**2}")
    else:
        print("Invalid Input")
calculator()
              
              
    

