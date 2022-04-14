
a = 94

Roman_digit = ["I","V","X","L","C","D","M"]


def int_to_roman(input):

    if not 0 < input < 4000:
        return ("too large numbers. Please insert for 1 to 3999")
         
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)


user_number = input('Please insert arabic number by convert to Roman number: ')

print(int_to_roman(int(user_number)))