from math import sqrt
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
gs = gridspec.GridSpec(1,1)


def primeCheck(n):                       # I define a new functin "primeCheck" that takes a number n
    for i in range(2, int(sqrt(n)+1)):   # I create a variable i, which is every integer from 2 to *result of sqrt(n)+1*
        if n % i == 0:                   # This tests if the remainder is 0, if it is, then its not prime
            return False;                
    return n > 1;                        # This safety net quits the function if a given 'n' is less than 1




def primesInRange(a,b):
    allPrimes = []                           # allPrimes becomes a blank list each time the function is called
    Ones = []                                # I create 5 lists to store and then plot each terminal digit
    Threes = []
    Sevens = []
    Nines = []
    for n in range(a,b):                     # This loop is where you input the range in which you want to find primes
        if primeCheck(n):                    # If the number 'n' is True (a.k.a. it is a prime number), do the following
            allPrimes.append(n)              # Append the prime number to the list of all primes
            if n % 10 ==1:                   # Calculate the terminal digit, and append to the appropriate list
                    Ones.append(n)
            if n % 10 == 3:
                    Threes.append(n)
            if n % 10 == 7:
                    Sevens.append(n)
            if n % 10 == 9:
                    Nines.append(n)         # add each prime to its respective list, depending on what number it ends in
    ones = [1] * len(Ones)                  # I create a list of 1's to plot my prime numbers against to see a more clear pattern
    threes = [3] * len(Threes)
    sevens = [7] * len(Sevens)
    nines = [9] * len(Nines)
    
    print(len(allPrimes))
    
    plt.figure(figsize=(2,5))
    
    ax1 = plt.subplot(gs[0,0])
    ax1.title.set_text('1-1000')

    ax1.plot(ones,Ones,'rs',markersize = 1)        # I adjusted the marker size to 5 to clearly see density differences
    ax1.plot(threes,Threes,'cs',markersize = 1)    # I also attempted to make the plot thin, to try and see a closer relationship
    ax1.plot(sevens,Sevens,'gs', markersize = 1)   # between each proceeding prime number
    ax1.plot(nines,Nines,'ms', markersize = 1)

    plt.show()
    #print(allPrimes)
    #print(Ones)

primesInRange(1,1000)
primesInRange(1001,2000)
primesInRange(2001,3000)

import matplotlib.pyplot as plt    # import plot from the python library
x = []                             # I create an empty list 'x'
for z in range (len(allPrimes)):           # I generate numbers from 0 to the length of y, (a.k.a. the number of primes within the range)
    x.append(z)                    # I add the generated the numbers to the empty list, now I have two lists of equal length to
plt.figure(figsize=(10,10))
plt.plot(x,allPrimes,'rs',markersize = 5)  # I plot each prime in order from 1 -> (however many primes there are) and
plt.plot(allPrimes,allPrimes,'co',markersize = 5)  # I plot each prime vs itself to create a line of primes
plt.show()
