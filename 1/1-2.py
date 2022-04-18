# Plan

# Load data into set

# For each X in set
# Y = 2020 - X
# If X in set
# return (print) X * Y

# log(n)

expense_data = set(open('input.txt'))

# Answer for Part I
# for x in expense_data:
#     y = 2020 - int(x)
#     if str(y) + '\n' in expense_data:
#         print(int(x) * int(y))
#         break


# Plan Part 2
# Use part 1 solution with nested for loop
# Could also try two cursors here
def findTriplet(expense_data):
    for z in expense_data:
        for x in expense_data:
            y = 2020 - int(x) - int(z)
            if str(y) + '\n' in expense_data:
                print(int(x) * int(y) * int(z))
                return

findTriplet(expense_data)
