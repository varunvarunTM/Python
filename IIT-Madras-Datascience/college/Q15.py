"""
Q15) Write a Program to create a two list and perform the following 
     operation's :
1) Add the Elements of the two list.
2) Compare the contents of the two list.
3) to find the number of the elements in the list.
4) Sort the elements of the list
5) Reverse the contents of the List. 

"""

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
print("Addition of two list: ", list1 + list2)
print("Comparing two list: ", list1 == list2)
print("Number of elements in list1: ", len(list1))
print("Number of elements in list2: ", len(list2))
print("Sorting list1: ", sorted(list1))
print("Sorting list2: ", sorted(list2))
print("Reversing list1: ", list1[::-1])
print("Reversing list2: ", list2[::-1])