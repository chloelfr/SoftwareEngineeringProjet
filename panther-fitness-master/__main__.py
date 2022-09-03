# Python modules
import time
import os

# Product modules
import Menus
from Customer import Customer
from Trainer import Trainer
from Dietitian import Dietitian
from Manager import Manager
from CustomerDatabase import customer_database
from EmployeeDatabase import employee_database
from EmployeeSchedule import employee_schedule
from CustomerSchedule import customer_schedule

# Main function to run the terminal
def __main__():
    # System powers off only for maintenance
    # Populates database-like modules
    customer_database.read_from_file('CustomerDatabase.pickle')
    employee_database.read_from_file('EmployeeDatabase.pickle')
    employee_schedule.read_from_file('EmployeeSchedule.pickle')
    customer_schedule.read_trainer_schedule_from_file('CustomerScheduleTrainer.pickle')
    customer_schedule.read_dietitian_schedule_from_file('CustomerScheduleDietitian.pickle')

    # Primary module of main - Only stops when someone powers off the terminal
    running = True
    while running:
        os.system('clear')

        # Startup menu - Sign In, Sign Up, Power Off
        option = Menus.display_start_menu()
        option = option.lower()

        if option == 'sign in':
            attempts_remaining = 5

            signed_in = False
            user_name = ''
            while attempts_remaining > 0 and not signed_in:
                email = input('\nEmail: ')
                password = input('Password: ')

                # Checks customer database for user
                for name in customer_database.individuals:
                    if customer_database.individuals[name].email == email and customer_database.individuals[name].password == password:
                        # Admits user into system
                        os.system('clear')
                        print('\nWelcome {0}!'.format(name.capitalize()))
                        user_name = name
                        signed_in = True
                        break
                    elif (customer_database.individuals[name].email == email and customer_database.individuals[name].password != password) or (customer_database.individuals[name].email != email and customer_database.individuals[name].password == password):
                        # User loses a sign in attempt if either their email or password is in the db, but they get the other wrong
                        attempts_remaining -= 1
                        print('\nEmail or Password Incorrect')
                        print('Attempts Remaining:', attempts_remaining)

                if signed_in:
                    break

                for name in employee_database.individuals:
                    if employee_database.individuals[name].email == email and employee_database.individuals[name].password == password:
                        # Admits user into system
                        os.system('clear')
                        print('\nWelcome {0}!'.format(name.capitalize()))
                        user_name = name
                        signed_in = True
                        break
                    elif (employee_database.individuals[name].email == email and employee_database.individuals[name].password != password) or (employee_database.individuals[name].email != email and employee_database.individuals[name].password == password):
                        # User loses a sign in attempt if either their email or password is in the db, but they get the other wrong
                        attempts_remaining -= 1
                        print('\nEmail or Password Incorrect')
                        print('Attempts Remaining:', attempts_remaining)

                # If neither email or password is recognized, nothing happens
                if not signed_in:
                    print('Email and Password not Recognized')

            # Customer menus
            if user_name in customer_database.individuals.keys() and customer_database.individuals[user_name].account_type == 'customer':
                customer = customer_database.individuals[user_name]

                while signed_in:
                    customer_option = Menus.display_customer_menu()
                    customer_option = customer_option.lower()

                    print('\n----------------------------------------------------------------------------------------------------------')
                    # Customer checks in => They are signed out and attendance is recorded
                    if customer_option == 'check in':
                        customer.check_in()
                        print('\nYou are checked in! Enjoy your workout!')
                        print('Signing you out...\n')
                        signed_in = False
                    # Customer navigates to their account
                    # Customer can change email, password, membership package, cancel their membership, view bill or go back
                    elif customer_option == 'my account':
                        os.system('clear')
                        viewing_account = True
                        while viewing_account:
                            account_option = Menus.display_customer_account_menu()
                            account_option = account_option.lower()

                            if account_option == 'change email':
                                new_email = input('New Email: ')
                                customer.change_email(new_email)

                            elif account_option == 'change password':
                                confirm_password = False
                                while not confirm_password:
                                    new_password = input('New Password: ')
                                    check_password = input(
                                        'Confirm Password: ')
                                    if new_password == check_password:
                                        customer.change_password(new_password)
                                        confirm_password = True
                                    else:
                                        print(
                                            'Passwords did not match. Please try again.')

                            elif account_option == 'change membership package':
                                customer.change_package_level()

                            elif account_option == 'view bill':
                                customer.display_bill()

                            elif account_option == 'cancel membership':
                                print('Are you sure you want to cancel?')
                                answer = input('Yes/No\n')
                                answer = answer.lower()

                                if answer == 'yes':
                                    customer_database.remove_user(user_name)
                                    print('Membership cancelled. Please come and see us again!')
                                    time.sleep(2)
                                    viewing_account = False
                                    logged_in = False
                                    break
                                elif answer == 'no':
                                    print('Thanks for sticking around!')

                            elif account_option == 'back':
                                viewing_account = False
                            else:
                                print('Menu option not recognized.')
                        os.system('clear')

                    # Customer can view their scheduled trainer appointment
                    elif customer_option == 'view trainer schedule':
                        customer.display_my_trainer_schedule()

                    # Customer can view their scheduled dietitian appointment
                    elif customer_option == 'view dietitian schedule':
                        customer.display_my_dietitian_schedule()

                    # Customer can view the details of their current package
                    elif customer_option == 'view current package details':
                        customer.display_current_package_info()

                    # Customer can view their training progress
                    elif customer_option == 'view training progress':
                        customer.display_training_progress()

                    # Customer can view their diet progress
                    elif customer_option == 'view diet progress':
                        customer.display_diet_progress()

                    # Customer can request to schedule a trainer
                    elif customer_option == 'schedule a trainer':
                        customer.schedule_trainer()

                    # Customer can request to schedule a dietitian
                    elif customer_option == 'schedule a dietitian':
                        customer.schedule_dietitian()

                    # Customer can add a service (trainer or dietitian)
                    elif customer_option == 'add service':
                        print('----------------------------------------------------------------------------------------------------------')
                        Menus.show_available_services()
                        customer.add_service()

                    # Customer can remove a service from their bill
                    elif customer_option == 'remove service':
                        customer.display_my_services()
                        customer.remove_service()

                    # Customer can log out
                    elif customer_option == 'log out':
                        signed_in = False
                    else:
                        print('What you have entered is not an option\n')

                    input('Press ENTER to Continue...')
                    os.system('clear')

            # Trainer menus
            elif user_name in employee_database.individuals.keys() and employee_database.individuals[user_name].account_type == 'trainer':
                trainer = employee_database.individuals[user_name]

                while signed_in:
                    trainer_option = Menus.display_trainer_menu()
                    trainer_option = trainer_option.lower()

                    # Takes trainer to their account
                    # Trainer can change email, password or go back
                    if trainer_option == 'my account':
                        viewing_account = True
                        while viewing_account:
                            os.system('clear')
                            account_option = Menus.display_employee_account_menu()
                            account_option = account_option.lower()

                            if account_option == 'change email':
                                new_email = input('New Email: ')
                                trainer.change_email(new_email)

                            elif account_option == 'change password':
                                confirm_password = False
                                while not confirm_password:
                                    new_password = input('New Password: ')
                                    check_password = input(
                                        'Confirm Password: ')
                                    if new_password == check_password:
                                        trainer.change_password(new_password)
                                        confirm_password = True
                                    else:
                                        print(
                                            'Passwords did not match. Please try again.')

                            elif account_option == 'back':
                                viewing_account = False
                            else:
                                print('Menu option not recognized.')

                    # Trainer can view any customer's training progress
                    elif trainer_option == 'view customer progress':
                        trainer.display_customer_progress()

                    # Trainer can update any customer's training progress
                    elif trainer_option == 'update customer progress':
                        update = Menus.display_training_progress_update_menu()
                        update = update.lower()

                        if update == 'update bench press':
                            trainer.update_customer_bench_press()
                        elif update == 'update bench press goal':
                            trainer.update_customer_bench_press_goal()
                        elif update == 'update squat':
                            trainer.update_customer_squat()
                        elif update == 'update squat goal':
                            trainer.update_customer_squat_goal()
                        elif update == 'update mile time':
                            trainer.update_customer_mile_time()
                        elif update == 'update mile time goal':
                            trainer.update_customer_mile_time_goal()
                        elif update == 'update current weight':
                            trainer.update_customer_weight()
                        else:
                            print('Option not recognized. Please try again.')
                        os.system('clear')

                    # Trainer can view their own schedule
                    elif trainer_option.lower() == 'view employee schedule':
                        trainer.display_my_schedule()

                    # Trainer can log out
                    elif trainer_option.lower() == 'log out':
                        signed_in = False
                    else:
                        print('What you have entered is not an option\n')

                    input('Press ENTER to Continue...')
                    os.system('clear')

            # Manager menus
            elif user_name in employee_database.individuals.keys() and employee_database.individuals[user_name].account_type == 'manager':
                manager = employee_database.individuals[user_name]

                while signed_in:
                    manager_option = Menus.display_manager_menu()
                    manager_option = manager_option.lower()

                    # Takes manager to their account
                    # Manager can change email, password or go back
                    if manager_option.lower() == 'my account':
                        os.system('clear')
                        viewing_account = True
                        while viewing_account:
                            account_option = Menus.display_employee_account_menu()
                            account_option = account_option.lower()

                            if account_option.lower() == 'change email':
                                new_email = input('New Email: ')
                                manager.change_email(new_email)
                                print('Email successfully changed!')
                                time.sleep(2)

                            elif account_option.lower() == 'change password':
                                confirm_password = False
                                while not confirm_password:
                                    new_password = input('New Password: ')
                                    check_password = input(
                                        'Confirm Password: ')
                                    if new_password == check_password:
                                        manager.change_password(new_password)
                                        print('Password successfully changed!')
                                        time.sleep(2)
                                        confirm_password = True
                                    else:
                                        print('Passwords did not match. Please try again.')
                            elif account_option == 'back':
                                viewing_account = False

                            os.system('clear')

                    # Manager can view trainer requests by customers
                    elif manager_option == 'view customer trainer schedule requests':
                        manager.display_customer_trainer_schedule()

                    # Manager can view dietitian requests by customers
                    elif manager_option == 'view customer dietitian schedule requests':
                        manager.display_customer_dietitian_schedule()

                    # Manager can add an employee to the schedule
                    elif manager_option == 'add employee to schedule':
                        manager.add_employee_to_schedule()

                    # Manager can remove an employee from the schedule
                    elif manager_option == 'remove employee from schedule':
                        manager.remove_employee_from_schedule()

                    # Manager can view or update various reports
                    elif manager_option == 'generate or update report':
                        os.system('clear')
                        report_menu = True
                        while report_menu:
                            report_option = Menus.display_manager_report_menu()
                            report_option = report_option.lower()

                            if report_option == 'generate attendance report':
                                manager.generate_attendance_report()
                            elif report_option == 'clear attendance report':
                                manager.clear_attendance_report()
                            elif report_option == 'generate monthly revenue report':
                                manager.generate_monthly_revenue_report()
                            elif report_option == 'update monthly revenue':
                                manager.update_monthly_revenue()
                            elif report_option == 'clear monthly revenue':
                                manager.clear_monthly_revenue()
                            elif report_option == 'generate annual revenue report':
                                manager.generate_annual_revenue_report()

                            elif report_option == 'clear annual revenue':
                                manager.clear_annual_revenue()
                            elif report_option == 'back':
                                report_menu = False
                            else:
                                print('Option not recognized. Please try again.')

                            input('Press ENTER to Continue...')
                            os.system('clear')

                    # Manager can act as a trainer and view or update customer progress
                    elif manager_option.lower() == 'view customer progress':
                        manager.display_customer_progress()
                    elif manager_option.lower() == 'update customer progress':
                        update = Menus.display_training_progress_update_menu()
                        update = update.lower()

                        if update == 'update bench press':
                            manager.update_customer_bench_press()
                        elif update == 'update bench press goal':
                            manager.update_customer_bench_press_goal()
                        elif update == 'update squat':
                            manager.update_customer_squat()
                        elif update == 'update squat goal':
                            manager.update_customer_squat_goal()
                        elif update == 'update mile time':
                            manager.update_customer_mile_time()
                        elif update == 'update mile time goal':
                            manager.update_customer_mile_time_goal()
                        elif update == 'update current weight':
                            manager.update_customer_weight()
                        else:
                            print('Option not recognized. Please try again.')
                        os.system('clear')

                    # Manager can view the employee schedule
                    elif manager_option == 'view employee schedule':
                        manager.display_employee_schedule()

                    # Manager can add employees to the database using a temporary password, which the employee will later change
                    elif manager_option == 'add employee to database':
                        manager.add_employee_to_database()

                    # Manager can remove employees from the database
                    elif manager_option == 'remove employee from database':
                        manager.remove_employee_from_database()

                    # Manager can view the employee database
                    elif manager_option == 'view employee database':
                        print('----------------------------------------------------------------------------------------------------------')
                        manager.display_employee_database()
                        print('----------------------------------------------------------------------------------------------------------')

                    # Manager can remove customers from the database
                    elif manager_option == 'remove customer from database':
                        manager.remove_customer_from_database()

                    # Manager can view the customer database
                    elif manager_option == 'view customer database':
                        print('----------------------------------------------------------------------------------------------------------')
                        manager.display_customer_database()
                        print('----------------------------------------------------------------------------------------------------------')

                    elif manager_option == 'log out':
                        signed_in = False
                    else:
                        print('What you have entered is not an option\n')

                    input('Press ENTER to Continue...')
                    os.system('clear')

            # Dietitian menus
            elif user_name in employee_database.individuals.keys() and employee_database.individuals[user_name].account_type == 'dietitian':
                dietitian = employee_database.individuals[user_name]

                while signed_in:
                    dietitian_option = Menus.display_dietitian_menu()
                    dietitian_option = dietitian_option.lower()

                    # Dietitian can view any customer's progress
                    if dietitian_option == 'view customer diet progress':
                        dietitian.display_customer_diet_progress()

                    # Dietitian can update any customer's progress
                    elif dietitian_option == 'update customer diet progress':
                        os.system('clear')

                        update = Menus.display_diet_progress_update_menu()
                        update = update.lower()

                        if update == 'update daily calorie intake':
                            dietitian.update_customer_calorie_intake()
                        elif update == 'update current weight':
                            dietitian.update_customer_current_weight()
                        elif update == 'update target weight':
                            dietitian.update_customer_target_weight()
                        else:
                            print('Option not recognized. Please try again.')

                        os.system('clear')
                        
                    # Dietitian can view their schedule
                    elif dietitian_option == 'view employee schedule':
                        dietitian.display_my_schedule()

                    # Dietitian can log out
                    elif dietitian_option == 'log out':
                        signed_in = False
                    else:
                        print('What you have entered is not an option\n')

                    input('Press ENTER to Continue...')
                    os.system('clear')

            if attempts_remaining == 0:
                print('Terminal Locked')
                time.sleep(5)

        # A User can sign up as a customer
        elif option == 'sign up':

            # User must enter their name
            need_name = True
            while need_name:
                customer_name = input('Name: ')
                if customer_name != '':
                    customer_name = customer_name.lower()
                    need_name = False
                else:
                    print('Please input your name.')

            # User must enter an email
            need_email = True
            while need_email:
                email = input('Email: ')
                if email != '':
                    need_email = False
                else:
                    print('Please input a valid email')

            # User must enter a password and confirm it
            password_confirmed = False
            while not password_confirmed:
                password = input('Password: ')
                check_password = input('Confirm Password: ')
                if password == check_password:
                    password_confirmed = True
                else:
                    print('\nPasswords Did Not Match. Please Try Again.\n')

            # User must enter billing information
            print('Billing Information:\n')
            need_cc = True
            while need_cc:
                credit_card = input('Credit Card: ')
                if credit_card != '':
                    need_cc = False
                else:
                    print('Please input a valid credit card')

            cvc = input('CVC: ')
            billing_address = input('Billing Address: ')

            # Displays package info
            # User must pick a valid package
            reading_package = True
            while reading_package:
                package_level = Menus.display_package_levels()
                package_level = package_level.lower()
                if package_level == 'bronze' or package_level == 'silver' or package_level == 'gold':
                    customer = Customer(customer_name.lower(
                    ), email, password, package_level, credit_card, cvc, billing_address)
                    customer_database.add_user(customer_name, customer)
                    reading_package = False
                else:
                    print('Package not recognized. Please input either Bronze, Silver, or Gold')

            print('\nPlease Log In to Access Your Account. Thanks For Signing Up!')
            time.sleep(3)
            os.system('clear')

        # If powered off writes all database-like structures to files
        elif option == 'power off':
            print('\nShutting Down Terminal...')
            customer_database.write_to_file('CustomerDatabase.pickle')
            employee_database.write_to_file('EmployeeDatabase.pickle')
            employee_schedule.write_to_file('EmployeeSchedule.pickle')
            customer_schedule.write_trainer_schedule_to_file('CustomerScheduleTrainer.pickle')
            customer_schedule.write_dietitian_schedule_to_file('CustomerScheduleDietitian.pickle')
            running = False

        else:
            print('\nOption Not Recognized')
            print('Please Try Again!\n')
            continue


__main__()
