# Payroll Sytem - Final Assignment

This project is my final assignment for the Programming 2 course at Fanshawe.

Payroll System Description:

The code implements a basic payroll system where user details for different types of employees can be inputted. The main components and functionalities are:

<b>Employee Types:</b> The system can cater to three types of employees:

<b>Full-Time Employees:</b> Identified by name, ID, age, optional car details, salary, and bonus.
Part-Time Employees: Identified by name, ID, age, optional car details, rate of pay, and hours worked.
Interns: Identified by name, ID, age, optional car details, and a stipend.
Car Details: For each employee type, there's an option to input car details, specifically the car's make and model.

<b>Input Loop:</b> The system continuously prompts the user to input employee details until the user chooses to exit by entering '999' as the employee name.

<b>Display:</b> After exiting the input loop (by entering '999'), the system displays a summary of all employees entered, categorized by their types. If an employee has car details, those are displayed as well.

<b>Code Structure: </b>The main logic is encapsulated within the Payroll class, which maintains separate lists for each type of employee. The main_loop method handles user input, while the display_all_employees method manages the display of entered details.

<b>Dependencies:</b> The code relies on external classes for employees and vehicles (Employee, Veichle, EmployeeFT, EmployeePT, EmployeeINTL), which are assumed to be defined in separate modules.
