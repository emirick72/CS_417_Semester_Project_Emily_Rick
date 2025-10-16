import sys
from pathlib import Path
from cs417temp.parse_temps import parse_raw_temps
from cs417temp.piecewise_linear_interpolation import piecewise_linear_interpolation

with Path(sys.argv[1]).open() as o:
    print(list(parse_raw_temps(o)))

def output_interpolation_file (core_index, x_values, y_values, basename):
    """
    Output a text file using the the piecewise_linear_interpolation function
    (defined in it's respective module)

    Args:
        core_index: counts the number of CPU cores (0 through 3)

        x_values: the x-intercept in the plot point or the time measured in seconds

        y_values: the y-intercept in the plot point or a tuple list of all four CPU temperatures

        basename: variable to hold the input file name without the extension (.dat or .txt extensions)

    Yields:
        Outputs each line for each interpolation in the following format:
        x_k <= x < x_(k+1) ; y_i = c_0 + c_1x ; type
    """
    plot_points = piecewise_linear_interpolation(x_values, y_values)
    # output the .txt file name
    file_output = f"{basename}-core-{core_index}.txt"

    # output each line for each interpolation
    with open(file_output, "w") as f:
        for (x_start, x_end, b, m) in plot_points:
            f.write(f"{x_start:10.0f} <= x <= {x_end:10.0f} ; y = {b:10.4f} + {m:10.4f} x ; interpolation\n")

"""
Main driver function
"""
def main():
    """
    Main driver function that parses each input file,
    transposes each "x" and "y" value, and loops through each CPU core.

    Args:
        No arguments declared.

    Yields:
        A parsed input file and four output files corresponding to the four CPU cores.
    """
    # Parse input file
    path = Path(sys.argv[1])
    basefile_name = path.stem
    with path.open() as f:
        data = list(parse_raw_temps(f))

    # Transpose both x and y values and loop through each core (column)
    x_values = [row[0] for row in data]
    cores = list(zip(*[row[1] for row in data]))

    for i, core_values in enumerate(cores):
        output_interpolation_file(i, x_values, core_values, basefile_name)

"""
Call the main driver function
"""
if __name__ == "__main__":
    main()