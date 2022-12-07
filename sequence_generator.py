pos_int = input("Please specify a positive integer to generate the sequence: ")

z = int(pos_int)

print(z)

while z > 1:
    if z % 2 == 0:
        n = z / 2
        print(int(n))
        z = n
    else:
        n = 3*z + 1
        print(int(n))
        z = n
