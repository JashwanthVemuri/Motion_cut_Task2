def temp_convert(data,choice):
    try:
        x=int(data)
        y=int(choice)
        if y==1:
            res=(x-32)*(5/9)
            print(res)
        elif y==2:
            res=(x*1.8)+32
            print(res)
        else:
            print("Invalid Choice")
    except:
        print("Invalid Data")


inp=input()
print("1. Convert to Celsius\n 2.Convert to Farenheit")
sel=int(input("Enter your choice: "))
temp_convert(inp,sel)