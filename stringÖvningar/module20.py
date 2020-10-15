#Bring out all numbers that are between 3 and 9 (NOT INCLUSIVE) from this list and sort the numbers in order of size with the
# largest number first.

#The result must NOT contain duplicates.

#Of course, also write a loop that prints all numbers in the sorted result list


tal = [ 9, 3, 7, 2, 1, 3, 4, 4, 2, 5, 75, 4, 2, 67 ]
newlist=[]
for x in tal:
   if x not in newlist and 3<x<9:
       newlist.append(x)
newlist.sort()
newlist.reverse()
for i in newlist:
    print(i)
