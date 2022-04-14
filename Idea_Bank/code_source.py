new_idea = input("What is your new idea: ")
plik = open("ideabank.txt", "a")
plik.write("\n" + new_idea)
#plik.write("\n")

print("Your idea:")
plik.close()
plik = open("ideabank.txt", "r") 

number = 1

for line in plik:
    print(number, end="")
    print (". " + line, end="")
    number +=1

print()