import random


def r():
    return str(random.randrange(1,6))

def Dice_in_Rice(roll):
    iter=0
    string = ""
    if(roll == 1):
        return r()
    while iter < roll:
        string =  string + r()
        iter+=1
        if(iter < roll ):
            string = string + "-" 
        

    return string

def Win_Loser(attack,defend):
    lenght_d = len(defend) - 1
    lenght_a = len(attack) - 1
    result = [0,0]
    help_a = []
    help_d = []
    i=0

    while lenght_a >= i:
        help_a.append(attack[i])
        i+=2
        
    i=0
    while lenght_d >= i:
        help_d.append(defend[i])
        i+=2
    
    help_a = sorted(help_a, reverse = True)
    #print(len(help_a))
    help_d = sorted(help_d, reverse = True)
    #print(help_d)
    i=len(help_a) -1
    j=0
    if (i==0):
        if(help_a[0] > help_d[j]):
            help_a.pop(0)
            help_d.pop(j)
            result[1]+=1
        else:
            j+=1
            result[0]+=1

    j=0
    while i != 0:
        if(help_a[0] > help_d[j]):
            help_a.pop(0)
            help_d.pop(j)
            result[1]+=1
        else:
            j+=1
            result[0]+=1
        i-=1
    return result

v_attack = -1
while (v_attack > 3) or (v_attack <= 0):
    v_attack = input('How many units attack: ')
    if(v_attack.isdigit()):
        v_attack = int(v_attack)
    else:
        v_attack = -1
    

v_defend = -1
while (v_defend > 2) or (v_defend <= 0):
    v_defend = input('How many units defend: ')
    if(v_defend.isdigit()):
        v_defend = int(v_defend)
    else:
        v_defend = -1


attack = Dice_in_Rice(v_attack)
defend = Dice_in_Rice(v_defend)

result = Win_Loser(attack,defend)




print("Dice:")
print("\tAttacker: " + attack)
print("\tDefender: " + defend)

print("Outcome:")
print("\tAttacker: Lost " + str(result[0]) + " unit")
print("\tDefender: Lost " + str(result[1]) + " unit")

