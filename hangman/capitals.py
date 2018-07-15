from random import randint
import string

def capitals() :
	cities = ['Montgomery', 'Juneau', 'Phoenix', 'LittleRock', 'Sacramento', 'Denver', 'Hartford', 'Dover', 'Tallahassee', 'Atlanta', 'Honolulu', 'Boise', 'Springfield', 'Indianapolis', 'DesMoines', 'Topeka', 'Frankfort', 'BatonRouge', 'Augusta', 'Annapolis', 'Boston', 'Lansing', 'SaintPaul', 'Jackson', 'JeffersonCity', 'Helena', 'Lincoln', 'CarsonCity', 'Concord', 'Trenton', 'SantaFe', 'Albany', 'Raleigh', 'Bismark', 'Columbus', 'OklahomaCity', 'Salem', 'Harrisburg', 'Providence', 'Columbia', 'Pierre', 'Nashville', 'Austin', 'SaltLakeCity', 'Montpelier', 'Richmond', 'Olympia', 'Charleston', 'Madison', 'Cheyenne']
	
	x = randint(0,50)
	for i in range(0,50) :
		cities[i] = cities[i].upper()
	return cities[x]

