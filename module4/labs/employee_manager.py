# Angel Chavez
# Aug 2nd, 2025
# Python 3.13.5
# program that manages a list of employee objects.

class Employee:
    """Employee class"""

    # i used type hints in the parameters to be more clear and less confusing,
    # note that Python does not enforce this though, so salary and performance
    # could still be initialized as strings.
    def __init__(self, name, department, salary: float, performance_score: int):
        """Initializes employee attributes"""

        self.name = name
        self.department = department
        self.salary = salary
        self.performance_score = performance_score
    
    def display_info(self):
        """Displays employee info"""

        print('Employee Stats')
        print(f'Name: {self.name.title()}')
        print(f'Department: {self.department.title()}')
        print(f'Annual Salary: ${self.salary:,.2f}')    # makes output more human readable
        print(f'Performance Score: {self.performance_score}\n')
    
    def apply_raise(self, percent):
        """Applies raise to employee as a percent
        """
        bonus = self.salary * percent / 100
        self.salary += bonus

# init empty lists
staff = []
high_performer_staff = []

# init employee objects
employee1 = Employee('angel', 'devops', 180000.00, 9)
employee2 = Employee('alex', 'operations', 89000.00, 8)
employee3 = Employee('joseph', 'operations', 145000.00, 9)
employee4 = Employee('matt', 'devops', 120000.00, 7)
employee5 = Employee('lauren', 'cybersecurity', 135000.00, 6)

# add employees to staff list
staff.append(employee1)
staff.append(employee2)
staff.append(employee3)
staff.append(employee4)
staff.append(employee5)

# display every employees info and adds them to high performer list if -
# their performance score is greater than or equal to 8
for employee in staff:
    employee.display_info()
    if employee.performance_score >= 8:
        high_performer_staff.append(employee)

# displays high performers and gives them a raise
for employee in high_performer_staff:
    print(' High performer! ')
    print(' They get a raise ')
    employee.apply_raise(5)
    employee.display_info()