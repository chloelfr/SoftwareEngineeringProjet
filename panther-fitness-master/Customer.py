from datetime import datetime
from User import User
from TrainingProgress import TrainingProgress
from DietProgress import DietProgress
from CustomerSchedule import customer_schedule
from Services import Services
from MembershipPackage import MembershipPackage
from pprint import pprint


class Customer(User):

    def __init__(self, name, email, password, current_package_level, credit_card=None, cvc=None, billing_address=None):
        User.__init__(self, name, email, password, 'customer')
        self.membership_package = MembershipPackage(current_package_level)
        self.credit_card = credit_card
        self.cvc = cvc
        self.billing_address = billing_address
        self.training_progress = TrainingProgress()
        self.diet_progress = DietProgress()
        self.services = Services()
        self.attendance = {'monday': 0, 'tuesday': 0, 'wednesday': 0,
                           'thursday': 0, 'friday': 0, 'saturday': 0, 'sunday': 0}


    '''
    ----------------------------------------------------------------------------
    check_in function
    calling the attendance dicionary to keep track of daily attendance during each week 
    '''
    def check_in(self):
        day = datetime.today().weekday()
        if day == 0:
            self.attendance['monday'] += 1
        elif day == 1:
            self.attendance['tuesday'] += 1
        elif day == 2:
            self.attendance['wednesday'] += 1
        elif day == 3:
            self.attendance['thursday'] += 1
        elif day == 4:
            self.attendance['friday'] += 1
        elif day == 5:
            self.attendance['saturday'] += 1
        elif day == 6:
            self.attendance['sunday'] += 1

    '''
    -----------------------------------------------------------------------------------------
    display_bill function that checks the current package level of the customer
    and adds that much to their monthly bill
    it also adds extra dietitian, trainer, and massage therapist services account_option
    their bills
    '''
    def display_bill(self):
        print('----------------------------------------------------------------------------------------------------------')
        monthly_bill = 0
        if self.membership_package.current_package == 'bronze':
            print('Bronze Package: $10')
            monthly_bill += 10
        elif self.membership_package.current_package == 'silver':
            print('Silver Package: $20')
            monthly_bill += 20
        elif self.membership_package.current_package == 'gold':
            print('Gold Package: $30')
            monthly_bill += 30

        if 'dietitian' in self.services.services_list:
            print('Dietitian: $10')
            monthly_bill += 10
        elif 'massage therapist' in self.services.services_list:
            print('Massage Therapist: $20')
            monthly_bill += 20
        elif 'trainer' in self.services.services_list:
            print('Trainer: $10')
            monthly_bill += 10

        print('Amount Due This Month: ${0}'.format(monthly_bill))

    '''
    ----------------------------------------------------------------------------
    display_training_progress function
    uses the training_progress class to output the customer's current training progress
    '''
    def display_training_progress(self):
        self.training_progress.display_training_progress()

    '''
    ----------------------------------------------------------------------------
    display_current_package_info function
    uses the membership package class to display the customer's current package
    '''
    def display_current_package_info(self):
        self.membership_package.display_my_package_info()

    '''
    ----------------------------------------------------------------------------
    change_package_level function
    calls the membership package class to change the customer's current membership package
    '''
    def change_package_level(self):
        self.membership_package.change_membership_package()

    '''
    ----------------------------------------------------------------------------
    display_package_descriptions function
    calls the membership package class to display all of the package levels and what
    comes included in each package level
    '''
    def display_package_descriptions(self):
        self.membership_package.display_package_levels()

    '''
    ----------------------------------------------------------------------------
    display_my_trainer_schedule function
    calls the customer schedule class to display the schedule of the customer's
    trainer on that day
    '''
    def display_my_trainer_schedule(self):
        customer_schedule.display_trainer_schedule(self.name)

    '''
    ----------------------------------------------------------------------------
    display_my_dietitian_schedule function
    calls the customer schedule class to display the schedule of the customer's
    dietitian on that day
    '''
    def display_my_dietitian_schedule(self):
        customer_schedule.display_dietitian_schedule(self.name)

    '''
    ----------------------------------------------------------------------------
    display_diet_progress function
    prints the current weight, target weight, and daily calorie intake if the
    current customer by calling the display diet progress function in the
    diet progress class
    '''
    def display_diet_progress(self):
        self.diet_progress.display_diet_progress()

    '''
    ----------------------------------------------------------------------------
    schedule_trainer function
    allows the customer to choose a trainer, day of the week, and time and add it
    to the trainers and customers schedule
    '''
    def schedule_trainer(self):
        if 'trainer' in self.services.services_list or self.membership_package.current_package == 'silver' or self.membership_package.current_package == 'gold':
            day = input('Day of the Week: ')
            time = input('Time: ')
            customer_schedule.schedule_trainer(self.name, day, time)
        else:
            print(
                'Please add a trainer to your services if you would like to schedule a trainer.')

    '''
    ----------------------------------------------------------------------------
    schedule_dietitian function
    allows the customer to choose a dietitian, day of the week, and time and add it
    to the dietitians and customers schedule
    '''
    def schedule_dietitian(self):
        if 'dietitian' in self.services.services_list or self.membership_package.current_package == 'gold':
            day = input('Day of the Week: ')
            time = input('Time: ')
            customer_schedule.schedule_dietitian(self.name, day, time)
        else:
            print(
                'Please add a dietitian to your services if you would like to schedule a dietitian.')

    '''
    ----------------------------------------------------------------------------
    add_service function
    calling the services class to use the add service function, and appends it to
    the services list for the current customer
    '''
    def add_service(self):
        service = input('Service to Add: ')
        service = service.lower()

        if service == 'trainer' or service == 'dietitian' or service == 'massage therapist':
            self.services.add_service(service)
        else:
            print('Service not recognized. Please try again.')

    '''
    ----------------------------------------------------------------------------
    remove_service function
    calling the services class to use the remove service function, and removes it from
    the services list for the current customer
    '''
    def remove_service(self):
        service = input('Service to Remove: ')
        service = service.lower()

        if service == 'trainer' or service == 'dietitian' or service == 'massage therapist':
            self.services.remove_service(service)
        else:
            print('Service not recognized. Please try again.')

    '''
    ----------------------------------------------------------------------------
    display_my_services function
    calling the services class to use the display my services function, which
    prints the services that the customer currently contain in the services list 
    '''
    def display_my_services(self):
        print('----------------------------------------------------------------------------------------------------------')
        print('Your Current Services:')
        self.services.display_my_services()
        print('----------------------------------------------------------------------------------------------------------')

