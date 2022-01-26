import random


def getDigits(num):
    ''' creates list of digits for the integer input'''
    return [int(i) for i in str(num)]


def noDuplicates(num):
    '''Returns True if number has no duplicate digits otherwise False'''
    num_li = getDigits(num)
    if len(num_li) == len(set(num_li)):
        return True
    else:
        return False


def generateNum():
    '''Generates a 4 digit number with no repeated digits'''
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num


def numOfBullsCows(num, guess):
    '''matches(bulls) and the common digits in wrong position (cows)'''
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)

    for i, j in zip(num_li, guess_li):

        # common digit present
        if j in num_li:

            # common digit exact match
            if j == i:
                bull_cow[0] += 1

            # common digit match but in wrong position
            else:
                bull_cow[1] += 1

    return bull_cow


def hints(num):
    '''returns no of even and odd digits'''
    h = [0, 0]
    num_li = getDigits(num)
    for i in num_li:
        if i % 2 == 0:
            h[0] += 1
    h[1] = 4 - h[0]

    return h


def upperrange(num):
    r = (num // 1000) * 10
    t = "first two numbers are in range of " + str(r) + " to " + str(r + 10)
    return t


def lowerrange(num):
    r = ((num // 10) % 10) * 10
    t = "last two numbers are in range of " + str(r) + " to " + str(r + 10)
    return t
