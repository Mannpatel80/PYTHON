mark1=int(input("what is your mark"))
mark2=int(input("what is your mark"))
mark3=int(input("what is your mark"))
mark4=int(input("what is your mark"))
mark5=int(input("what is your mark"))

tot=mark1+mark2+mark3+mark4+mark5
avg=tot/5

if avg>=91 and avg<=100:
    print("a1")
elif avg>=81 and avg<=91:
    print("a2")
elif avg>=71 and avg<=81:
    print("b1")
elif avg>=61 and avg<=71:
    print("b2")
elif avg>=51 and avg<=61:
    print("c1")
elif avg>=41 and avg<=51:
    print("c2")
elif avg>=31 and avg<=41:
    print("a1")

elif avg>=21 and avg<=31:
    print("a1")

elif avg>=0 and avg<=21:
    print("a1")

else:
    print("invalid input")