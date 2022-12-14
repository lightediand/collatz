# Collatz Conjecture Counterexample Finder!

This is a fun little program that tests whether or not a given integer is a counterexample to the Collatz conjecture.

The program takes the starting number and generators a sequence based on these rules:
* if the number is even, divide it by 2
* if the number is odd and greater than 1, triple it and add 1
* if the number is 1, stop the sequence!
    
The time it takes for a sequence to reach 1, marked by the number of terms in the sequence before 1, is known as the stopping time.

Simply run collatz.py and it will generate the sequence, tell you the stopping time (if it exists (it probably will)) and whether or not that makes it a counterexample to the Collatz conjecture.

Have fun!
