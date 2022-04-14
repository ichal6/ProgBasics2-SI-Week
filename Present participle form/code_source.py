import sys

len_verbs = len(sys.argv) - 1



vowels = ['o', 'i', 'y', 'e', 'a','u']
def is_vowel(char):
    return char in vowels 
def is_consonant(char):
    return char not in vowels


verb =  "do"


while len_verbs > 0:
    verb = sys.argv[len_verbs]
    end_verb = len(verb) - 1
    if ("see" == verb or "be" == verb or "flee" == verb or "knee" == verb or "queue" == verb):
        list_temp = list(verb)
        list_temp.append("ing")
        verb = "".join(list_temp)
    elif (verb[end_verb] == 'e' and verb[end_verb-1] != 'i' ):
        list_temp = list(verb)
        del(list_temp[end_verb])
        list_temp.append("ing")
        verb = "".join(list_temp)
    elif (verb[end_verb] == 'e' and verb[end_verb-1] == 'i'):
        list_temp = list(verb)
        del(list_temp[end_verb])
        del(list_temp[end_verb-1])
        list_temp.append("y")
        list_temp.append("ing")
        verb = "".join(list_temp)
    elif (is_consonant(verb[end_verb]) and is_vowel(verb[end_verb-1]) and is_consonant(verb[end_verb-2])):
        list_temp = list(verb)
        list_temp.append(verb[end_verb])
        list_temp.append("ing")
        verb = "".join(list_temp)
    else:
        list_temp = list(verb)
        list_temp.append("ing")
        verb = "".join(list_temp)
    print(verb)
    len_verbs -=1
