#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.interpolate import interp1d
import math as mat
import os
from sklearn.model_selection import validation_curve
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from scipy import optimize
import pickle

class NN2Va:
    def __init__(self):
        pass

    def matrix_multiply(self, matrix1, matrix2, A, B, C):
        """
        Multiply two matrices and generate Verilog-A style operations.

        Parameters:
        - matrix1: List of lists representing the first matrix.
        - matrix2: List of lists representing the second matrix.
        - A, B, C: Names of matrices in the Verilog-A model.

        Returns:
        - result: The result of the matrix multiplication.
        - operations: List of strings representing Verilog-A operations.
        """
        # Check if matrices can be multiplied
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Number of columns in the 1st matrix must be equal to the number of rows in 2nd matrix")

        # Get dimensions of the matrices
        rows1, cols1 = len(matrix1), len(matrix1[0])
        rows2, cols2 = len(matrix2), len(matrix2[0])

        # Initialize result matrix with zeros
        result = [[0 for _ in range(cols2)] for _ in range(rows1)]

        # Perform matrix multiplication and generate Verilog-A operations
        operations = []
        for i in range(rows1):
            for j in range(cols2):
                operation = f"activation(bias_{C}_{i}_{j} + "
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
                    operation += f"{A}_{i}_{k} * {B}_{k}_{j} + "  # Add terms for multiplication
                # Remove the trailing "+" sign
                operation = operation[:-3]
                operation += f", {C}_{i}_{j})"
                operations.append(operation)

        return result, operations

    def last_equation(self, matrix1, matrix2, A, B, C, physical_param):
        
        #Multiply two matrices and generate Verilog-A equations for the last layer.

        #Parameters:
        #- matrix1: List of lists representing the first matrix.
        #- matrix2: List of lists representing the second matrix.
        #- A, B, C: Names of matrices in the Verilog-A model.

        #Returns:
        #- result: The result of the matrix multiplication.
        #- operations: List of strings representing Verilog-A operations.
        
        # Check if matrices can be multiplied
        if len(matrix1[0]) != len(matrix2):
            raise ValueError("Number of columns in the 1st matrix must be equal to the number of rows in 2nd matrix")

        # Get dimensions of matrices
        rows1, cols1 = len(matrix1), len(matrix1[0])
        rows2, cols2 = len(matrix2), len(matrix2[0])

        # Initialize result matrix with zeros
        result = [[0 for _ in range(cols2)] for _ in range(rows1)]

        # Perform matrix multiplication and generate Verilog-A operations
        operations = []
        for i in range(rows1):
            for j in range(cols2):
                operation = f"{physical_param} <+ (bias_{C}_{i}_{j} + "
                for k in range(cols1):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
                    operation += f"{A}_{i}_{k} * {B}_{k}_{j} + "  # Add terms for multiplication
                # Remove the trailing "+" sign
                operation = operation[:-3]
                operation += f")"
                operations.append(operation)

        return result, operations

    def write_parameters(self, file, matrix, name):
        
        #Write matrix parameters to a file in Verilog-A style.
        
        #Parameters:
        #- file: Opened file object to write to.
        #- matrix: Matrix to write parameters for.
        #- name: Name prefix for the parameters in Verilog-A.
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                file.write(f"real {name}_{row}_{col} = {matrix[row][col]};\n")

    def write_reals(self, file, rows, cols, name):
    
        #Write real variable declarations in Verilog-A style.

        #Parameters:
        #- file: Opened file object to write to.
        #- rows: Number of rows in the matrix.
        #- cols: Number of columns in the matrix.
        #- name: Name prefix for the real variables.
    
        for row in range(rows):
            for col in range(cols):
                file.write(f"real {name}_{row}_{col};\n")


# In[ ]:




