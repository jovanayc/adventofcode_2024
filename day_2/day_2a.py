# Jovanay Carter
# Advent of Code 
# Day 2 | Dec 2, 2024 | 1:25PM CST
# Time to complete: 28 mins

'''
The levels (rows) must either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
Figure our how many reports are safe.
'''

def level_safety(in_file):
    with open(in_file, 'r') as file:
        lines = file.readlines()
        
        total_safe = 0  # Count of safe lines

        # Convert lines to lists of integers
        int_lines = [[int(num) for num in line.split()] for line in lines]

        # Check if values are strictly decreasing by 1, 2, or 3
        for line in int_lines:
            is_decreasing = True
            for i in range(len(line) - 1):
                if not (1 <= (line[i] - line[i+1]) <= 3):
                    is_decreasing = False
                    break  # No need to check further
            if is_decreasing:
                total_safe += 1  # Line is safe if decreasing

        # Check if values are strictly increasing by 1, 2, or 3
        for line in int_lines:
            is_increasing = True
            for i in range(len(line) - 1):
                if not (1 <= (line[i+1] - line[i]) <= 3):  # Reverse the difference for increasing check
                    is_increasing = False
                    break  # No need to check further
            if is_increasing:
                total_safe += 1  # Line is safe if increasing

        print(total_safe)  # Print the total safe lines
    return total_safe



if __name__ == '__main__':
    # level_safety('levels_example.txt')  # test
    level_safety('levels.txt')  # actual