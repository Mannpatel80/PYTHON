amount=int(input("PLese enter amount of withdraw: "))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

print("this is how many 100 notes", note1)
print("this is how many 50 notes", note2)
print("this is how many 10 notes", note3)

