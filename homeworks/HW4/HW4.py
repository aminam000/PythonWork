#Amina Muumin, muumi002, 008, HW4
#==========================================
# Name: remove_the_fact
# Purpose: Given a list of strings, create a new list that has in
# position 0 the number of times “fact” was in the original list and in
# position 1, a list of all other strings in the original list that were
# not “fact”. There can be duplication of strings on the new list.
# Precondition: The list will only contain strings.
# Input Parameter(s)
# my_list: a list containing only strings or the empty list
# Return Value(s)
# -- if the input parameter is an empty list, return a list
# of [0, []]
# -- else return a list with the 0th index position containing the
# number of times “fact” was seen on the list and the 1st
# index position containing the list of the strings that are
# not “fact”. If there are no strings on the list, return
# an empty list in that position.
#============================================
def remove_the_fact(mylist):
    y = 0
    newlist = []
    for x in mylist:
        if x == "fact":
            y +=1
        else:
            newlist.append(x)
    return ([y, newlist])
#==========================================
# Name: average_of_ints
# Purpose: To find the integers in a list of inputs and find the average
# Precondition: Hint: Answer the question “What must be true prior
# to the call?” Is there a condition that must be true?
# Input Parameter(s): mylist, which is a list of inputs
#
# Return Value(s): The average of the integers as well as the list of integers
#
#============================================
def average_of_ints(mylist):
    y = 0
    newlist = []
    sum_mylist = 0
    for x in mylist:
        if type(x) == int:
            newlist.append(x)
            sum_mylist = sum_mylist + x
            avg = sum_mylist / len(newlist)
            y = avg
    return ([y, newlist])
#==========================================
# Name: max_of_lists
# Purpose: return the maximum number in a lists of lists
# Input Parameter(s): mylist
#
# Return Value(s): the maximum number, which is y
#
#============================================
def max_of_lists(mylist):
    maximum = mylist[0][0]
    for x in mylist:
        for y in x:
            if y > maximum:
                maximum = y
    return maximum
#==========================================
# Name: greater_than
# Purpose: To determine if the greatest integer in the first list is greater than or less than the integer in the second list.
# Input Parameter(s): mylist, x
#
# Return Value(s): True or False
#
#============================================
def greater_than(mylist, x):
    newlist= []
    max_num = 0
    for y in mylist:
        if type(y) == int:
            newlist.append(y)
        for w in newlist:
            if w > max_num:
                max_num = w
    if w > x:
        return True
    else:
        return False
#==========================================
# Name: selection sort
# Purpose:
# 
# Input Parameter(s)
#
# Return Value(s)
#
#============================================
