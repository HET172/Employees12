"""
Employee Management System Module

This module provides various functionalities for managing employee data, 
including adding, deleting, updating, and generating reports.
"""
import src.menu as menu

def main():
    employees_data = read_employees()
    main_menu(employees_data)  
    write_employees(employees_data)
    menu.main_menu()

if __name__ == "__main__":
    main()
