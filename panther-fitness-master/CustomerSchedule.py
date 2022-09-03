import pickle

class CustomerSchedule:
    def __init__(self):
        '''
        schedule dictionaries with days of the week as keys to other dictionaries
        these other dictionaries are meant to hold times
        '''
        self.trainer_schedule = {
            'monday': {},
            'tuesday': {},
            'wednesday': {},
            'thursday': {},
            'friday': {},
            'saturday': {},
            'sunday': {}
        }

        self.dietitian_schedule = {
            'monday': {},
            'tuesday': {},
            'wednesday': {},
            'thursday': {},
            'friday': {},
            'saturday': {},
            'sunday': {}
        }

    '''
    ----------------------------------------------------------------------------
    display_trainer_schedule function
    prints the specified day in the trainer_schedule dictionary
    '''
    def display_trainer_schedule(self, customer_name=None):
        print('----------------------------------------------------------------------------------------------------------')
        if customer_name:
            for day in self.trainer_schedule:
                print(day.upper())
                if customer_name in self.trainer_schedule[day].keys():
                    print(self.trainer_schedule[day][customer_name])
        else:
            for day in self.trainer_schedule:
                print(day.upper(), self.trainer_schedule[day])
        print('----------------------------------------------------------------------------------------------------------')

    '''
    ----------------------------------------------------------------------------
    display_dietitian_schedule function
    prints the specified day in the dietitian dictionary
    '''
    def display_dietitian_schedule(self, customer_name=None):
        print('----------------------------------------------------------------------------------------------------------')
        if customer_name:
            for day in self.dietitian_schedule:
                print(day.upper())
                if customer_name in self.dietitian_schedule[day].keys():
                    print(self.dietitian_schedule[day][customer_name])
        else:
            for day in self.dietitian_schedule:
                print(day.upper(), self.dietitian_schedule[day])
        print('----------------------------------------------------------------------------------------------------------')

    '''
    ----------------------------------------------------------------------------
    schedule_trainer function
    this function adds a time to the subdictionaries under each day for a trainer
    '''
    def schedule_trainer(self, customer_name, day, time):
        day = day.lower()
        if customer_name in self.trainer_schedule[day].keys() and day in self.trainer_schedule.keys():
            self.trainer_schedule[day][customer_name] = time
        else:
            self.trainer_schedule[day][customer_name] = time

    '''
    ----------------------------------------------------------------------------
    schedule_dietitian function
    this function adds a time to the subdictionaries under each day for a dietitian
    '''
    def schedule_dietitian(self, customer_name, day, time):
        day = day.lower()
        if customer_name in self.dietitian_schedule[day].keys():
            self.dietitian_schedule[day][customer_name] = time
        else:
            self.dietitian_schedule[day][customer_name] = time

    '''
    ----------------------------------------------------------------------------
    clear_trainer_schedule function
    this function empties the entire trainer schedule dictionary
    '''
    def clear_trainer_schedule(self):
        self.trainer_schedule.clear()

    '''
    ----------------------------------------------------------------------------
    clear_dietitian_schedule function
    this function empties the entire dietitian schedule dictionary
    '''
    def clear_dietitian_schedule(self):
        self.dietitian_schedule.clear()

    '''
    ----------------------------------------------------------------------------
    writing schedules to pickle files so that upon shutdown the dictionaries are saved and 
    can be read and reopened to retain the data from all previous sections
    '''
    def write_trainer_schedule_to_file(self, file_name):
        with open(file_name, 'wb') as handle:
            pickle.dump(self.trainer_schedule, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def read_trainer_schedule_from_file(self, file_name):
        with open(file_name, 'rb') as handle:
            self.trainer_schedule = pickle.load(handle)

    def write_dietitian_schedule_to_file(self, file_name):
        with open(file_name, 'wb') as handle:
            pickle.dump(self.dietitian_schedule, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def read_dietitian_schedule_from_file(self, file_name):
        with open(file_name, 'rb') as handle:
            self.dietitian_schedule = pickle.load(handle)

customer_schedule = CustomerSchedule()
