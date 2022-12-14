def sequence_generator(z: int):
    sequence = []
    sequence.append(z)
    while z > 1:
        if z % 2 == 0:
            n = z // 2
            sequence.append(n)
            z = n
        else:
            n = 3*z + 1
            sequence.append(n)
            z = n
    return sequence
