from sequence_generator import sequence_generator as sg
from stopping_times import stopping_time as st

print("Welcome to the Collatz Conjecture Counterexample Finder!")
while True:
    test_value = input("Please specify a number to test, or type exit to quit: ")
    if test_value == str("exit"):
       print("Have a nice day!")
       break
    t = int(test_value)
    print("\nFor the test value", t, "the stopping time is", st(t), "and the sequence is:")
    print(sg(t))
    print("\nUnfortunately, this number is not a counterexample to the Collatz Conjecture. Try again!\n")
