x=5
if (type(x)is int):
    print ( "true")
else:
    print("false")

print("-----------------------------------")

x=5.0
if (type(x)is not float):
    print("true")
else:
    print ("False")

print("-----------------------------------")

x=20
y=20

if (x is y):
    print ("x&y same identety")

y=30

if (x is not y):
    print("x & y  have diffrent identaty")