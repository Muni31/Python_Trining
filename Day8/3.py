# Implement basic function for finding n'th fibonacci number of series. 
# (function must sleep for 0.001second after each iteration) 

# a.Take list of N numbers and find respective fibonacci number without using multiprocessing 	
# and show after results of all numbers are ready. 

# b.Take list of N numbers and find their respective fibonacci number using multiprocessing 	
# and show after results of all numbers are ready. 

# c.Analyse time taken, cpu usage, memory usage 
import time
import psutil
import multiprocessing

# Function to calculate Fibonacci number with a sleep of 0.001 seconds after each iteration
def with_sleep(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = 1
        prev_fib = 0
        for _ in range(2, n + 1):
            fib, prev_fib = fib + prev_fib, fib
            time.sleep(0.001)  # Sleep for 0.001 seconds after each iteration
        return fib

# Function to calculate Fibonacci number without using multiprocessing
def without_multiprocessing(numbers):
    results = []
    for num in numbers:
        results.append(with_sleep(num))
    return results

# Function to calculate Fibonacci number using multiprocessing
def fibonacci_worker(num, results):
    result = with_sleep(num)
    results.append(result)

if __name__ == "__main__":
    # Take list of N numbers for Fibonacci calculation
    numbers = [30, 31, 32, 33, 34]

    # Calculate Fibonacci numbers without multiprocessing and measure time, CPU, and memory usage
    start_time = time.time()
    results_without_multiprocessing = without_multiprocessing(numbers)
    end_time = time.time()

    print("Fibonacci numbers without multiprocessing:")
    for num, result in zip(numbers, results_without_multiprocessing):
        print(f"Fibonacci number of {num} is: {result}")

    print("Time taken without multiprocessing:", end_time - start_time)
    print("CPU usage without multiprocessing:", psutil.cpu_percent(interval=1))
    print("Memory usage without multiprocessing:", psutil.virtual_memory().percent)

    # Calculate Fibonacci numbers with multiprocessing and measure time, CPU, and memory usage
    start_time = time.time()
    manager = multiprocessing.Manager()
    results_with_multiprocessing = manager.list()
    processes = []

    for num in numbers:
        process = multiprocessing.Process(target=fibonacci_worker, args=(num, results_with_multiprocessing))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results_with_multiprocessing = list(results_with_multiprocessing)

    end_time = time.time()

    print("\nFibonacci numbers with multiprocessing:")
    for num, result in zip(numbers, results_with_multiprocessing):
        print(f"Fibonacci number of {num} is: {result}")

    print("Time taken with multiprocessing:", end_time - start_time)
    print("CPU usage with multiprocessing:", psutil.cpu_percent(interval=1))
    print("Memory usage with multiprocessing:", psutil.virtual_memory().percent)

