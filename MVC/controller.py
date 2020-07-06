from model import Person
import view

def show_all():
	persons = Person.get_all()
	return view.show_all_view(persons)

def start():
	view.start_view()
	input_char = input()
	if input_char.lower() == 'y':
		return show_all()
	elif input_char.lower() == 'n':
		return view.end_view()
	else:
		raise Exception('Enter valid character')

if __name__ == "__main__":
	#running controller function
	start()