print("\n")
print("This program will factorize a third-degree polynomial equation of the form ax³+bx²+cx+d\n")

hornercheck = False
while hornercheck == False:
    condition = True
    while condition: #checking if the polyonym is of the third-degree
        a = int(input("Give a: "))
        if a != 0:
            condition = False
        else:
            print("The polyonym cannot be of the third-degree if 'a' is 0! Please input another number!\n")
    #now that a != 0, input the other numbers
    b = int(input("Give b: "))
    c = int(input("Give c: "))
    d = int(input("Give d: "))

    #check from 1 through 1000 if there is a solution, if not, check from -1 to -1000
    r = 0 
    #r for horner, will increase or decrease by 1
    horner = 1 
    #when horner equals zero, it means the polyonym can be factorized with current r
    solved = False
    while solved == False and r < 1000:
        r += 1
        horner = (((a * r) + b) * r + c) * r + d
        if horner == 0:
            solved = True
        
    while solved == False and r < -1000:
        r -= 1
        print(f"DEBUG!: The r for this check is: {r}")
        horner = (((a * r) + b) * r + c) * r + d
        if horner == 0:
            solved = True    

    hornerA = a
    hornerB = (a * r) + b
    hornerC = (((a * r) + b) * r + c)
    #These will be used for (x-r)(hornerA + hornerB + hornerC)


    if solved == True:
        hornercheck == True
        if hornerA != 1 and hornerA != -1:
            if hornerA > 1:
                if hornerB < 0:
                    if hornerC < 0: 
                        print(f"The factorized polyonym is: (x{-r})({hornerA}x\u00B2{hornerB}x{hornerC}), with r= {r}!")
                    else:
                        print(f"The factorized polyonym is: (x{-r})({hornerA}x\u00B2{hornerB}x+{hornerC}), with r= {r}!")
                elif hornerB > 0:
                        print(f"The factorized polyonym is: (x{-r})({hornerA}x\u00B2+{hornerB}x+{hornerC}), with r= {r}!")
            elif hornerA < -1:
                if hornerB < 0:
                    if hornerC < 0: 
                        print(f"The factorized polyonym is: (x{-r})(-{hornerA}x\u00B2{hornerB}x{hornerC}), with r= {r}!")
                    else:
                        print(f"The factorized polyonym is: (x{-r})(-{hornerA}x\u00B2{hornerB}x+{hornerC}), with r= {r}!")
                elif hornerB > 0:
                        print(f"The factorized polyonym is: (x{-r})(-{hornerA}x\u00B2+{hornerB}x+{hornerC}), with r= {r}!")
        else:
            if hornerA == 1:
                if hornerB < 0:
                    if hornerC < 0: 
                        print(f"The factorized polyonym is: (x{-r})(x\u00B2{hornerB}x{hornerC}), with r= {r}!")
                    else:
                        print(f"The factorized polyonym is: (x{-r})(x\u00B2{hornerB}x+{hornerC}), with r= {r}!")
                elif hornerB > 0:
                        print(f"The factorized polyonym is: (x{-r})(x\u00B2+{hornerB}x+{hornerC}), with r= {r}!")
            elif hornerA == -1:
                if hornerB < 0:
                    if hornerC < 0: 
                        print(f"The factorized polyonym is: (-x{-r})(x\u00B2{hornerB}x{hornerC}), with r= {r}!")
                    else:
                        print(f"The factorized polyonym is: (-x{-r})(x\u00B2{hornerB}x+{hornerC}), with r= {r}!")
                elif hornerB > 0:
                        print(f"The factorized polyonym is: (-x{-r})(x\u00B2+{hornerB}x+{hornerC}), with r= {r}!")                                       
        from math import sqrt
        x1 = r
        x2 = (-hornerB + sqrt (hornerB ** 2 - 4 * hornerA * hornerC)) / (2 * hornerA)
        x3 = (-hornerB - sqrt (hornerB ** 2 - 4 * hornerA * hornerC)) / (2 * hornerA)
        print(f"The x for the equation are {x1},{x2} and {x3}")                   
    else:
        print("This polyonym doesn't have an integer x that verifies the equation! Please give another polyonym.\n")