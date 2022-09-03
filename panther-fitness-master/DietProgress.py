class DietProgress:
    def __init__(self, daily_calorie_intake=None, current_weight=None, target_weight=None):
        self.daily_calorie_intake = daily_calorie_intake
        self.current_weight = current_weight
        self.target_weight = target_weight

    '''
    ----------------------------------------------------------------------------
    display_diet_progress function
    prints the newest target weight, current weight, and daily calorie intake
    of a given object, if there is nothing for that attribute then it does not print
    '''
    def display_diet_progress(self):
        if self.daily_calorie_intake:
            print('Daily Calorie Goal:', self.daily_calorie_intake)

        if self.current_weight:
            print('Current Weight:', self.current_weight)

        if self.target_weight:
            print('Target Weight:', self.target_weight)

        if not self.daily_calorie_intake and not self.current_weight and not self.target_weight:
            print('You do not currently have any diet information.')
            print('Please schedule a dietitian if you would like to track diet information.')

    '''
    ----------------------------------------------------------------------------
    update_calorie_intake function
    changes the daily calory intake of a given object
    '''
    def update_calorie_intake(self, new_daily_calorie_intake):
        self.daily_calorie_intake = new_daily_calorie_intake

    '''
    ----------------------------------------------------------------------------
    update_current_weight function
    changes the current weight of a given object
    '''
    def update_current_weight(self, new_current_weight):
        self.current_weight = new_current_weight


    '''
    ----------------------------------------------------------------------------
    update_target_weight function
    changes the target weight of a given object
    '''
    def update_target_weight(self, new_target_weight):
        self.target_weight = new_target_weight
