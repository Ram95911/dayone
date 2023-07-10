def checker_number_type(num):
    num=num.strip()
    if all(char in '01' for char in num):
        return "Binary"
    if num.isdigit():
        return "Decimal"
    try:
        int(num,16)
        return "Hexadecimal"
    except ValueError:
        pass
    
    return "Invalid"
def DecimalToOctal(num):
    if(num>0):
        DecimalToOctal(int(num/8))
        print(num%8,end="")

def DecimalToBinary(num):
    if(num>0):
        DecimalToBinary(int(num/4))
        print(num%4,end="")
def DecimalToHexadecimal(num):
    convertion_table={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',
                      6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',
                      12:'C',13:'D',14:'E',15:'F'}
    if num<=0:
        return ''
    rem=num%16
    return DecimalToHexadecimal(num//16) + convertion_table[rem]
    
while True:
    print("\nNumber opertions \n 1.Number type \n 2.Decimal To Octal \n 3.Decimal To Binary \n 4.Decimal To Hexadecimal \n 5.Exit")
    choice=int(input("Enter the Choice: "))
    if choice==1:
        num=input("Enter the number to check number type: ")
        type=checker_number_type(num)
        print("Type:"+type+" number")
    elif choice==2:
        num=int(input("Enter the Number: "))
        DecimalToOctal(num)
        #print("Octal number:",octal)
    elif choice==3:
        num=int(input("Enter the Number: "))
        DecimalToBinary(num)
        #print("Binary number:",binr) 
    elif choice==4:
        num=int(input("Enter the Number: "))
        hexa=DecimalToHexadecimal(num)
        print("Hexadecimal number is: ",hexa)
    elif choice==5:
        break
    else:
        print("Incorrect Option please correct Option") 