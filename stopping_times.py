from sequence_generator import sequence_generator

def stopping_time(z: int):
    s=sequence_generator(z)
    return len(s)-1

