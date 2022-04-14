import sys
def dnaComplement(s):
    e = ['A','T' ,'C', 'G']
    length_s = len(s)
    
    reverse = ""

    
    k = 1
    
    while length_s > k:
        reverse =  reverse + s[length_s - k] 
        k+=1
    reverse =  reverse + s[0] 

    #reverse = s[::-1]
     

    i = 0

    list_temp = list(reverse)
    #print(list_temp)
    while i < len(list_temp):
        if reverse[i] == 'A':
            list_temp[i] = 'T'
        elif reverse[i] == 'T':
            list_temp[i] = 'A'
        elif reverse[i] == 'C':
            list_temp[i] = 'G'
        elif reverse[i] == 'G':
            list_temp[i] = 'C'
        i+=1
    result = "".join(list_temp)
    print(result)

dnaComplement("ATGC")