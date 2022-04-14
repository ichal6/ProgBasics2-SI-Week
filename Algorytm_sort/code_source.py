
def insertion_sort(table):
    iter=0

    size_table = len(table)

    while iter < size_table:
        j=0
        while j<= size_table-2:
            if table[j] > table[j+1]:
                temp = table[j+1]
                table[j+1] = table[j]
                table[j] = temp
            j=j+1
        iter+=1

    return table
    
table = []
print("Enter a number (or a letter to exit): ")

user_number = input()

while (user_number.isdigit()):
    digit = int(user_number)
    table.append(digit)
    user_number = input()

table = insertion_sort(table)

print(table)