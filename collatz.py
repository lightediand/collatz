from sequence_generator import sequence_generator as sg
from stopping_times import stopping_time as st

test_value = input("Please specify a number to test: ") 

t = int(test_value)

print("For the test value", t, "the stopping time is", st(t), "and the sequence is:\n")
print(sg(t))
print("\nUnfortunately, this number is not a counterexample to the Collatz conjecture. Try again!")
