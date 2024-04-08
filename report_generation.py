"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""

def generate_reports():
    print("List of all employees:")
    for employee in employees_data:
        print("ID:", employee['id'])
        print("Name:", employee['full_name'])
        print("Department:", employee['department'])
        print("Salary:", employee['salary'])
        print("----------------------")
