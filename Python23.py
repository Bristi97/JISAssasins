#Q23)menu driven program?
X = input("Enter your string")
l=len(X)
print("The length is", l)
Y = " Abc is better than pqr "
Z= X+Y
print("After concatenation", Z)
print(''.join(reversed(X)))
old="Ram is a gud boy"
new=old.replace("gud","bad")
print(new)
if X == Y:
    print("Equal")
else:
    print("Not Equal")