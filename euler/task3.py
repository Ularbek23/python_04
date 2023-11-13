def result(num):
    # spis = [] #1
    # for i in range(2, num):
    #     a = True
    #     ost = num % i
    #     if ost == 0:
    #         for k in range(2, i):
    #             res = i % k
    #             if res == 0:
    #                 a = False
    #         if a == True:
    #             otv = i
                # spis.append(i) #1
    
    # return otv

    # divisor = 2
    # largest_prime_divisor = 1
    # while num > 1:
    #     while num % divisor == 0:
    #         largest_prime_divisor = divisor
    #         num /= divisor
    #     divisor += 1

    # return largest_prime_divisor

    if not isinstance(num, int) or num < 1:
        return None

    divisor = 2
    largest_prime_divisor = 1
    while num > 1:
        while num % divisor == 0:
            largest_prime_divisor = divisor
            num /= divisor
        divisor += 1

    return largest_prime_divisor



print(result(13195))




# print(result(600851475143))