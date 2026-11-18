
# Employee Salary Management System

# Function 1: Add Employee
def add_employee(name, emp_id, salary):

    with open("employees.txt", "a") as file:
        file.write(f"{name} | {emp_id} | {salary}\n")

    return "Employee Added Successfully"


# Function 2: View Employees
def view_employees():

    try:
        with open("employees.txt", "r") as file:
            data = file.read()

        if data:
            print("\n----- Employee Records -----")
            print(data)

        else:
            print("No Employee Records Found")

    except FileNotFoundError:
        print("No Employee Records Found")


# Main Program
while True:

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Choose Option:")

    if choice == "1":

        name = input("Enter Name:")
        emp_id = input("Enter ID:")
        salary = input("Enter Salary:")

        message = add_employee(name, emp_id, salary)

        print(message)

    elif choice == "2":

        view_employees()

    elif choice == "3":

        print("Program Closed")
        break

    else:

        print("Invalid Option! Please Try Again")
