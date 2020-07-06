"""
Model:
	It consists of pure application logic, which interacts with the database. 
	It includes all the information to represent data to the end user.
"""

import json


class Person:
    """docstring for Person"""

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def get_all(self):
        persons = []
        with open('db.txt', 'r') as db:
            json_list = json.loads(db.read())

        for item in json_list:
            item = json.loads(item)
            person = Person(item['first_name'], item['last_name'])
            persons.append(person)

        return persons
