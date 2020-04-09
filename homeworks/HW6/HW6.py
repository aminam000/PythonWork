# CSCI 1133 Amina Muumin muumi002 lab008

# Name: sameKeys
# Purpose: if the two dictionaries share the same keys, a new dictionary with these shared keys will be formed
# Precondition: 2 dictionaries
# Input Parameter(s) - diction1 & diction2, both of which contain strings and integers
# Return Value(s) - a catcanated dictionary          
#==========================================
def sameKeys(diction1, diction2):
    new_diction1 = {}
    if diction1 == {}:
        return new_diction1
    elif diction1 != {}:
        for y in diction1:
            if y in diction2:
                new_diction1[y] = [diction1[y],diction2[y]]
        return new_diction1

#==========================================
# Name: averageHours
# Purpose: Creates a new dictionary with keys representing employees and values representing an average of their hours worked per week.
# Precondition: a dictionary with a name and a list number of hours
# Input Parameter(s): diction
# Return Value(s): names with their average hours worked
#============================================
def averageHours(diction):
    new_diction = {}
    newdict = { }
    for i in diction:
        if diction == { }:
            return newdict
        elif diction[i] != [ ]:
            average = int(sum(diction[i])/len(diction[i]))
            newdict[i] = average
        else:
            newdict[i] = 0
    return newdict
    newlist = []
    for i in sorted (new_diction) :
        newlist.append(i)
        newlist.append(new_diction[i])
    return newlist

#============================================
# Name: allKeys
# Purpose: The function creates a sorted list of nonduplicated keys representing the keys from the dictionary where any of the integers on the element list was found 
# Precondition: element needs to be an integer
# Input Parameter(s): diction, element 
# Return Value(s): a list with a dictionary of index values of element
#============================================

def allKeys(diction, element):
    list_of_keys = []
    for t in diction:
        if element in diction[t]:
            list_of_keys.append(t)
            list_of_keys.sort
            
    return list_of_keys
