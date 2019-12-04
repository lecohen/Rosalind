#need code to reverse number - only works as string
#flip function starts at last character of string and adds it to flip, then moves backwards
#int(flip) returns string as integer

#test function tests if the reverse of 4 times the original number = the original number
#while loop uses test function - if test function returns False, loop moves to check next number
#starts at 1000 since we're looking for a 4 digit number 

def flip(number):
    string = str(number)
    flip = ''

    n = len(string) - 1 #index position
    while n >= 0:
        flip += string[n]
        n -= 1
    return int(flip)

def test(number):
    if flip(4*number)==number:
        return True
    else:
        return False

number = 1000
while test(number) == False:
    number += 1
print(number) 
