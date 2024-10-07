# NN2Va
<<<<<<< HEAD
# NN2Va
=======
This script allows you to translate a neural network from python to verilog-a. It has been exclusively designed to use a neural network model of unconventional electronics for circuit simulations. It has already been tested for neural networks that include 420 neurons in total with success, but larger neural networks faield because the software we tested on does not support it.<br>

# Introduction:
Make sure you are in the correct directory where the *py2va.py* file is located. In this repo the file location is in the *src* (source) folder. Here you create your new script and import the library:<br>
**from py2va import NN2Va**<br>

This will import the class that you can use to write your neural network in Verilog-a.<br>

# Content:<br>
The class currently includes four functions:<br>
## matrix\_multiply:<br>
**matrix_multiply(matrix1, matrix2, A, B, C)**<br>
*Let's say you want to multiply matrix1 and matrix2, the result is matrix 3*<br>
This function will return the result and the Verilog-a lines of code that describes the matrix multiplication.<br>
Normally this will be where the weight matrices are added.<br>
The string arguments are just the names of the matrices that will be written in Verilog-a.<br>
**matrix1**: The first matrix.<br>
**matrix2**: The second matrix.<br>
**A**: *String*: The name of the first matrix that will be written in the Verilog-a file.<br>
**B**: *Sting*: The name of the second matrix that will be written in the Verilog-a file. <br>
**C**: *String*: The name of the output matrix that will be written in the Verilog-a file.<br>
(*The output matrix is the resulting matrix you get by multiplying matrix1 and matrix2*)<br>

## write\_parameters:<br>
**write_parameters(file, matrix, name):**<br>
**file**: The file you want the parameters to be written in. Typically this will be the verilog-a file.<br>
**matrix**: The matrix from which wou want to define the parameters.<br>
**name**: The name of the matrix in the Verilog-a code.<br>
*This fuction will define parameters as "real" in Verilog-a, and will be used for the known parameters.*<br>
This function will output in Verilog-a code parameters of the weight and bias matricies.<br>

## wite\_reals:<br>
**write_reals(file, rows, cols, "name")**:<br>
**file**: The file you want the parameters to be written in. Typically this will be the verilog-a file.<br>
**rows**: The number of rows in the output matrix. If you want to multiply matrix1 and matrix2 resulting in matrix3, this is where you give the numbers of rows for matrix3.<br>
**cols**: The numbers of columns in the output matrix.<br>
**name**: *String*: The name of the output matrix<br>
*This funcution will also output parameters as "real" in Verilog-a, but this time this is used to define your output matrices, the ones you get by multiplying the known matricie"s*<br>

## Last\_equation:<br>
**last_equation(matrix1, matrix2, A, B, C, physical_param):**<br>
**matrix1**: The first matrix<br>
**matrix2**: The second matrix<br>
**A**: (*String*) Name of the first matrix in Verilog-a<br>
**B**: (*String*) Name of the second matrix in Verilog-a<br>
**C**: (*String*) Name of the output matrix in Verilog-a<br>
**physical_param**:(*String*) Name of the output physical parameter.<br>
This function will output the last equation for the neural network. Normally this will be with a physical parameter, so while naming it make sure to include the branches.<br>
*Example: If you are computing the drain current of a transistor, then the physical_param should be written as I(d, s) where d and s are the branches (drain and source) in the Verilog-a code*<br>

# Example:<br>

