
class Employee:
    salary_by_designation = {
        'Programmer': 25000,
        'Tester': 20000,
        'Manager': 30000
    }

    def __init__(self, name, age, designation):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = Employee.salary_by_designation[designation]

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Designation: {self.designation}, Salary: {self.salary}"

    def raise_salary(self, percent):
        if percent > 30:
            raise ValueError("Raise percentage cannot exceed 30%.")
        self.salary += int((self.salary * percent) / 100)


employees = {}

def save_employees_to_file():
    with open("employee.txt", "w") as f:
        for emp in employees.values():
            f.write(f"{emp.name},{emp.age},{emp.designation},{emp.salary}\n")


def create_employee():
    try:
        name = input("Enter employee name: ")
        if name in employees:
            print("Employee already exists!")
            return
    except Exception as e:
        print(f"Error with name input: {e}")
        return

    try:
        age_input = input("Enter employee age: ")
        if not age_input.isdigit():
            raise ValueError("Age must be a number.")
        age = int(age_input)
    except ValueError as ve:
        print(f"Invalid age input: {ve}")
        return
    except Exception as e:
        print(f"Unexpected error with age: {e}")
        return

    try:
        print("Designations: Programmer, Tester, Manager")
        designation = input("Enter designation: ").capitalize()

        if designation not in Employee.salary_by_designation:
            raise ValueError("Invalid designation.")
    except ValueError as ve:
        print(f"Invalid designation input: {ve}")
        return
    except Exception as e:
        print(f"Unexpected error with designation: {e}")
        return

    employee = Employee(name, age, designation)
    employees[name] = employee
    print("Employee added successfully.")
    save_employees_to_file()


def display_employees():
    if not employees:
        print("No employees to display.")
    else:
        print("\nEmployee List:")
        for emp in employees.values():
            print(emp)


def raise_salary():
    name = input("Enter the name of the employee whose salary you want to raise: ")
    if name not in employees:
        print("Employee not found.")
        return

    try:
        percent_input = input("Enter raise percentage (max 30%): ")
        if not percent_input.replace('.', '', 1).isdigit():
            raise ValueError("Percentage must be a positive number.")

        percent = float(percent_input)
        if percent <= 0 or percent > 30:
            raise ValueError("Percentage must be between 0 and 30.")

        employees[name].raise_salary(percent)
        print(f"Salary raised by {percent}%. New salary: {employees[name].salary}")
        save_employees_to_file()
    except ValueError as ve:
        print(f"Invalid input for salary raise: {ve}")
    except Exception as e:
        print(f"Unexpected error while raising salary: {e}")


def main():
    while True:
        print("\nMenu:")
        print("1. Create Employee")
        print("2. Display Employees")
        print("3. Raise Salary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            create_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            raise_salary()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")

        cont = input("Do you want to continue? (Y/N): ")
        if cont.lower() != 'y':
            print("Thank you for using Employee Management System.")
            break

main()
