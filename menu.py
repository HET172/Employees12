# Menu Module
from .employee_operations import add_employee, delete_employee, update_employee
from .report_generation import generate_reports

def main_menu(employees_data):
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Update Employee")
        print("4. Generate Reports")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee(employees_data)
        elif choice == "2":
            delete_employee(employees_data)
        elif choice == "3":
            update_employee(employees_data)
        elif choice == "4":
            generate_reports(employees_data)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
