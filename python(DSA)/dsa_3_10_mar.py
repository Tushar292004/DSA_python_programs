n = int(input("Enter the number of elements you want : "))

roll_no=[(input("Enter the element {0} = ".format(i+1))) for i in range(n)]

flag = 0

find_no = input("Enter the roll numbers which you want to find : ")

if (len(roll_no) == 0):
    print("List is empty")


else:
    for i in roll_no:
        if (i == find_no):
            print("{0} number is present in the list.".format(find_no))
            flag = 1
            break    
    if (flag == 0 ):
        print("not present")  