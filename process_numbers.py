import statistics

def process_numbers(numbers):
    """
    Processes a list of numbers and calculates the sum, average, and median.
    """
    total_sum = sum(numbers)
    average = statistics.mean(numbers)
    median = statistics.median(numbers)
    
    return total_sum, average, median

if __name__ == "__main__":
    # Example usage
    numbers = [10, 20, 30, 40, 50]
    total_sum, average, median = process_numbers(numbers)
    
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Median: {median}")