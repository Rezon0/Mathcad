import math
maximum = 0
def issimple(a):
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if a%i==0:
            if issimple(i)==[]:
                lst.append(i)
    return lst
r=issimple(600851475143)
print("\n" + "Наибольший простой делитель: " + str(max(r)))