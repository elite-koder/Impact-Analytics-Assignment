import sys
from solution import Solution
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please provide number of days")
        sys.exit(1)
    elif not sys.argv[1].isdigit() or int(sys.argv[1]) < 4 or int(sys.argv[1]) > 1000:
        print("Please provide valid number of days. It should be in range (4, 1000) inclusive")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Please provide only one argument")
        sys.exit(1)
    n = int(sys.argv[1])
    solution = Solution(n)
    print(f"For {n} days: {solution.get_ways_to_miss_ceremony()}/{solution.get_ways_to_attend_classes()}")