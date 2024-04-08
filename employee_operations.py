def add_employee(employees_data):
    employee_id = input("Enter employee ID: ")
    full_name = input("Enter employee full name: ")
    department = input("Enter employee department: ")
    salary = input("Enter employee salary: ")
    
    new_employee = {'id': employee_id, 'full_name': full_name, 'department': department, 'salary': salary}
    employees_data.append(new_employee)
    print("Employee added successfully.")

def delete_employee(employees_data):
    employee_id = input("Enter ID of employee to delete: ")
    for employee in employees_data:
        if employee['id'] == employee_id:
            employees_data.remove(employee)
            print("Employee deleted successfully.")
            return
    print("Employee not found.")

def update_employee(employees_data):

    employee_id = input("Enter ID of employee to update: ")
    for employee in employees_data:
        if employee['id'] == employee_id:
            print("Enter new employee details:")
            employee['full_name'] = input("Enter new full name: ")
            employee['department'] = input("Enter new department: ")
            employee['salary'] = input("Enter new salary: ")
            print("Employee updated successfully.")
            return
    print("Employee not found.")