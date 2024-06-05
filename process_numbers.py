import statistics
import os

def process_numbers(numbers):
    """
    Processes a list of numbers and calculates the sum, average, and median.
    """
    total_sum = sum(numbers)
    average = statistics.mean(numbers)
    median = statistics.median(numbers)
    
    return total_sum, average, median

def load_input():
    f = open("input.txt", "r")
    lines = ", ".join(f.readlines())
    numbers_str =  lines.split(",")
    numbers_int = [int(x.strip()) for x in numbers_str]
    return numbers_int

if __name__ == "__main__":
    if (not os.path.exists("./input.txt")):
        print("Error Create a input text file in : ./input.txt")
        exit()

    numbers = load_input()

    if (numbers):
        total_sum, average, median = process_numbers(numbers)
    
        print(f"Sum: {total_sum}")
        print(f"Average: {average}")
        print(f"Median: {median}")
    else:
        print("Insert input separated by comma in file: input.txt")