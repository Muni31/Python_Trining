# Implement simple function which takes name as input and returns "hello <name>" after 1 second. 

#     a. Do it for N names using multithreading and multiprocessing. 

import threading
import multiprocessing
import time

# N names using multithreading
def with_thread(name):
    time.sleep(1)
    print(f"Hello {name}")

def with_threads(names):
    threads = []
    for name in names:
        thread = threading.Thread(target=with_thread, args=(name,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()



# N names using multiprocessing

def with_process(name):
    time.sleep(1)
    print(f"Hello {name}")

def with_processes(names):
    processes = []
    for name in names:
        process = multiprocessing.Process(target=with_process, args=(name,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


if __name__ == "__main__":
    names = ["vamsi", "jai", "shivam"]
    print("multithreading is started")
    with_threads(names)
    print("multithreading is Ended")
    print('--------------------')
    print("\nmultiprocessing is Started")
    with_processes(names)
    print("multiprocessing is Ended")
