from User import User

#This MembershipPackage class is set to hold the current package, the package price and the package description
class MembershipPackage:
    def __init__(self, current_package):
        self.current_package = current_package
        self.package_price = self.determine_package_price()
        self.package_description = self.determine_package_description()

#This method is used to determine the price of a package and add it to the collection
    def determine_package_price(self):
        if self.current_package == 'bronze':
            return 10
        elif self.current_package == 'silver':
            return 20
        elif self.current_package == 'gold':
            return 30
#This method is used to determine the description of a package and add it to the collection
    def determine_package_description(self):
        if self.current_package == 'bronze':
            return 'Cardio, Weights & Machines, Locker Rooms with Showers'
        elif self.current_package == 'silver':
            return 'Cardio, Weights & Machines, Locker Rooms with Showers, Schedule a Trainer Once a Week'
        elif self.current_package == 'gold':
            return 'Cardio, Weights & Machines, Locker Rooms with Showers, Schedule a Trainer Once a Week, Schedule a Dietitian Once a Week'

#This method is used to update the price and the description of a package
    def update_package_details(self):
        self.package_price = self.determine_package_price()
        self.package_description = self.determine_package_description()

#This method is used to display the package information of a customer
    def display_my_package_info(self):
        print('----------------------------------------------------------------------------------------------------------')
        print('Current Package Level: {0}\nCost Per Month: {1}\nPackage Description: {2}'.format(self.current_package.upper(), self.package_price, self.package_description))
        print('----------------------------------------------------------------------------------------------------------')

#This method is used to display all the available packages
    def display_package_levels(self):
        print('Bronze: INCLUDES Cardio, Weights & Machines, Locker Rooms with Showers')
        print('Silver: INCLUDES Cardio, Weights & Machines, Locker Rooms with Showers, Schedule a Trainer Once a Week')
        print('Gold: INCLUDES Cardio, Weights & Machines, Locker Rooms with Showers, Schedule a Trainer Once a Week, Schedule a Dietitian Once a Week')

#This method is used to change the membership package of the customer
    def change_membership_package(self):
        new_package = input('New Package: ')
        new_package = new_package.lower()
        self.current_package = new_package
        self.update_package_details()
