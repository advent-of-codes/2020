with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

def setup_buffer(data):
    # modify the data to add a ring of floor all around to make conway rules
    # simpler
    # add the top and bottom, minus the corners
    data.insert(0, 'x' * len(data[0]))
    data.append('x' * len(data[0]))

    # add  the left and right, including the corners
    # Update: and split here, since can't assign by index to string
    for y in range(len(data)):
        data[y] = list('x' + data[y] + 'x')

    buffer = []

    # append twice for double buffer
    buffer.append(data)
    # buffer.append(data)  pass by reference, dummy!

    setup = []

    for _ in range(len(data)):
        # split the buffer too
        setup.append(list('x' * len(data[0])))

    buffer.append(setup)

    return buffer

# Print helper

def print_seating(data):
    for row in data:
        print(''.join(row).strip('x'))

def count_occupied(data):
    count = 0
    for row in data:
        for char in row:
            if char == '#':
                count += 1

    return count

def seatway(data):
    buffer = setup_buffer(data)
    # print_seating(buffer[0])

    current = 0
    back = 1

    iterations = 0

    while (True):
        iterations += 1
        print(iterations)
        # print_seating(buffer[0])
        for y in range(1, len(buffer[0])-1):
            for x in range(1, len(buffer[0][0])-1):
                # do the rules
                position = buffer[current][y][x]
                # floor stays floor
                if position == '.':
                    # breakpoint()
                    buffer[back][y][x] = '.'

                # otherwise, look, NSEW --AND DIAGONAL-- and count
                neighbors = 0

                # since we added the border, and limited our loops, can ignore edges
                for i in range(-1, 2, 1):
                    # print(i)
                    for k in range(-1, 2, 1):
                        if buffer[current][y + i][x + k] == '#':
                            # don't count self
                            if i == 0 and k == 0:
                                continue
                            else:
                                neighbors += 1

                # print(f'neighbors: {neighbors}')

                # breakpoint()
                # adjust depending on rules and neighbors
                if position == 'L':
                    if neighbors == 0:
                        buffer[back][y][x] = '#'
                    else:
                        buffer[back][y][x] = 'L'

                if position == '#':
                    # breakpoint()
                    if neighbors >= 4:
                        # print("more than 3")
                        buffer[back][y][x] = 'L'
                    else:
                        # print("less than 4")
                        buffer[back][y][x] = '#'


        # check for stability and exit if buffer 0 == buffer 1
        if buffer[0] == buffer[1]:
            # calculate occupied
            return buffer[0]

        # flip active buffer
        if current == 0:
            current = 1
            back = 0
        else:
            current = 0
            back = 1

        # print_seating(buffer[current])
        # print_seating(buffer[back])
        # breakpoint()
    # try once before adding while(true) around above
    # return buffer[1]

stable = seatway(data)

print_seating(stable)

print(count_occupied(stable))

#  Conway!!!!!

# double buffer
# remember y, x
