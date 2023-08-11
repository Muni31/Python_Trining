# Implement basic function for finding factorial of single number. (function must sleep or 0.001second after each iteration) 

# a.Take list of N numbers and find their factorial without using multithreading and show after 	results of all numbers are ready. 

# b.Take list of N numbers and find their factorial using multithreading and show after result of 	all number is ready. 

# c.Analyse time taken, cpu usage, memory usage. 


import time
import math
import threading

# Function to calculate factorial with a sleep of 0.001 seconds after each iteration
def factorial_with_sleep(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
        time.sleep(0.001)  # Sleep for 0.001 seconds after each iteration
    return result

# Function to calculate factorial without multithreading
def without_multithreading(numbers):
    results = []
    for num in numbers:
        results.append(factorial_with_sleep(num))
    return results

#  with multithreading
def with_multithreading(numbers):
    results = []
    threads = []
    for num in numbers:
        thread = threading.Thread(target=lambda: results.append(factorial_with_sleep(num)))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    return results

if __name__ == "__main__":
    numbers = [5, 6, 7, 8, 9]

    #  without multithreading and measure time, CPU, and memory usage
    start_time = time.time()
    without_multithreading = without_multithreading(numbers)
    end_time = time.time()

    print("Factorial without multithreading:")
    for num, result in zip(numbers, without_multithreading):
        print(f"Factorial of {num} is: {result}")

    print("Time taken without multithreading:", end_time - start_time)

    #  with multithreading and measure time, CPU, and memory usage
    start_time = time.time()
    results_with_multithreading = with_multithreading(numbers)
    end_time = time.time()

    print("\nFactorial with multithreading:")
    for num, result in zip(numbers, results_with_multithreading):
        print(f"Factorial of {num} is: {result}")

    print("Time taken with multithreading:", end_time - start_time)
