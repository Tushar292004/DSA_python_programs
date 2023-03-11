n = int(input("Enter the number of elements you want : "))
no=[int(input("Enter the element {0} = ".format(i+1))) for i in range(n)]

if(len(no)==0):
  print("Array is empty.")
else: 
  smallest = no[0]
  largest = no[0] 
  for i in no:
    if i<smallest:
        smallest = i
        smallest_index = no.index(i)
    if i>largest:
        largest = i
        largest_index = no.index(i)
  print("Smallest number in array is {0} and index is {1} and largest number is {2} and index is {3}.".format(smallest, smallest_index+1, largest, largest_index+1))
        