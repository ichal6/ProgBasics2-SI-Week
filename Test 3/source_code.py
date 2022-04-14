def differentTeams(skills):
    subject = ['p','c', 'm', 'b', 'z']
    length_s = len(subject)
    list_temp = list(skills)
    print(list_temp)
    j=0
    i=len(list_temp)
    k=0
    result = 0
    while i != 0:
        if(list_temp[0] == subject[j]):
            list_temp.pop(0)
            result+=1
            k+=1
        else:
            j+=1
            

        if j == length_s:
            list_temp.pop(0)
            j=k
        i=len(list_temp)

    print(result)

    wynik = int(result/5)

    #print(wynik)

    return wynik
    

print(differentTeams("pcmpcmbbbzz")) #2
print(differentTeams("pcmpp")) #0
print(differentTeams("pcmbz")) #1