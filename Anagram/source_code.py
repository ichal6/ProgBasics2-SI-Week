import sys
plik = open("anagrams.csv", "r") 

anagram_list = []

for line in plik:
    anagram_list.append(line)
    
lenght = len(anagram_list)    
j=0

while j < lenght:
    i=0
    while i < lenght:
        if(sorted(anagram_list[j])==sorted(anagram_list[i]) and (anagram_list[j]!= anagram_list[i])):
            print(anagram_list[j],end="")
            
            print(anagram_list[i])
            i+=1
        else:
            
            i+=1
    j+=1

plik.close()