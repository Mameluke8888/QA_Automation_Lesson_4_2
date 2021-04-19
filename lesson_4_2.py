
def show_employee(name, salary = 50000):
    """prints out name and salary of an employee"""
    print(name, salary)

show_employee(name = 'Matthew McConaughey', salary = 20000) # 2 keyword arguments
show_employee('Matthew McConaughey', 20000) # 2 positional agrument
show_employee('Matthew McConaughey') # 1 positional argument