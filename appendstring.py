# GIVEN TWO STRING WORD1 AND WORD 2
#TO FIND MERGE THE STRING IN ALTERNATING ODER AND  APPEND ADDITIONAL LETTER TO MERGED STRING 

def mergedAternately(word1,word2):
    merged = ""
   
    i=0
    j=0
    while i<len(word1) and j<len(word2):
        merged += word1[i]+word2[j]
        i+=1
        j+=1

    
    if i<len(word1):
        print(i)
        merged += word1[i:]
        i += 1
        print(i)
        print(merged)
        #print(i)
    if j<len(word2):
        merged += word2[j:]
        j +=1
        
    return merged

    
    #print(merged)

mergedAternately("haihai","he")
