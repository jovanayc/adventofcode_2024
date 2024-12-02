# Jovanay Carter
# Advent of Code 
# Day 1 | Dec 1, 2024 | 10:05PM CST
# Time to complete: 55 mins

'''
Find the total distance between the left list and the right list
Add up the distances between all of the pairs you found. 

Your actual left and right lists contain many location IDs. 
What is the total distance between your lists?
'''
    
def compute_diff(in_file):
    ''' PART 1:
    opens file and saves to two lists
    RETURN lista, listb as a tuple
    '''
    with open(in_file, 'r') as file1:
        # read info into a list
        lines = file1.readlines()
    
    list_a = []
    list_b = []
    
    for line in lines:
        a, b = line.split()
        list_a.append(a)
        list_b.append(b)
    
    
    ''' PART 2:
    sorts both lists, loops through to sum differences
    RETURNS sum as int
    '''
    list_a.sort()
    list_b.sort()
    sum = 0
    
    for item_a, item_b in zip(list_a, list_b):
        # get abs value differences and add to sum total
        diff = abs(int(item_a) - int(item_b))
        sum += diff
        
    sum = int(sum)
    sum_formatted = "{:,}".format(sum)
    print(sum_formatted) # formatted for readability
    
    return sum


if __name__ == '__main__':
    file = 'location_ids.txt'
    solution = compute_diff(file)