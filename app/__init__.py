import sys

from .day1 import calc_total_sum

def main():
    day = int(sys.argv[1])
    input = sys.stdin.read()
    if day == 1:
        print(calc_total_sum(input))
