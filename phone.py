

#digit1 = input("Enter first digit:\n")
#digit2 = input("Enter second digit:\n")
#digit3 = input("Enter third digit:\n")
#digit4 = input("Enter fourth digit:\n")
#digit5 = input("Enter fifth digit:\n")
#digit6 = input("Enter sixth digit:\n")
#digit7 = input("Enter eight digit:\n")
#digit9 = input("Enter nineth digit:\n")
#digit10 = input("Enter tenth digit:\n")


#def phonenumber(digit1,digit2,digit3,digit4,digit5,digit6,digit7,digit8,digit9,digit10):
#    if digit1 == A or digit1 == B or digit1 == C:
#        print(2)
#    else:
#       print(digit)
    

    


numbers = input("Input number: ")
print(numbers)
uppernumbers = numbers.upper()
def split(phonenumber):
    return [char for char in uppernumbers]
phonenumber = split(uppernumbers)

def lennumber(phonenumber):
    if len(phonenumber) < 12:
        print("Input number is illegal and can not be converted.")
        return
lennumber(phonenumber)


def randomnumber(phonenumber):
    n = 0
    for n in range(12):
        if phonenumber[n] == 'A' or phonenumber[n] == 'B' or phonenumber[n] == 'C':
            phonenumber[n] = '2'
        if phonenumber[n] == 'D' or phonenumber[n] == 'E' or phonenumber[n] == 'F':
            phonenumber[n] = '3'
        if phonenumber[n] == 'G' or phonenumber[n] == 'H' or phonenumber[n] == 'I':
            phonenumber[n] = '4'
        if phonenumber[n] == 'J' or phonenumber[n] == 'K' or phonenumber[n] == 'L':
            phonenumber[n] = '5'
        if phonenumber[n] == 'M' or phonenumber[n] == 'N' or phonenumber[n] == 'O':
            phonenumber[n] = '6'
        if phonenumber[n] == 'P' or phonenumber[n] == 'Q' or phonenumber[n] == 'R' or phonenumber[n] == 'S':
            phonenumber[n] = '7'
        if phonenumber[n] == 'T' or phonenumber[n] == 'U' or phonenumber[n] == 'V':
            phonenumber[n] = '8'
        if phonenumber[n] == 'W' or phonenumber[n] == 'X' or phonenumber[n] == 'Y' or phonenumber[n] == 'Z':
            phonenumber[n] = '9'
       
    return
randomnumber(phonenumber)

def legal(phonenumber):
 if len(phonenumber) > 12:
    print("Input number is illegal and can not be converted.")
 elif len(phonenumber) < 12:
    print("Input number is illegal and can not be converted.")
 elif phonenumber[2] == '-' or phonenumber[4] == '-' or phonenumber[5] == '-' or phonenumber[6] == '-' or phonenumber[8] == '-' or phonenumber[9] == '-' or phonenumber[10] == '-' or  phonenumber[11] == '-':
     print("Input number is illegal and can not be converted.")
 else:
     listToString = ''.join([str(elem) for elem in phonenumber])
     print("New number:  ",listToString)
 

 return
legal(phonenumber)


    



    

    


        
        


    
