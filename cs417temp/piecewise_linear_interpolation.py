"""
This is the start of the piecewise linear interpolation module.
Take the interpolation formulas from the "Least Squares Approximation Introduction"
and apply them here to the current notation.
This module is supposed to take two different pairs of points and then compute
a straight line equation from the two point pairs.
"""

def piecewise_linear_interpolation(x_values, y_values):
    """
    Define a piecewise linear interpolation function and return a list of each plot point

    Args:
        x_values: the x-intercept in the plot point or the time measured in seconds

        y_values: the y-intercept in the plot point or a tuple list of all four CPU temperatures

    Yields:
        Returns/yields an array of the plot points to be graphed.
    """

    # Return list of (x_start, x_ending, b, m) for each pair of points/line segment
    list_results = []

    for k in range(len(x_values) - 1):
        # set the starting and ending "x" and "y" values
        x_start = x_values[k]
        x_end = x_values[k + 1]
        y_start = y_values[k]
        y_end = y_values[k + 1]

        # declare "m" and "b" variables for their respective formulas
        m = (y_end - y_start) / (x_end - x_start)
        b = y_start - m * x_start

        # append list of results to the array
        list_results.append((x_start, x_end, b, m))
    # return the list of results in the array
    return list_results
