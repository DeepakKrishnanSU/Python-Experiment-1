for row in range(0,7):
    for column in range(0,4):
        if row==0 or row==3 or row==6 or column==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()