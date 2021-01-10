def InsertionSort(input): #passes a 1-D array for insertion sort
    for ind in range(1,len(input)):
        val = input[ind] #get value of current key
        prevInd = ind-1 #get position of previous index
        while prevInd>=0 and input[prevInd]>val: #check for conditions: 1) index is in the first pos or higher 2) key in pos is greater than current key
            input[prevInd+1] = input[prevInd] #replace key in next pos with the key in previous pos
            prevInd -= 1 #move index counter down 1
        input[prevInd+1] = val #once index holding smallest key value found in sorted list, replace key in that ind with current key