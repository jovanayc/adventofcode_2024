# Jovanay Carter
# Advent of Code 
# Day 1 | Dec 1, 2024 | 11:44AM CST
# Time to complete: 95 mins

'''Figure out exactly how often each number from the left list 
appears in the right list. Calculate a total similarity score 
by adding up each number in the left list after multiplying it 
by the number of times that number appears in the right list.
'''

def sum_of_similarities(in_file):
    list_a = []
    list_b = []
    dict_b = {}
    similarities_sum = 0
    
    '''Open file and split lists into two'''
    with open(in_file, 'r') as file1:
        # read info into a list
        lines = file1.readlines()
    
    for line in lines:
        a, b = line.split()
        list_a.append(a)
        list_b.append(b)
        
    '''create dict of values in list B'''
    for value in list_b:
        if value in dict_b:
            dict_b[value] += 1 # add 1 to value
        else:
            dict_b[value] = 1 # else create new value

    '''calculate sum by looking for values in list A within dict B'''
    for value in list_a:
        if value in dict_b.keys():
            similarities_sum += (int(value) * dict_b[value])
    print(similarities_sum)
    return similarities_sum

if __name__ == '__main__':
    file = 'location_ids.txt'
    # file = 'lst_example.txt'
    solution = sum_of_similarities(file)