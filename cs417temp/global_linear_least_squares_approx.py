"""
This is the start of the global Linear Least Squares Approximation module.
Take one of the Discrete Least Squares Approximation methods below and incorporate
it into the codebase. Only implement one of the approximation methods.

Discrete Least Squares Approximation methods:
1. XTX|XTY method

2. A|b⃗  method

3. Pre-solved version of the A|b⃗  method
"""
import numpy as np

def read_file(path):
    """
    The read_file function reads each input file,
    and splits the text into 4 columns and appends them as floats
    to the cores list variable.

    Args:
        path: variable for the path to the input file

    Yields:
        This function returns all four cores for each file in a list.
    """
    cores = [[], [], [], []]
    with open(path) as file:
        for line in file:
            cols = line.split()
            for i in range(4):
                cores[i].append(float(cols[i]))
    return cores

def build_times(cores):
    """
    The build_times function takes in the
    row length of each core and returns the times for
    each core.

    Args:
        cores: a list of CPU cores in each .txt file

    Yields:
        This function returns the times incremented by 30 seconds
        for the row length of each core.
    """
    row_count = len(cores[0])
    return [i * 30 for i in range(row_count)]


file1cores = read_file("cs417temp/Input_Text_Files/sensors-2018.12.26-no-labels.txt")
file2cores = read_file("cs417temp/Input_Text_Files/sensors-2019.01.26-no-labels.txt")
file3cores = read_file("cs417temp/Input_Text_Files/sensors-2019.02.09-no-labels.txt")

file1times = build_times(file1cores)
file2times = build_times(file2cores)
file3times = build_times(file3cores)


# Least Squares Computations function
def least_squares_approx(times, temperatures):
    """
    The least_squares_approx function
    computes the value of least-squares for all the
    cores in the three .txt files.

    Args:
        times: represents the times for each core incremented by 30 seconds.

        temperatures: represented the CPU temperatures that were originally listed
            in the .txt files.

    Yields:
        This function returns c0_total and c1_total, which represent
        the y-intercept and the slope, respectively.
    """
    times = np.array(times)
    temperatures = np.array(temperatures)

    k = len(times)
    times_sum = sum(times)
    temperatures_sum = sum(temperatures)

    squared_times_sum_1 = np.sum(times**2)
    multiply_arrays = times * temperatures
    summed_multiplied_arrays = sum(multiply_arrays)
    squared_times_sum_2 = np.sum(times)**2

    # CALCULATE C1 (FIRST)
    c1_numerator = ((k * summed_multiplied_arrays) - (times_sum * temperatures_sum))
    c1_denominator = ((k * squared_times_sum_1) - (squared_times_sum_2))
    c1_total = c1_numerator / c1_denominator

    # CALCULATE C0
    c0_numerator = ((temperatures_sum) - (c1_total * times_sum))
    c0_total = c0_numerator / k
    
    return c0_total, c1_total


# array that hold all files together
all_files = [
    ("sensors-2018.12.26-no-labels.txt", file1cores, file1times),
    ("sensors-2019.01.26-no-labels.txt", file2cores, file2times),
    ("sensors-2019.02.09-no-labels.txt", file3cores, file3times),
]

# loop through all 3 files (12 cores total)
# and apply the least_squares function to all of them
for basename, cores, times in all_files:
    for core_index in range(4):
        temps = cores[core_index]
        c0, c1 = least_squares_approx(times, temps)