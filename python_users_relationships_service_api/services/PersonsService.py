from repositories.PersonsRepository import PersonsRepository

class PersonsService(object):
    def __init__(self):
        self.persons_repository = PersonsRepository()

    def add_person(self, name, age):
        return self.persons_repository.add_person(name, age)

    def get_person_by_name(self, name):
    	return self.persons_repository.get_person_by_name(name)
    
    def get_friends(self, name):
    	return self.persons_repository.get_friends(name)
    
    def get_friends_from_my_friends(self, name):
        return self.persons_repository.get_friends_from_my_friends(name)
    
    def make_friend(self, name1, name2):
        return self.persons_repository.make_friend(name1, name2)

    def delete_from_my_friends(self, name1, name2):
        return self.persons_repository.delete_from_my_friends(name1, name2)

    def get_all_persons(self):
        return self.persons_repository.get_all_persons()