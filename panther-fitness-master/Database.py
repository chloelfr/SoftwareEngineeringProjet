import pickle
from pprint import pprint
from abc import abstractmethod


class Database:

    def __init__(self):
        self.individuals = {}

    @abstractmethod
    def add_user(self):
        pass

    @abstractmethod
    def remove_user(self):
        pass

    '''
    ----------------------------------------------------------------------------
    writing schedules to pickle files so that upon shutdown the dictionaries are saved and 
    can be read and reopened to retain the data from all previous sections
    '''
    def write_to_file(self, file_name):
    	with open(file_name, 'wb') as handle:
    		pickle.dump(self.individuals, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def read_from_file(self, file_name):
    	with open(file_name, 'rb') as handle:
    		self.individuals = pickle.load(handle)
