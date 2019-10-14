weight = int(input("Enter Your Weight: "))
val = input("(L)bs or (K)g: ")

if val.upper() == 'L':
    con = weight * 0.453
    print(f'You are {con} kilos ')
elif val.upper() == 'K':
    con = weight * 2.20
    print(f'You are {con} pounds ')


