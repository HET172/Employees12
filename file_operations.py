"""
File Operations Module

This module provides functions for reading from and writing to the text file
that stores employee data.
"""
def read_employees():
    try:
        with open("employees.txt", 'r') as file:
            employees_data = [line.strip() for line in file.readlines()]
        return employees_data
    except FileNotFoundError:
        print("File not found.")
        return []

def write_employees():
   with open("employees.txt", 'w') as file:
        for employee in employees_data:
            file.write(employee + '\n')
