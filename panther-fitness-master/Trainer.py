from User import User
from CustomerDatabase import customer_database
from EmployeeSchedule import employee_schedule
from pprint import pprint

class Trainer(User):
    def __init__(self, name, email, password):
        User.__init__(self, name, email, password, 'trainer')

    '''
    ----------------------------------------------------------------------------
    update_customer_bench_press function
    requests input of customer's name and new bench press weight to change that
    customer object's bench press weight
    '''
    def update_customer_bench_press(self):
        name = input('Customer Name:\n')
        name = name.lower()
        new_bench_press = input('Updated Bench Press Weight:\n')
        customer_database.individuals[name].training_progress.update_bench_press(new_bench_press)

    '''
    ----------------------------------------------------------------------------
    update_customer_bench_press_goal function
    requests input of customer's name and new bench press goal weight to change that
    customer object's bench press goal weight
    '''
    def update_customer_bench_press_goal(self):
        name = input('Customer Name:\n')
        name = name.lower()
        new_bench_press_goal = input('Updated Bench Press Weight Goal:\n')
        customer_database.individuals[name].training_progress.update_bench_press_goal(new_bench_press_goal)
        
    '''
    ----------------------------------------------------------------------------
    update_customer_squat function
    requests input of customer's name and new squat weight to change that
    customer object's squat weight
    '''
    def update_customer_squat(self):
        name = input('Customer Name:\n')
        name = name.lower()
        new_squat = input('Updated Squat Weight:\n')
        customer_database.individuals[name].training_progress.update_squat(new_squat)
    '''
    ----------------------------------------------------------------------------
    update_customer_squat_goal function
    requests input of customer's name and new squat goal weight to change that
    customer object's squat goal weight
    '''
    def update_customer_squat_goal(self):
        name = input('Customer Name:\n')
        name = name.lower()
        new_squat_goal = input('Updated Squat Weight Goal:\n')
        customer_database.individuals
        
    '''
    ----------------------------------------------------------------------------
    update_customer_mile_time function
    requests input of customer's name and new mile time to change that
    customer object's mile time
    '''
    def update_customer_mile_time(self):
        name = input('Customer Name:\n')
        name = name.lower()
        new_time = input('Updated Mile Time:\n')
        customer_database.individuals[name].training_progress.update_mile_time(new_time)

    '''
    ----------------------------------------------------------------------------
    update_customer_mile_time_goal function
    requests input of customer's name and new mile time goal to change that
    customer object's mile time goal
    '''
    def update_customer_mile_time_goal(self):
        name = input('Customer Name:\n')
        name = name.lower()
        new_time_goal = input('Updated Mile Time Goal:\n')
        customer_database.individuals[name].training_progress.update_mile_time_goal(new_time_goal)

    '''
    ----------------------------------------------------------------------------
    update_customer_weight function
    requests input of customer's name and new weight to change that
    customer object's current weight
    '''
    def update_customer_weight(self):
        name = input('Customer Name:\n')
        name = name.lower()
        new_weight = input('Updated Customer Weight:\n')
        customer_database.individuals[name].training_progress.update_weight(new_weight)

    '''
    ----------------------------------------------------------------------------
    display_customer_progress function
    requests input of customer's name and calls the training_progress class to use
    the display_training_progress function and display the customer object's stats
    '''
    def display_customer_progress(self):
        customer_name = input('Customer Name:\n')
        customer_name = customer_name.lower()

        if customer_name in customer_database.individuals.keys():
            customer_database.individuals[customer_name].training_progress.display_training_progress()
        else:
            print('Customer not recognized.')
            
    '''
    ----------------------------------------------------------------------------
    display_my_schedule function
    display's the current employee's schedule based on the name of the employee
    '''
    def display_my_schedule(self):
        employee_schedule.display_employee_schedule(self.name)
