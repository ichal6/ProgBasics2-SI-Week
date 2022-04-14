import sys

def show_list():
    plik = open("ideabank.txt", "r") 

    number = 1

    print("Your idea:")
    for line in plik:
        print(number, end="")
        print (". " + line, end="")
        number +=1

    print()
    plik.close()

def delete_item(id):
    openfile = open('ideabank.txt','r')
    my_list = openfile.readlines()
    openfile.close()

    
    my_list.pop(id-1)
    
    outfile = open('ideabank.txt','w')
    for line in my_list:
        outfile.write(line)
    outfile.close()



if len(sys.argv) >= 2:
    if sys.argv[1] == "--list":
        show_list()
        sys.exit()
    if sys.argv[1] == "--delete":
        index = int(sys.argv[2])
        delete_item(index)
        show_list()
        sys.exit()

new_idea = input("What is your new idea: ")
plik = open("ideabank.txt", "a")
plik.write("\n" + new_idea)

plik.close()

show_list()


