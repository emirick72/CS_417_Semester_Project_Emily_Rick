# CS 417 Semester Project

## Project Description Page
The link to the Project Description page is [here](https://www.cs.odu.edu/~tkennedy/cs417/latest/Assts/project-cpu-temps/index.html).
______
## Building the Project
Enter this command in the terminal to build the project and get the output files.
```
python -m cs417temp cs417temp/Input_Text_Files/sensors-2018.12.26-no-labels.txt
```
(Note: Replace the ending file ```sensors-2018.12.26-no-labels.txt``` with the corresponding file name to get the respective output files. There should be four output file for each core, so a total of 12 files should appear when all three input files are used in the command.)
______
## Project Overview
(The overview was given by Professor Kennedy)

"As a Computer Scientist, I have a number of interests. Many of these interests overlap. While designing this project, I happened to be batch encoding some videos. I decided to write a quick script to grab CPU temperature data every 30 seconds.

Each of the encoding jobs ran for 5 to 10 hours. If you look at the data you see four temperatures for each reading. My CPU is a 4-core (8 thread) Intel i7-6700K. I found myself interested in not only the behavior of the readings, but also in the temperature differences between the 4 CPU cores."
______

## Input Format

(All input was originally gathered by Professor Kennedy and put into .txt files.)

Input libraries were given by Professor Kennedy.

Input data is given via a txt file and is formatted as temperatures in degrees Celsius.
All data points are whitespace delimited and each line represents temperature readings from 4 CPU cores (8 threads). Readings were taken every 30 seconds.

When reading the input, the user should look at each of the four cores independently. Meaning, each input file is really 4 sets of temperature data.

______

## Output Format

All output must be written to text files (one file per core). Each line must take the form:

$$x_k <= x < x_\{k+1}$$; $$y_i = c_0 + c_1x$$; *type* 


where…

* $$x_k$$ and $$x_\{k+1}$$ are the domain in which $$y_k$$ is applicable

* $$y_k$$ is the $$kth$$ function

* *type* is either *least-squares* or *interpolation*
______

## Project Requirements
Your task is to take the temperature readings and generate for each core:
1. A piecewise linear interpolation.
2. A global linear least squares approximation.
3. (Optional) A cubic spline (or other non-linear) interpolation.

Your program must accept an input filename as the first command line argument. Your program must NOT prompt the user for a filename.

Your solution must be organized into appropriate “modules” (using your selected language’s best practices). Start with four modules:
1. Input (e.g., using the supplied input libraries)
2. Data pre-processing (i.e., structuring the data for analysis)
3. Piecewise Linear Interpolation
4. Least Squares Approximation
______

## Documentation Requirements
All code must be properly and fully documented using a language appropriate comment style. All functions (including parameters and return types) must be documented. 
* Doxygen can be used for C++, Java, or JavaScript.
* Javadoc can be used for Java.
* Pydoc or Sphinx can be used for Python.
______

## Updates
11/24/2025: Implemented the global linear least squares approximation module for this project. Also updated the README file and the main file.