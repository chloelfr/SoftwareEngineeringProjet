from CustomerDatabase import customer_database

"""
The Manage report class will use two dictionaries. One is for the monthly revenue and the other is for the 
attendence by day. Annual revenue will be a float.
"""


class ManagerReport():

    def __init__(self):
        self.monthly_revenue = {
            'january': 0, 
            'february': 0, 
            'march': 0,
            'april': 0,
            'may': 0, 
            'june': 0, 
            'july': 0,
            'august': 0,
            'september': 0,
            'october': 0,
            'november': 0,
            'december': 0
        }
        self.annual_revenue = 0
        self.attendance_by_day = {
            'monday': 0,
            'tuesday': 0,
            'wednesday': 0,
            'thursday': 0,
            'friday': 0,
            'saturday': 0,
            'sunday': 0
        }

# This method add the monthly revenue to the annual revenue
    def add_monthly_revenue_to_annual_revenue(self):
        for month in self.monthly_revenue:
            self.annual_revenue += self.monthly_revenue[month]

# This method will clear the annual revenue
    def clear_annual_revenue(self):
        self.annual_revenue = 0

# This method clears the monthly revenue
    def clear_monthly_revenue(self):
        self.monthly_revenue.clear()

    def update_monthly_revenue(self):
        month = input('Month: ')
        month = month.lower()
        if month in self.monthly_revenue.keys():
            dollar_amount = input('Dollars to Add: ')
            dollar_amount = int(dollar_amount)
            self.monthly_revenue[month] += dollar_amount
        else:
            print(month, 'is not a month.')

# This method will print out the monthly report by day
    def generate_monthly_revenue_report(self):
        print('----------------------------------------------------------------------------------------------------------')
        for month in self.monthly_revenue:
            print('{0}: {1}'.format(month.upper(), self.monthly_revenue[month]))
        print('----------------------------------------------------------------------------------------------------------')

# This method will print out the annual report
    def generate_annual_revenue_report(self):
        print('----------------------------------------------------------------------------------------------------------')
        print('Annual Revenue:', self.annual_revenue)
        print('----------------------------------------------------------------------------------------------------------')

# This method updates the attendence and needs the name and attendance
    def update_attendance_by_day(self):
        for customer in customer_database.individuals:
            for day in customer_database.individuals[customer].attendance:
                self.attendance_by_day[
                    day] += customer_database.individuals[customer].attendance[day]

# This method will clear the attendence for each day
    def clear_attendance_report(self):
        self.attendence_by_day.clear()

# This method will print out the attendence report by day
    def generate_attendance_report(self):
        self.update_attendance_by_day()

        print('----------------------------------------------------------------------------------------------------------')
        for key in self.attendance_by_day:
            print('{0}: {1} customers'.format(
                key.upper(), self.attendance_by_day[key]))
        print('----------------------------------------------------------------------------------------------------------')
