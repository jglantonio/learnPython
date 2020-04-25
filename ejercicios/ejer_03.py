## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for number in check_prime:
    if (number % 2) == 1:
        print("{} IS a prime number".format(number))
    else:
        print("{} is NOT a prime number, because 2 is a factor of {}" .format(number,2,number))
