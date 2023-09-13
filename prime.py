# 1. look at each number from 2 to 25
# identify if that number is prime (has no divisors) or not
#     2. look at each possible_divisor from 2 up to the number - 1
#.       3. if the possible_divisor divides in evenly then
#.       3a.  "it's not prime"
#.       3b. STOP CHECKING, no need to check rest of possible_divisors
#.    if we tried ALL of the possible divisors and none divide in
#.          then it's prime

for number in range(2, 26): # 1
    is_prime = True # start out by assuming the number is prime
    for possible_divisor in range(2, number): # 2
        if number % possible_divisor == 0: # this IS a divisor (ergo, NOT PRIME) (3)
            print(number, 'equals', possible_divisor, '*', number // possible_divisor) # 3a
            is_prime = False # we KNOW it's not prime
            break # 3b
    # if we get to the end of this for loop and did not break, then it's PRIME
    if is_prime: # == True
        print(number, 'is prime')
