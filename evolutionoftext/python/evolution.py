# -*- coding: cp1252 -*-

"""

    @Name:      Evolution of Text
    @Author:    CodeBarbarian

    @Desc:      A way to solve the classic text evolution challenge

"""

import random
import string
import time

# Search string .. Write whatever you want in this
SearchString = 'passwordsogoodtahtittakestrillionyearstobreakitgoaheadtryme'

SearchLength = len(SearchString)


# Search Space
SearchSpace = string.ascii_letters + string.digits + string.punctuation + ' ’´¤'

# Flag to check if it is completed
Completed = False

# NameSearch
CurrentGeneration = []

# Append the searchstring to Searchlist to prevent indexing errors
for i in range(SearchLength):
   CurrentGeneration.append(random.choice(SearchSpace))

# Need to keep track of the generations somehow
Generation = 0

StartTime = time.time()

# The main generation loop
while Completed != True:
    # Let us assume it will complete someday
    Completed = True

    # Print the current generation
    print 'Generation ' + str(Generation)
    
    for i in range(SearchLength):
        if CurrentGeneration[i] != SearchString[i]:
            # Set the completed flag to false so that the loop will be run again
            Completed = False

            # Randomise the currentgeneration with choice from the SearchSpace
            CurrentGeneration[i] = random.choice(SearchSpace)
            
    # Increment the generation, for as long as the flag "Completed" is not true    
    if Completed == False:
        Generation += 1
    
# Some filler text, yeah I know.
EndTime = time.time()
print 
print '==============================================================================='
print 'Completed! It took  ' + str(round(EndTime - StartTime)) + ' seconds, and ' + str(Generation) + ' generation to'
print 'get to the predefined searchstring. "Current Generation Below"...'
print '==============================================================================='
print
print 'Current Generation:'
print '-------------------'
print 'Output: ' + ''.join(CurrentGeneration)
