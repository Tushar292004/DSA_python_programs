#area and semiperimeter of trangle
# sides = [float(input("Enter the side {0} = ".format(i+1))) for i in range(3)]
# sp=(sides[0]+sides[1]+sides[2])/2    
# print("Semi-Perimeter : {0} \nArea : {1}".format(sp,(sp*(sp-sides[0])*(sp-sides[1])*(sp-sides[2]))**0.5))

#greatest among 3 numbers
n = [float(input("Enter the number {0} = ".format(i+1))) for i in range(3)]
if(n[0]>=n[1] and n[0]>=n[2]):
    print(n[0], "is greatest")
elif(n[1]>=n[2]):
    print(n[1], "is greatest")
else:
    print(n[2], "is greatest")





