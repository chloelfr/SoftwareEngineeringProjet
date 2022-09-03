from Database import Database


class CustomerDatabase(Database):

    def __init__(self):
        '''
        calling the database class to access the database dictionary
        for the customer database
        '''
        Database.__init__(self)

    '''
    ----------------------------------------------------------------------------
    add_user function
    calls the individuals dictionary from the database class to add a new customer
    '''
    def add_user(self, name, customer):
        self.individuals[name] = customer

    '''
    ----------------------------------------------------------------------------
    remove_user function
    calls the individuals dictionary from the database class to remove a current customer
    '''
    def remove_user(self, name):
        if name in self.individuals.keys():
            del self.individuals[name]
            print('Customer Successfully Removed.')
        else:
            print('Customer Not in Database')

    '''
    ----------------------------------------------------------------------------
    display_users function
    calls the individuals array from the database class to print the current
    customers present in the dictionary
    '''
    def display_users(self):
        for key in self.individuals:
            print(key.upper())


customer_database = CustomerDatabase()
