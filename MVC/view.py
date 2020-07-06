"""
View:
	View represents the HTML files, which interact with the end user. 
	It represents the model’s data to user.
	View never interacts with model; controller does this work (communicating with model and view).
"""

from model import Person

def show_all_view(persons):
	print(f'In our db we have {len(persons)} users. Here they are:')
	for person in persons:
		print(person)

def start_view():
	print ('MVC - the simplest example')
	print ('Do you want to see everyone in my db?[y/N]')

def end_view():
	print ('Goodbye!')