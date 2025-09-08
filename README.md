# CS 417 Semester Project

## Project Overview
(The following sections' rules were given by Professor Kennedy)

"As a Computer Scientist, I have a number of interests. Many of these interests overlap. While designing this project, I happened to be batch encoding some videos. I decided to write a quick script to grab CPU temperature data every 30 seconds.

Each of the encoding jobs ran for 5 to 10 hours. If you look at the data you see four temperatures for each reading. My CPU is a 4-core (8 thread) Intel i7-6700K. I found myself interested in not only the behavior of the readings, but also in the temperature differences between the 4 CPU cores."
______

### Input Format

Data takes the form of temperatures in a txt file. All data points are whitespace delimited. Each line represents temperature readings from 4 processor cores. Readings are taken every 30 seconds.

In practice… we need to look at each of the four cores independently. This means that each input file is really four (4) sets of temperature data.
______

### Output Format
All output must be written to text files (one file per core). Each line must take the form:

xk<=x<xk+1
; yi=c0+c1x
 ; type

where…

xk
 and xk+1
 are the domain in which yk
 is applicable

yk
 is the kth
 function

type is either least-squares or interpolation

### Project Requirements
Your task is to take the temperature readings and generate for each core:

A piecewise linear interpolation.
A global linear least squares approximation.
(Optional) A cubic spline (or other non-linear) interpolation.

Your program must accept an input filename as the first command line argument. Your program must NOT prompt the user for a filename.

Your solution must be organized into appropriate “modules” (using your selected language’s best practices). Start with four modules:
1. Input (e.g., using the supplied input libraries)
2. Data pre-processing (i.e., structuring the data for analysis)
3. Piecewise Linear Interpolation
4. Least Squares Approximation

### Documentation Requirements
All code must be properly and fully documented using a language appropriate comment style. All functions (including parameters and return types) must be documented.