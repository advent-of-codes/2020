# should be using with...
with open('data.txt', 'r') as file:
    boarding_data = file.read().split('\n')

# cut trailing newline
boarding_data.pop(-1)

# 128 rows on plane
# First 7 are FB

# 8 columns of seats - widebody!
# last 3

# seat ID = row by 8 then add column

index_of_highest = 0

ROWS = 127 # I guess the airline does know about 0 index!
COLUMNS = 7

def find_position(seat):
    row_position = [0, ROWS]

    for i in range(0, 7):
        if seat[i] == 'F':
            row_position[1] -= ((row_position[1] - row_position[0] + 1) // 2)
        else:
            # assuming no bad data, could be wrong
            # need to add 1 like in a heap
            # or not, off by 1 errors are fun...
            # resorted to throwing spaghetti at the wall
            # no idea why -1 -1, should analyze later
            row_position[0] += ((row_position[1] - row_position[0] + 1) // 2)
    # they should be the same now

    column_position = [0, COLUMNS]
    # copying and pasting is bad, but i did it anyways /shruggles
    for i in range(7, 7 + 3):  # I hate magic numbers
        if seat[i] == 'L':
            column_position[1] -= ((column_position[1] - column_position[0] + 1) // 2)
        else:
            column_position[0] += ((column_position[1] - column_position[0] + 1) // 2)
    # they should be the same now
    return [row_position[0], column_position[0]]



def get_id_from_position(position):
    return position[0] * 8 + position[1]

# Part 1 solution
# highest_id = 0

# for ticket in boarding_data:
#     position = find_position(ticket)
#     candidate = get_id_from_position(position)
#     if candidate > highest_id:
#         highest_id = candidate

# print(highest_id)

# I'm not sure filling the plane will work because of below
# but trying first:

# It's a completely full flight, so your seat should be the only missing
# boarding pass in your list. However, there's a catch: some of the seats at the
# very front and back of the plane don't exist on this aircraft, so they'll be
# missing from your list as well.

# Your seat wasn't at the very front or back, though; the seats with IDs +1 and
# -1 from yours will be in your list.

airplane = []

for i in range(0, ROWS + 1):
    airplane.append([])
    for k in range(0, COLUMNS + 1):
        airplane[i].append(0)

# print(len(airplane))
# print(len(airplane[0]))

for ticket in boarding_data:
    position = find_position(ticket)
    # print(position[0])
    # print(position[1])
    airplane[position[0]][position[1]] = 1

# print(airplane)


# So can see missing rows on both ends and a partial missing on one end.
# Can also see  what is probably my seat in the middle

# Probably supposed to do something with ID nums, but feeling lazy
# and have a better ideea

# Find lonely 0
def find_lonely_zero(airplane):
    lonely_seat = [None, None]
    for row in range(0, ROWS + 1):
        # Don't feel like looking up Python magic
        num_empty = 0
        for column in range(0, COLUMNS + 1):
            if airplane[row][column] == 0:
                lonely_seat = [row, column]
                num_empty += 1

        if num_empty == 1:
            return lonely_seat

my_seat = find_lonely_zero(airplane)
print(get_id_from_position(my_seat))
