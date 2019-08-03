# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird

z = [4, 1, 3, 4, 5, 6, 7, 8, 9, 0]

for n in z:

    if n % 2 > 0:
        print('Weird')
    elif n % 2 == 0 and 2 <= n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')
