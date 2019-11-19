#Aly Ranucci
#CSCI 102 - Section A
#Week 11 - Part B

def PrintOutput(string):
    print('OUTPUT', string)
    
def LoadFile(string):
    with open(string, 'r') as myfile:
        mylist = myfile.readlines()
        return mylist
        
def UpdateString(string1, string2, num):
    return string1[:num] + string2 + string1[num + 1:]

