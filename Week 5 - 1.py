def Extract(seq):
    #Pointer one tracks the start of the longest sequence (p1)
    #Pointer two hops up the list comparing n to n-1      (p2)

    counted = 1
    # ^ Total counted
    record = 1
    # ^ Longest length counted
    recordcount = 1
    # ^ Running record tracker

    p1 = 0
    p2 = 1
    
    while counted < len(seq):
        if seq[p2] > seq[p2-1]:
            p2 = p2 + 1
            counted = counted + 1
            recordcount = recordcount + 1
            # ^ Incrementing p2 until a new sub-seq is found
            
        else:
            if recordcount > record:
                #print("New record found:",recordcount)
                record = recordcount
                p1 = p2-record
                # ^ Sets p1 to the start of the longest recorded seq
                #print("Record start point:",p1)
                
            #print("\nStart of new sequence:")
            recordcount = 1
            counted = counted + 1
            p2 = counted
    if record == 1:
        return "No valid sequence found"
    print("\nCounted:",counted)
    print("Longest sub-sequence start:",p1,"\n"
          "Length of sub-sequence:",record,"\n"
          "Sub-sequence:",seq[p1:p1+record])

            
