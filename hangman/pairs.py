from random import randint
import itertools
import string

def pairs() :
        cities = ['MONTGOMERY', 'JUNEAU', 'PHOENIX', 'LITTLEROCK', 'SACREMENTO', 'DENVER', 'HARTFORD', 'DOVER', 'TALLAHASSEE', 'ATLANTA', 'HONOLULU', 'BOISE', 'SPRINGFIELD', 'INDIANAPOLIS', 'DESMOINES', 'TOPEKA', 'FRANKFORT', 'BATONROUGE', 'AUGUSTA', 'ANNAPOLIS', 'BOSTON', 'LANSING', 'SAINTPAUL', 'JACKSON', 'JEFFERSONCITY', 'HELENA', 'LINCOLN', 'CARSONCITY', 'CONCORD', 'TRENTON', 'SANTAFE', 'ALBANY', 'RALEIGH', 'BISMARK', 'COLUMBUS', 'OKLAHOMACITY', 'SALEM', 'HARRISBURG', 'PROVIDENCE', 'COLUMBIA', 'PIERRE', 'NASHVILLE', 'AUSTIN', 'SALTLAKECITY', 'MONTPELIER', 'RICHMOND', 'OLYMPIA', 'CHARLESTON', 'MADISON', 'CHEYENNE']
        states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'NewHampshire', 'NewJersey', 'NewMexico', 'NewYork', 'NorthCarolina', 'NorthDakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland', 'SouthCarolina', 'SouthDakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington', 'WestVirginia', 'Wisconsin' , 'Wyoming']
	pairs = dict(zip(cities, states))
        return pairs
