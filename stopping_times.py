pos_int = input("Please specify a positive integer to generate the sequence: ")

z = int(pos_int)

sequence = []
sequence.append(z)

while z > 1:
    if z % 2 == 0:
        n = z / 2
        sequence.append(int(n))
        z = n
    else:
        n = 3*z + 1
        sequence.append(int(n))
        z = n

print("The sequence is ", sequence)
print("The stopping time is ", len(sequence))
