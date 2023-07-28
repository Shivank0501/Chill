while True:
    a = int(input(" Enter number 1 = "))

    b= int(input(" Enter number 2 = "))

    z = a*b
    y = a//b
    m= a+b
    n = a-b

    k = input("What you want - ADD / Sub / Mul / div")
    if k=="Add":
        print("your anser is :", m)

    elif k=="sub":
        print("Your anser is ", n)

    elif k=="Mul":
        print("Your anser is ", z)

    elif k== "div":
        print("Your anser is ", y)

    else:
        print("Do it right ")

   

    x=input("Wannna try again y/n  ")
    if x== "n" :
        print("Thank you for using it")
        break