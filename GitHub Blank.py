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

def FindWordCount(mylist, string):
    with open(mylist, 'r') as myfile:
        newfile = myfile.read()
        occurence = newfile.count(string)
        return occurence

def ScoreFinder(players, scores, child):
    counter = 0
    Bool = False
    for person in players:
        if person.lower() == child.lower():
            Bool = True
            playerscore = scores[counter]
            player = players[counter]
        counter += 1
    if Bool == False:
        print('player not found')
    else:
        print(player, 'got a score of', playerscore)


    
    
