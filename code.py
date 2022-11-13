#Hash code 

"""we start by defining the architecture of the problem with services, features, binaries""" 

class Binary:
    def __init__(self, id) -> None:
        """It define a list of services, engineers and an id.
        """
        self.services = []
        self.engineers = []
        self.id = id
        
    def add_engineer(self, engineer) -> None:  # pragma: no cover
        """adding engineers whome working on binary
        """
        self.engineers.append(engineer)
    
    def remove_engineer(self, engineer) -> None:  # pragma: no cover   
        self.engineers.remove(engineer)
        
    def add_service(self, service) -> None:  # pragma: no cover
        self.services.append(service)
    
    def remove_service(self, service) -> None:  # pragma: no cover
        self.services.remove(service)
    
    def get_n_services(self) -> int:  # pragma: no cover
        """ number of services
        """
        return len(self.services)

    def get_n_engineers(self) -> int:  # pragma: no cover
        """It returns the number of engineers
        """
        return len(self.engineers)   

class Feature:
    def __init__(self, services: list, users: int, difficulty: int, name: str) -> None:
        """foo feature is implemented in 3 services, its difficulty is 3
and 100 users per day will benefit from it

        inputs: list of services, number of users per day will benefit from it and its difficulty.
        """
        self.name = name
        self.services = services
        for s in services:
            self.add_service(s)

        self.users = users
        self.difficulty = difficulty
    
    def add_service(self, service) -> None:  
        """It adds the features to the respective services where they are running 
        Return: updated list of services
        """
        self.services.append(service)
        service.add_feature(self)
    def remove_service(self, service) -> None: 
        self.services.remove(service)
    def is_launched(self) -> bool :
        """Return (Boolean): features already launched
        """
        return len(self.services) == 0

class Service:
    def __init__(self, name, binary: Binary) -> None:
        """It define a list of features.
        """
        self.name = name
        self.binary = binary
        self.binary.add_service(self)
        self.features = []
    
    def add_feature(self, feature) -> None:
        """It adds to features list a feature relied on a service
        Return: updated list of features
        """
        self.features.append(feature)
        
   class Task:
    def __init__(self, type):
        self.type = type

class Engineer:
    def __init__(self, id) -> None:
        """It define a list of tasks, the id, the current task and the availability of an engineer.
        Args:
        self represents the instance of the class
        id
        """
        self.id = id
        self.tasks = []
        self.current_task = None
        self.is_available = True 

"""An engineer can choose any binary Bj and implement a feature Fi in all relevant services in that binary at once.
If an engineer works on a binary Bj to implement a feature Fi this work will require
DFi + RBj + CBj days, where:
"""

class ImplementFeature(Task):
    def __init__(self, feature: Feature, binary: Binary, engineer: Engineer) -> None:
        """It recalls the feature, binary, engineer classes.
        """
        self.feature = feature
        self.binary = binary
        self.engineer = engineer
        self.total_days = self.compute_difficulty()
        self.remaining_days = self.total_days
        self.engineer.is_available = False
        self.binary.engineers.append(engineer)
        self.engineer.tasks.append(self)
        self.engineer.current_task = self
    
    def compute_difficulty(self) -> int:
        """It  returns the result obtained by the calculation of difficulty to implement a feature
        """
        return self.feature.difficulty + len(self.binary.services) + len(self.binary.engineers)
    
class Wait(Task):    
    def __init__(self, days: int, engineer: Engineer) -> None:
        """It updates the remaining working days and the total days.
        """
        self.engineer = engineer
        
        self.engineer.is_available = False

        self.total_days = days
        self.remaining_days = self.total_days

        self.engineer.tasks.append(self)
        self.engineer.current_task = self



