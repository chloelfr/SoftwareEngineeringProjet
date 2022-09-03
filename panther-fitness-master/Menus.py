"""
All Menus will be displayed and will wait for the user to type in a response. The user must spell whatever
option they choose correctly but the options are not case sensetive. The menus file is used to display the
possible choices to the user.
"""

#Display for the home menu for the system
def display_start_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('Welcome to Panther Fitness!\n')
    print('Sign In            Sign Up\n')
    print('\n\nPower Off')
    print('----------------------------------------------------------------------------------------------------------')
    return input('\nWhat would you like to do?\n')

#Display for shown to all customers
def display_customer_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nCheck In\n')
    print('My Account\n')
    print('View Trainer Schedule\n')
    print('View Dietitian Schedule\n')
    print('View Current Package Details\n')
    print('View Training Progress\n')
    print('View Diet Progress\n')
    print('Add Service\n')
    print('Remove Service\n')
    print('Schedule a Trainer\n')
    print('Schedule a Dietitian\n')
    print('Log Out\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Please enter an option from above:\n')

#Display for the customers account menu
def display_customer_account_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nChange Email\n')
    print('Change Password\n')
    print('Change Membership Package\n')
    print('View Bill\n')
    print('Cancel Membership\n')
    print('Back\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Please enter an option from above:\n')

#Display the trainers menu
def display_trainer_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nMy Account\n')
    print('View Customer Progress\n')
    print('Update Customer Progress\n')
    print('View Employee Schedule\n')
    print('Log Out\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Please enter an option from above:\n')

#Display the dietitian menu
def display_dietitian_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nMy Account\n')
    print('View Customer Diet Progress\n')
    print('Update Customer Diet Progress\n')
    print('View Employee Schedule\n')
    print('Log Out\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Please enter an option from above:\n')

#Display the training progress update menu
def display_training_progress_update_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nUpdate Bench Press\n')
    print('Update Bench Press Goal\n')
    print('Update Squat\n')
    print('Update Squat Goal\n')
    print('Update Mile Time\n')
    print('Update Mile Time Goal\n')
    print('Update Current Weight\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('What would you like to update?\n')

#Display the diet progress update menu
def display_diet_progress_update_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nUpdate Daily Calorie Intake\n')
    print('Update Current Weight\n')
    print('Update Target Weight\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('What would you like to update?\n')
   

#Display employee account menu
def display_employee_account_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nChange Email\n')
    print('Change Password\n')
    print('Back\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Please enter an option from above:\n')

#Display the manager's menu
def display_manager_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nMy Account\n')
    print('View Customer Trainer Schedule Requests\n')
    print('View Customer Dietitian Schedule Requests\n')
    print('Add Employee To Schedule\n')
    print('Remove Employee From Schedule\n')
    print('Generate or Update Report\n')
    print('View Customer Progress\n')
    print('Update Customer Progress\n')
    print('View Employee Schedule\n')
    print('Add Employee To Database\n')
    print('Remove Employee From Database\n')
    print('View Employee Database\n')
    print('Remove Customer From Database\n')
    print('View Customer Database\n')
    print('Log Out\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Please enter an option from above:\n')

def display_manager_report_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nGenerate Attendance Report\n')
    print('Clear Attendance Report\n')
    print('Generate Monthly Revenue Report\n')
    print('Update Monthly Revenue\n')
    print('Clear Monthly Revenue\n')
    print('Generate Annual Revenue Report\n')
    print('Clear Annual Revenue Report\n')
    print('Back\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Report to generate:\n')

def display_package_levels():
    print('----------------------------------------------------------------------------------------------------------')
    print('Bronze: INCLUDES Cardio, Weights & Machines, Locker Rooms with Showers')
    print('Silver: INCLUDES Cardio, Weights & Machines, Locker Rooms with Showers, Schedule a Trainer Once a Week')
    print('Gold: INCLUDES Cardio, Weights & Machines, Locker Rooms with Showers, Schedule a Trainer Once a Week, Schedule a Dietitian Once a Week')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Package level:\n')

#Display the massage therapist menu
def display_massageTherapist_menu():
    print('----------------------------------------------------------------------------------------------------------')
    print('\nMy Account\n')
    print('View schedule\n')
    print('Log Out\n')
    print('----------------------------------------------------------------------------------------------------------')
    return input('Please enter an option from above:\n')

#Display the services menu
def show_available_services():
    print('----------------------------------------------------------------------------------------------------------')
    print('Trainer: Description...') 
    print('Dietitian: Description...') 
    print('Massage Therapist: Description...') 
    print('----------------------------------------------------------------------------------------------------------')
