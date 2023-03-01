import random
import threading
import time
import statistics
import numpy as np

# create random array
def random_array(maxN, start, end):
    return np.random.randint(start, end, maxN)

# thread_function
def thread_function(numArray, N):
    return sum(numArray[:N])

# Main function
def main():
    maxN = 1000
    numArray = random_array(maxN, 1, 10000)
    time_samples = []

    for j in range(1000):
        start_time = time.time()
        N = random.randint(1, maxN)
        thread_handle = threading.Thread(target=thread_function, args=(numArray, N))
        thread_handle.start()
        thread_handle.join()
        end_time = time.time()
        time_samples.append(end_time - start_time)

    print("Minimum: ", min(time_samples))
    print("Maximum: ", max(time_samples))
    print("Average: ", sum(time_samples)/len(time_samples))
    print("Standard Deviation: ", statistics.stdev(time_samples))

main()