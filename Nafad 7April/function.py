def cubeVolume(sidelen):
    volume = sidelen**3
    return volume

def areaRec(w,l):
    area = w*l
    return area


cubelen=int(input("Enter The cube length: "))
reclen = int(input("Enter Rectangle length: "))
recwid = int(input("Enter Rectangle length:"))

v1 = cubeVolume(cubelen)
a1= areaRec(reclen,recwid)

print("The Volum of the cube is :",v1)
print("The Area of Rectangle is :",a1)