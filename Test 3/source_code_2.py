def find_min(L):
    k = 0
    i = 1
    r = len(L) - 1
    while i <= r:
        if L[i] < L[k]:
            k = i
        i += 1
    return L[k]

def differentTeams(skills):
    subject = ['p','c', 'm', 'b', 'z']

    list_temp = list(skills)
    print(list_temp)
    j=0
    length_t=len(list_temp)
    k=0
    w = 0
    result = [0,0,0,0,0]
    while k < 5 :
        if(list_temp[w] == subject[j]):
            result[k]+=1
            w+=1
            
            
        else:
            w+=1

        if w == length_t:
            
            w=0
            k+=1
            j+=1

            
    out = find_min(result)   

    #print(out)

    return out
    


print(differentTeams("pcmpcmbbbzz")) #2
print(differentTeams("pcmpp")) #0
print(differentTeams("pcmbz")) #1