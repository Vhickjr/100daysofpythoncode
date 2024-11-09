print("welcome to the tip calculator")
x = float(input("what is the total bill ? "))
y= float(input("what percentage tip will you like to give 10, 12, or 15?"))
x = float((y/100)*x + x)
'''
if y ==10:
    x= float(0.1*x +x)
elif y ==12:
    x= float(0.12*x +x)
else:
     x= float(0.15*x +x)
'''

z = float(input("how many people will slit the bill ? "))
print("each person should pay: ", round(float(x/z),2))
