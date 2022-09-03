from Database import Database


class EmployeeDatabase(Database):

    def __init__(self):
        '''
        calling the database class to access the database dictionary
        for the employee database
        '''
        Database.__init__(self)

    '''
    ----------------------------------------------------------------------------
    add_user function
    calls the individuals dictionary from the database class to add a new employee
    by name
    '''
    def add_user(self, name, employee):
        self.individuals[name] = employee

    '''
    ----------------------------------------------------------------------------
    remove_user function
    calls the individuals dictionary from the database class to remove a current employee
    '''
    def remove_user(self, name):
        if name in self.individuals.keys():
            del self.individuals[name]
            print('Employee Successfully Removed.')
        else:
            print('\nEmployee Not in Database\n')

    '''
    ----------------------------------------------------------------------------
    display_users function
    calls the individuals array from the database class to print the current
    employees present in the dictionary
    '''
    def display_users(self):
        for key in self.individuals:
            print('{0}: {1}'.format(key.upper(),
                                    self.individuals[key].account_type.upper()))


employee_database = EmployeeDatabase()
