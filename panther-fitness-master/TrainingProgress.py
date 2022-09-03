from User import User
from CustomerDatabase import customer_database

class TrainingProgress():
    def __init__(self, bench_press=None, bench_press_goal=None, squat=None, squat_goal=None, mile_time=None, mile_time_goal=None, weight=None):
        self.bench_press = bench_press
        self.bench_press_goal = bench_press_goal
        self.squat = squat
        self.squat_goal = squat_goal
        self.mile_time = mile_time
        self.mile_time_goal = mile_time_goal
        self.weight = weight

    '''
    ----------------------------------------------------------------------------
    display_training_progress function
    prints out the training progress stats of a user based on their name in the
    individuals dictionary in the database file
    '''
    def display_training_progress(self):
        print('----------------------------------------------------------------------------------------------------------')
        
        if self.bench_press:
            print('Bench Press:', self.bench_press)
            print('Bench Press Goal:', self.bench_press_goal)

        if self.squat:
            print('Squat:', self.squat)
            print('Squat Goal', self.squat_goal)

        if self.mile_time:
            print('Mile Time:', self.mile_time)
            print('Mile Time Goal:', self.mile_time_goal)

        if self.weight:
            print('Current Weight', self.weight)

        print('----------------------------------------------------------------------------------------------------------')


    '''
    ----------------------------------------------------------------------------
    update_bench_press function
    takes an input to change the current bench press weight
    '''
    def update_bench_press(self, new_bench_press):
        self.bench_press = new_bench_press

    '''
    ----------------------------------------------------------------------------
    update_bench_press_goal function
    takes an input to change the current bench press goal weight
    '''
    def update_bench_press_goal(self, new_bench_press_goal):
        self.bench_press_goal = new_bench_press_goal


    '''
    ----------------------------------------------------------------------------
    update_squat function
    takes an input to change the current squat weight
    '''
    def update_squat(self, new_squat):
        self.squat = new_squat

    '''
    ----------------------------------------------------------------------------
    update_squat_goal function
    takes an input to change the current squat goal weight
    '''
    def update_squat_goal(self, new_squat_goal):
        self.squat_goal = new_squat_goal

    '''
    ----------------------------------------------------------------------------
    update_mile_time function
    takes an input to change the current mile time
    '''
    def update_mile_time(self, new_time):
        self.mile_time = new_time

    '''
    ----------------------------------------------------------------------------
    update_mile_time_goal function
    takes an input to change the current goal mile time
    '''
    def update_mile_time_goal(self, new_time_goal):
        self.mile_time_goal = new_time_goal

    '''
    ----------------------------------------------------------------------------
    update_weight function
    takes an input to change the current weight
    '''
    def update_weight(self, new_weight):
        self.weight = new_weight
