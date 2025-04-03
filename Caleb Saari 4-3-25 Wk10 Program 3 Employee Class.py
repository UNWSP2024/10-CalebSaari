# The task requires the creation of a Python class named Employee that encapsulates the attributes
# of an employee, specifically: name, ID number, department, and job title. Subsequently, a
# program will instantiate three Employee objects with predefined data and display their
# information.

class Employee:
    def __init__(self, name, id_number, department, job_title):
        self.name = name
        self.id_number = id_number
        self.department = department
        self.job_title = job_title

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID Number: {self.id_number}")
        print(f"Department: {self.department}")
        print(f"Job Title: {self.job_title}")
        print()  # For better readability

# Creating Employee objects
employee1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
employee2 = Employee("Mark Jones", 39119, "IT", "Programmer")
employee3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

# Displaying employee information
employee1.display_info()
employee2.display_info()
employee3.display_info()

# Caleb Saari 4/3/25 Wk10 Program 3: Employee Class