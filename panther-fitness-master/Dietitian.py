from User import User
from CustomerDatabase import customer_database
from EmployeeSchedule import employee_schedule
from pprint import pprint

class Dietitian(User):
    def __init__(self, name, email, password):
        User.__init__(self, name, email, password, 'dietitian')

    '''
    ----------------------------------------------------------------------------
    update_customer_calorie_intake function
    requests input of customer's name and new daily calory intake to change that
    customer object's daily calory intake
    '''
    def update_customer_calorie_intake(self):
        print('----------------------------------------------------------------------------------------------------------')
        customer_name = input('Customer Name: ')
        customer_name = customer_name.lower()
        new_calories = input('Updated Daily Calorie Intake: ')
        customer_database.individuals[customer_name].diet_progress.update_calorie_intake(new_calories)

    '''
    ----------------------------------------------------------------------------
    update_customer_current_weight function
    requests input of customer's name and new current weight to change that
    customer object's newest weight for that customer
    '''
    def update_customer_current_weight(self):
        print('----------------------------------------------------------------------------------------------------------')
        customer_name = input('Customer Name: ')
        customer_name = customer_name.lower()
        new_weight = input('Updated Current Weight: ')
        customer_database.individuals[customer_name].diet_progress.update_current_weight(new_weight)

    '''
    ----------------------------------------------------------------------------
    update_customer_target_weight function
    requests input of customer's name and new target weight to change that
    customer object's newest target weight for that customer
    '''
    def update_customer_target_weight(self):
        print('----------------------------------------------------------------------------------------------------------')
        customer_name = input('Customer Name: ')
        customer_name = customer_name.lower()
        new_target_weight = input('Updated Target Weight: ')
        customer_database.individuals[customer_name].diet_progress.update_target_weight(new_target_weight)


    def display_customer_diet_progress(self):
        print('----------------------------------------------------------------------------------------------------------')
        customer_name = input('Customer Name: ')
        customer_name = customer_name.lower()
        customer_database.individuals[customer_name].diet_progress.display_diet_progress()

    '''
    ----------------------------------------------------------------------------
    display_my_schedule function
    calls the display_employee_schedule function from the employee_schedule class
    printing the schedule dictionary with the days of the week for keys and lists
    for each day
    '''
    def display_my_schedule(self):
        employee_schedule.display_employee_schedule(self.name)
