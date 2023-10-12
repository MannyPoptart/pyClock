# Create a simple timer that counts down from 10.
# When it reaches 0, it prints "BLAST OFF!" and then exits.
import time
import sys


def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
        time.sleep(1)
    print("BLAST OFF!")
    sys.exit()

countdown(10)