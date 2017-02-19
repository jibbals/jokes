from numpy import random

shortlist=[ "Police station toilet stolen, cops have nothing to go on", \
            "I discovered cloning, I am beside myself.", \
            "I broke 3 of my fingers. On the other hand everything is fine.", ]

def shortjoke():
    i=random.randint(0,len(shortlist))
    return (shortlist[i])

longlist=["African man storms up to missionary in remote village " \
    + "'My wife gave birth to a white baby! You're the only white man in this village.'" \
    + "The missionary looks around guiltily and then dissembles: 'Look at those goats, all are white except for one that is black, perhaps the lord works in mysterious ways?'" \
    + "Mr Africa's eyes widen: 'OK clever man, I won't tell people about the white baby, if you don't tell people about the black goat.'", ]

def longjoke():
    i=random.randint(0,len(longlist))
    return (longlist[i])

def joke():
    return [longjoke(),shortjoke()][random.randint(0,2)]

