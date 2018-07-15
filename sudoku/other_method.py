
def m_read_table(filename):
    
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
        values[l].append([])
#        if numbers[i]:
#            #cannot = [x for x in possible if x !=numbers[i]]
#            values[l].append(cannot)
#        else:
#            values[l].append([])
    
    return values

def m_check_square(values):
    #Create list holding all labels for sqaures
    squares = [[r+c for r in rg for c in cg] for rg in r_group for cg in c_group]
    
    #Remove finished squares from possible in other square items
    for sq in squares:
        label_values = [values[label][0] for label in sq if values[label][0]]
        for label in sq:
            if not values[label][0]:
                values[label][1].extend(x for x in label_values if x not in values[label][1]) 
                
    #Check if any values have only one possibility
    values, count = m_populate_value(values)
    
    return values, count

def m_check_row(values):
    #Create list holding all labels for rows
    rows = [[r + c for c in col] for r in row]
    
    #Remove finished squares from possible in other row items
    for r in rows:
        label_values = [values[label][0] for label in r if values[label][0]]
        for label in r:
            if not values[label][0]:
                values[label][1].extend(x for x in label_values if x not in values[label][1]) 
                
    #Check if any values have only one possibility
    values, count = m_populate_value(values)
    
    return values, count

def m_check_col(values):
    #Create list holding all labels for rows
    cols = [[r + c for r in row] for c in col]
    
    #Remove finished squares from possible in other row items
    for c in cols:
        label_values = [values[label][0] for label in c if values[label][0]]
        for label in c:
            if not values[label][0]:
                values[label][1].extend(x for x in label_values if x not in values[label][1]) 
                
    #Check if any values have only one possibility
    values, count = m_populate_value(values)
    
    return values, count

#Count tells how many squares have left to be solved
def m_populate_value(values):
    count = 81
    for key in values:
        if len(values[key][1]) == 8:
            values[key][0] = [x for x in possible if x not in values[key][1]][0]
            values[key][1] = []
        if not len(values[key][1]):
            count -= 1
    return values, count

    
def m_run(filename):
    values = m_read_table(filename)
    
    count, tries = 81, 0
    while count:
        tries += 1 
        prev_count = count
        values, count = m_check_square(values)
        values, count = m_check_row(values)
        values, count = m_check_col(values)
        if prev_count == count:
            print('Values did not change.')
            print(values)
            break
    print(tries)
    print_table(values)