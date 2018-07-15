import collections

row = '123456789'
col = 'ABCDEFGHI'
possible = [1,2,3,4,5,6,7,8,9]
r_group = ['123', '456', '789']
c_group = ['ABC', 'DEF', 'GHI']

def read_table(filename):
    
    #Parse given file into list containing each number
    with open(filename) as f:
        numbers = f.read()
    numbers = [n.strip() for n in numbers]
    numbers = [n for n in numbers if n]
    numbers = list(map(int, numbers))
    
    if len(numbers) != 81:
        print('Input was incorrect. Please check and try again.')
        return None
    
    values = {}
    labels = [r+c for r in row for c in col]
    #Create a dict holding value in that spot and possible values
    for i, l in enumerate(labels):
        values.setdefault(l,[])
        values[l].append(numbers[i])
        
        if numbers[i]:
            values[l].append([numbers[i]])
        else:
            values[l].append(possible)
    
    return values

def check_square(values):
    #Create list holding all labels for sqaures
    squares = [[r+c for r in rg for c in cg] for rg in r_group for cg in c_group]
    
    #Remove finished squares from possible in other square items
    for sq in squares:
        label_values = [values[label][0] for label in sq if values[label][0]]
        all_can = []
        for label in sq:
            values[label][1] = [val for val in values[label][1] if val not in label_values]
            all_can  = all_can + values[label][1]
        counts = collections.Counter(all_can) 
        single = [i for i in counts if counts[i]==1]
        if len(single):
            for val in single:
                for label in sq:
                    if val in values[label][1]:
                        values[label][1] = [val]
            
    #Check if any values have only one possibility
    values, count = populate_value(values)
    
    return values, count

def check_row(values):
    #Create list holding all labels for rows
    rows = [[r + c for c in col] for r in row]
    
    #Remove finished squares from possible in other row items
    for r in rows:
        label_values = [values[label][0] for label in r if values[label][0]]
        all_can = []
        for label in r:
            values[label][1] = [val for val in values[label][1] if val not in label_values]
            all_can  = all_can + values[label][1]
        counts = collections.Counter(all_can) 
        single = [i for i in counts if counts[i]==1]
        if len(single):
            for val in single:
                for label in r:
                    if val in values[label][1]:
                        values[label][1] = [val]
    #Check if any values have only one possibility
    values, count = populate_value(values)
    
    return values, count

def check_col(values):
    #Create list holding all labels for rows
    cols = [[r + c for r in row] for c in col]
    
    #Remove finished squares from possible in other row items
    for c in cols:
        label_values = [values[label][0] for label in c if values[label][0]]
        all_can = []
        for label in c:
            values[label][1] = [val for val in values[label][1] if val not in label_values]
            all_can  = all_can + values[label][1]
        counts = collections.Counter(all_can) 
        single = [i for i in counts if counts[i]==1]
        if len(single):
            for val in single:
                for label in c:
                    if val in values[label][1]:
                        values[label][1] = [val]
    #Check if any values have only one possibility
    values, count = populate_value(values)
    
    return values, count

#Count tells how many squares have left to be solved
def populate_value(values):
    count = 81
    for key in values:
        if len(values[key][1]) == 1:
            values[key][0] = values[key][1][0]
            count -= 1
        if not len(values[key][1]):
            count -= 1
    return values, count

#Print sudoku table with values provided in the dict
def print_table(values):
    for i, r in enumerate(row):
        if i in [3, 6]:
            print('------+-------+------')
        for j, c in enumerate(col):
            if j in [3, 6]:
                print ('|', end = ' ')
            print (values[r + c][0], end = ' ')
        print()

#Passes easy checks, asks what can go in each sqaure
def run(filename):
    values = read_table(filename)
    values, count = populate_value(values)
    tries = 0
    while count:
        tries += 1
        prev_count = count
        values, count = check_square(values)
        values, count = check_row(values)
        values, count = check_col(values)
        if prev_count == count:
            print('Values did not change.')
#            print(values)
#            break
            print(tries)
            print_table(values)
            return values
    print(tries)
    print_table(values)

     