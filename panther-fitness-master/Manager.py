from User import User
from pprint import pprint
from Trainer import Trainer
from Dietitian import Dietitian
from CustomerDatabase import customer_database
from EmployeeDatabase import employee_database
from EmployeeSchedule import employee_schedule
from CustomerSchedule import customer_schedule
from ManagerReport import ManagerReport

class Manager(User):
    def __init__(self, name, email, password):
        User.__init__(self, name, email, password, 'manager')
        self.report = ManagerReport()

    '''
    ----------------------------------------------------------------------------
    remove_customer_from_database function
    calls the database dictionary from the customer_database class to remove a current customer
    takes customer name as input
    '''
    def remove_customer_from_database(self):
        customer_name = input('Customer Name: ')
        customer_name = customer_name.lower()
        customer_database.remove_user(customer_name)

    '''
    ----------------------------------------------------------------------------
    add_employee_to_database function
    calls the individuals dictionary from the employee_database class to add a new employee
    takes employee type, name, email, temporary password
    '''
    def add_employee_to_database(self):
        employee_type = input('Employee Type: ')
        name = input('Employee Name: ')
        name = name.lower()
        email = input('Email: ')
        password = input('Temporary Password: ')

        if employee_type.lower() == 'trainer':
            employee = Trainer(name, email, password)
        elif employee_type.lower() == 'dietitian':
            employee = Dietitian(name, email, password)

        employee_database.add_user(name, employee)

    '''
    ----------------------------------------------------------------------------
    remove_employee_from_database function
    calls the individuals dictionary from the employee_database class to remove an employee
    takes employee type, name, email, temporary password
    '''
    def remove_employee_from_database(self):
        employee_name = input('Employee Name: ')
        employee_name = employee_name.lower()
        employee_database.remove_user(employee_name)

    '''
    ----------------------------------------------------------------------------
    add_employee_to_schedule function
    calls the schedule dictionary from the employee_schedule class to add an employee
    takes employee name, day, and time
    '''
    def add_employee_to_schedule(self):
        name = input('Employee Name: ')
        name = name.lower()
        day = input('Day: ')
        day = day.lower()
        time = input('Time: ')
        employee_schedule.add_employee(name, day, time)

    '''
    ----------------------------------------------------------------------------
    remove_employee_from_schedule function
    calls the schedule dictionary from the employee_schedule class to remove an employee
    deletes employee name, day, and time
    '''
    def remove_employee_from_schedule(self):
        name = input('Employee Name: ')
        name = name.lower()
        day = input('Day: ')
        day = day.lower()
        time = input('Time: ')
        employee_schedule.remove_employee(name, day, time)

    '''
    ----------------------------------------------------------------------------
    display_employee_database function
    calls the individuals array from the employee_database class and uses the 
    display_users to print the current employees
    '''
    def display_employee_database(self):
        employee_database.display_users()

    '''
    ----------------------------------------------------------------------------
    display_customer_database function
    calls the individuals array from the customer_database class and uses the 
    dislay_users to print the current customers
    '''
    def display_customer_database(self):
        customer_database.display_users()

    '''
    ----------------------------------------------------------------------------
    display_employee_schedule function
    calls the schedule array from the employee_schedule class and uses the 
    schedule dictionary to print an employee's schedule by their name
    '''
    def display_employee_schedule(self):
        employee_schedule.display_entire_schedule()
        
    '''
    ----------------------------------------------------------------------------
    display_customer_trainer_schedule function
    calls the schedule array from the employee_schedule class and uses the 
    schedule dictionary to print a trainer's schedule by their name
    '''
    def display_customer_trainer_schedule(self):
        customer_schedule.display_trainer_schedule()

    '''
    ----------------------------------------------------------------------------
    display_customer_dietitian_schedule function
    calls the schedule array from the employee_schedule class and uses the 
    schedule dictionary to print a dietitian's schedule by their name
    '''
    def display_customer_dietitian_schedule(self):
        customer_schedule.display_dietitian_schedule()

    '''
    ----------------------------------------------------------------------------
    clear_customer_trainer_schedule function
    calls the schedule array from the employee_schedule class and uses the 
    clear schedule dictionary function the clear the schedule dictionary
    '''
    def clear_customer_trainer_schedule(self):
        customer_schedule.clear_trainer_schedule()

    '''
    ----------------------------------------------------------------------------
    clear_customer_dietitian_schedule function
    calls the schedule array from the employee_schedule class and uses the 
    clear schedule dictionary function the clear the schedule dictionary
    '''
    def clear_customer_dietitian_schedule(self):
        customer_schedule.clear_dietitian_schedule()

    '''
    ----------------------------------------------------------------------------
    update_customer_bench_press function
    requests input of customer's name and new bench press weight to change that
    customer object's bench press weight
    '''
    def update_customer_bench_press(self):
        name = input('Customer Name:')
        new_bench_press = input('Updated Bench Press Weight:')
        customer_database.individuals[name].training_progress.update_bench_press(new_bench_press)

    '''
    ----------------------------------------------------------------------------
    update_customer_bench_press_goal function
    requests input of customer's name and new bench press goal weight to change that
    customer object's bench press goal weight
    '''
    def update_customer_bench_press_goal(self):
        name = input('Customer Name:')
        new_bench_press_goal = input('Updated Bench Press Weight Goal:')
        customer_database.individuals[name].training_progress.update_bench_press_goal(new_bench_press_goal)

    '''
    ----------------------------------------------------------------------------
    update_customer_squat function
    requests input of customer's name and new squat weight to change that
    customer object's squat weight
    '''
    def update_customer_squat(self):
        name = input('Customer Name:')
        new_squat = input('Updated Squat Weight:')
        customer_database.individuals[name].training_progress.update_squat(new_squat)

    '''
    ----------------------------------------------------------------------------
    update_customer_squat_goal function
    requests input of customer's name and new squat goal weight to change that
    customer object's squat goal weight
    '''
    def update_customer_squat_goal(self):
        name = input('Customer Name:')
        new_squat_goal = input('Updated Squat Weight Goal:')
        customer_database.individuals

    '''
    ----------------------------------------------------------------------------
    update_customer_mile_time function
    requests input of customer's name and new mile time to change that
    customer object's mile time
    '''
    def update_customer_mile_time(self):
        name = input('Customer Name:')
        new_time = input('Updated Mile Time:')
        customer_database.individuals[name].training_progress.update_mile_time(new_time)

    '''
    ----------------------------------------------------------------------------
    update_customer_mile_time_goal function
    requests input of customer's name and new mile time goal to change that
    customer object's mile time goal
    '''
    def update_customer_mile_time_goal(self):
        name = input('Customer Name:')
        new_time_goal = input('Updated Mile Time Goal:')
        customer_database.individuals[name].training_progress.update_mile_time_goal(new_time_goal)

    '''
    ----------------------------------------------------------------------------
    update_customer_weight function
    requests input of customer's name and new weight to change that
    customer object's current weight
    '''
    def update_customer_weight(self):
        name = input('Customer Name:')
        new_weight = input('Updated Customer Weight:')
        customer_database.individuals[name].training_progress.update_weight(new_weight)


    '''
    ----------------------------------------------------------------------------
    display_customer_progress function
    requests input of customer's name and calls the training_progress class to use
    the display_training_progress function and display the customer object's stats
    '''
    def display_customer_progress(self):
        customer_name = input('Customer Name: ')
        if customer_name in customer_database.individuals.keys():
            customer_database.individuals[customer_name].training_progress.display_training_progress()
        else:
            print('There is no training progress available for this customer.')

    # This method will print out the attendence report by day
    def generate_attendance_report(self):
        self.report.generate_attendance_report()

    # This method will clear the weekly attendence
    def clear_attendance_report(self):
        self.report.clear_attendance_report()

    # This method will print out the weekly report by day
    def generate_monthly_revenue_report(self):
        self.report.generate_monthly_revenue_report()

    # This method will take an input of dollars to add to this months revenue
    def update_monthly_revenue(self):
        self.report.update_monthly_revenue()
        self.update_annual_revenue()

    # This method clears the weekly revenue
    def clear_monthly_revenue(self):
        self.report.clear_monthly_revenue()

    # This method will print out the annual report
    def generate_annual_revenue_report(self):
        self.report.generate_annual_revenue_report()
    # This method will take an input of dollars to add to this years revenue
    def update_annual_revenue(self):
        self.report.add_monthly_revenue_to_annual_revenue()

    # This method will clear the annual revenue
    def clear_annual_revenue(self):
        self.report.clear_annual_revenue()
