def addition(a,b):
             c=a+b
             print(a,"+",b,"=",c)
             return c
def substraction(a,b):
            c=a-b
            print(a,"-",b,"=",c)
            return c

def division(a,b):
            c=a/b
            print(a,"/",b,"=",c)
            return c
def floorDivision(a,b):
            c=a//b
            print(a,"//",b,"=",c)
            return c
def Exponential(a,b):
            c=a**b
            print(a,"^",b,"=",c)
            return c
def multiplication(a,b):
            c=a*b
            print(a,"*",b,"=",c)
            return c


print("\t--MENU--\n1.Addition \n2.Substraction \n3.Multiplication \n4.Division \n5.Floor Division \n6.Exponential\n7.All Calculation Results\n8.Exit\n")
a=int(input("Enter the First Number :"))
b=int(input("Enter the Second Number :"))
while True:
    choice=int(input("Enter the Choice :"))
    if(choice==1):
        addition(a,b)
    elif(choice==2):
        substraction(a,b)
    elif(choice==3):
        multiplication(a,b)
    elif(choice==4):
       division(a,b)
    elif (choice==5):
       floorDivision(a,b)
    elif(choice==6):
        Exponential(a,b)
    elif(choice==7):
        print("\n--All Results--\n")
        print(f"Addition  = {addition(a,b)}")
        print(f"Substraction ={substraction(a,b)}")
        print(f"Product ={multiplication(a,b)}")
        print(f"Division ={division(a,b)}")
        print(f"Floor Division ={floorDivision(a,b)}")
        print(f"Power ={Exponential(a,b)}")
    elif(choice==8):
        break
    else:
        print("Invalid Choice")


