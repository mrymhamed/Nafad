h1 = int(input("Enter the hour of the first time : "))
m1 = int(input("Enter the min of the first time : "))
h2 = int(input("Enter the hour of the second time : "))
m2 = int(input("Enter the min of the second time : "))

print("Time 1 is ",h1,":",m1)
print("Time 2 is " ,h2,":",m2)

if (0<=h1 <=23) and (0 <= h2 <= 23) and (0 <= m1 <= 59) and (0 <= m2 <= 59):
    if h1==h2 and m1>m2 :
        print("Time 2 come first")
    elif h1==h2 and m1<m2 :
        print("Time 1 come first")
    elif h1>h2:
        print("Time 2 come first")
    else:
        print("Time 1 come first")

else:
    print("Invaild input ")
