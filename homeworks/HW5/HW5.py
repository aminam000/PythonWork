# Amina Muumin, muumi002, 008, Problem 1


#==========================================
# Name: (cnt_occur)
# Purpose: (takes in a list and returns the number of times an integer is on the list)
# Precondition: (The list can contain numerous data types (e.g. int, float, String, etc) Only int data types are counted.)
# Input Parameter(s): (iny)
# Return Value(s): ( The amount of occurences of a int)
#============================================

def cnt_occur(mylist):
    if mylist == []:
        return 0 
    elif type(mylist) == int:
        return 0
    elif int:
        return cnt_occur(mylist[0]) + helper(mylist[1:])
   

def helper(mylist):
    length = len(mylist)
    counter = 0
    if type(mylist) == int:
        counter +=1
    return counter
    
    
    
# Amina Muumin, muumi002, 008, Problem 2
#============================================
# Name: not_position
# Purpose: takes in a list and an element and returns all the elements in the list
# Precondition: cannot loop and paramters must return 0 if list is empty or 
# Input Parameter(s): 
# Return Value(s):
#============================================
    
def not_position(mylist, element):
        return helper(mylist,element,0)
    
def helper(mylist, element, count, notinlist ):
    if mylist == []:
        return []
    elif element in mylist:
        return [count] + helper(mylist[1:],element,count+1)
    else:
        return helper(mylist[1:],element,count+1,notinlist)


    
# Amina Muumin, muumi002, 008, Problem 3

#============================================
# Name: seq_of_mult_3
# Purpose:models the recursive function thatgenerates the sequence = {2, 6, 18, 54, 162 ...}.
# Precondition: no looping, sequence starts @ 2,  
# Input Parameter(s): seq, index
# Return Value(s): number @ the given index
#============================================

def seq_of_mult_3(seq,index):
    if len(seq) < 2:
        return 0
    elif len(seq) >= 2:
        return seq_of_mult_3(seq(mylist[2:] + [index[seq]*3]
    



# Amina Muumin, muumi002, 008, Problem 4

#============================================
# Name: 
# Purpose:
# Precondition: 
# Input Parameter(s): 
# Return Value(s):
#============================================
def create_range():


 

