#The services class will be used to hold all possible services
class Services:
    def __init__(self):
        self.services_list = []

#This method is used to add a service to the collection
    def add_service(self, service):
        self.services_list.append(service)

#This method is used to remove a service from the collection
    def remove_service(self, service):
        self.services_list.remove(service)

#This method will display all availiable services
    def display_my_services(self):
        for service in self.services_list:
            print(service.upper())
