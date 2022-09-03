import pickle
from EmployeeDatabase import employee_database

class EmployeeSchedule:
    def __init__(self):
        self.schedule = {}

    '''
    schedule dictionaries with days of the week as keys to embedded lists
    these other lists are meant to hold times
    '''
    def add_employee(self, name, day, time):
        if name in self.schedule.keys():
            self.schedule[name][day].append(time)
        else:
            self.schedule[name] = {
                'monday': [],
                'tuesday': [],
                'wednesday': [],
                'thursday': [],
                'friday': [],
                'saturday': [],
                'sunday': []
            }
            if name in employee_database.individuals.keys() and day in self.schedule[name].keys():
                self.schedule[name][day] = [time]
            else:
                print('Error. Make sure that the employee is in the employee database and that you did not mistype the day of the week\n')

    '''
    ----------------------------------------------------------------------------
    remove_employee function
    deletes an employee from the dictionary
    '''
    def remove_employee(self, name, day, time):
        self.schedule[name][day].remove(time)

    '''
    ----------------------------------------------------------------------------
    clear_all_schedules function
    deletes all keys and values from the dictionary
    '''
    def clear_all_schedules(self):
        self.schedule.clear()

    '''
    ----------------------------------------------------------------------------
    display_entire_schedule function
    prints the entire schedule dictionary 
    both keys and value lists
    '''
    def display_entire_schedule(self):
        for key in self.schedule:
            print('{0}:'.format(key.upper()))
            self.display_employee_schedule(key)

    '''
    ----------------------------------------------------------------------------
    display_employee_schedule function
    prints all of the employees in the dictionary 
    both keys and value lists
    '''
    def display_employee_schedule(self, name):
        print('-----------------------------------------------')
        if name in self.schedule.keys():
            for key in self.schedule[name]:
                print(key.upper())
                print('-----------------------')
                self.display_day_schedule(self.schedule[name][key])
        else:
            print('Weekly schedule not available yet.')

    '''
    ----------------------------------------------------------------------------
    display_day_schedule function
    prints all scheduled appointments by time on that day 
    '''
    def display_day_schedule(self, day_schedule):
        for time in day_schedule:
            print(time)

        print('\n')

    '''
    ----------------------------------------------------------------------------
    writes an output to a pickle file and creates a readable file to retain data
    between shutdowns of the system 
    '''
    def write_to_file(self, file_name):
        with open(file_name, 'wb') as handle:
            pickle.dump(self.schedule, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def read_from_file(self, file_name):
        with open(file_name, 'rb') as handle:
            self.schedule = pickle.load(handle)

employee_schedule = EmployeeSchedule()
