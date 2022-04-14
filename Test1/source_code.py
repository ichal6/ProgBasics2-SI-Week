
def alphabet_filter(word):
    the_vowel = ["a","e","i","o","u"]
    lenght_v = len(the_vowel)
    lenght_w = len(word) 
    
    word_consonants = ""
    word_vowels = ""
    j = 0
    
    while j < lenght_w:
        i=0
        while i < lenght_v :
            if word[j] == the_vowel[i]:
                word_vowels += word[j]
                i = lenght_v
            i+=1
        j+=1
    j = 0
    
    while j < lenght_w:
        i=0
        con = 1
        while i < lenght_v :
            if word[j] == the_vowel[i]:
                i = lenght_v
                con = 0
            
            i+=1
        if con == 1:
            word_consonants += word[j]
        j+=1
    print(word_consonants)
    print(word_vowels)        
    
    return word_consonants, word_vowels

alphabet_filter("urszula")
