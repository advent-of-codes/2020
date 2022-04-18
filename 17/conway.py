# https://github.com/rbusquet/advent-of-code/blob/main/2020/day_17/day_17.py

import timeit

start_time = timeit.default_timer()

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)


ON = '#'
OFF = '.'

MAX_NEIGHBORS = 3
MIN_NEIGHBORS = 2

GENESIS_NEIGHBORS = 3

START_WIDTH = len(data[0])


## NOW IN 4D!!!!!!!


ON = '#'
OFF = '.'

MAX_NEIGHBORS = 3
MIN_NEIGHBORS = 2

GENESIS_NEIGHBORS = 3

class QuadrupleConway:
    def __init__(self, data):
        self.buffer = []

        self.buffer.append(set())
        self.buffer.append(set())

        self.active = 0
        self.back = 1

        self.buffer[0] = self.load_grid(data)

    def load_grid(self, data):
        # load the grid into the front buffer as strings in a set

        grid_set = set()

        z = 0
        w = 0
        # y first
        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[y][x] == ON:
                    # coords = f"{x},{y},{z},{w}"
                    # strings are slow, arrays are not hashable.  Tuples are! (Or not really)
                    # but still better solution
                    coords = (x, y, z, w)
                    grid_set.add(coords)

        return grid_set

    # takes a string cell and looks for neighbors in the set
    def count_alive_and_get_dead_neighbors(self, cell, collect_dead=True):
        x = cell[0]
        y = cell[1]
        z = cell[2]
        w = cell[3]

        count = 0
        dead_neighbors = set()

        for i in range(-1, 2, 1):
            for k in range(-1, 2, 1):
                for m in range(-1, 2, 1):
                    for p in range(-1, 2, 1):
                        if i == 0 and k == 0 and m == 0 and p == 0:
                            continue
                        else:
                            coords = (x-i, y-k, z-m, w-p)
                            if coords in self.buffer[self.active]:
                                count += 1
                            elif collect_dead:
                                dead_neighbors.add(coords)

        # print(count)

        return dead_neighbors, count

    def step_simulation(self):
        active_buffer = self.buffer[self.active]
        # back_buffer = self.buffer[self.back]

        all_dead_neighbors = set()

        # add still alive to back buffer
        for cell in active_buffer:
            dead, count = self.count_alive_and_get_dead_neighbors(cell)
            all_dead_neighbors.update(dead)

            if count >= MIN_NEIGHBORS and count <= MAX_NEIGHBORS:
                self.buffer[self.back].add(cell)
            # else it is dead now, no action needed

        # genesis
        for dead in all_dead_neighbors:
            # don't need dead neighbors here, optimize?
            dead_list, count = self.count_alive_and_get_dead_neighbors(dead, False)

            if count == GENESIS_NEIGHBORS:
                self.buffer[self.back].add(dead)

        # swap buffers at end
        if self.active == 0:
            self.active = 1
            self.back = 0
        else:
            self.active = 0
            self.back = 1

        # clear the back buffer because it doesn't get overwritten
        # like it would with an array!

        self.buffer[self.back] = set()

        # print("Active Count:", len(active_buffer))
        # print("Back Count: ", len(back_buffer))
        # print("self.back count: ", len(self.buffer[self.back]))

    def iterate_n_times_and_return_alive(self, n):

        for i in range(n):
            # print(i, len(self.buffer[self.active]))
            self.step_simulation()

            # print("Count", len(self.buffer[self.active]))

        return len(self.buffer[self.active])

instance = QuadrupleConway(data)
# dead, count = instance.count_alive_and_get_dead_neighbors('2,1,0')

# print(dead, count)

print("Result", instance.iterate_n_times_and_return_alive(20))
print(timeit.default_timer() - start_time)




# Part 1 Solution

## Conway in 3d!!!! :D

# set up 3d double_buffer

# Ah, interesting, it's an infinite pocket dimension

# half tempted to write a new array class here that can handle negative indices
# or just offset

# picking back up after six months!

# New approach, virtual grid:

# create a set that has "X,Y,Z" coordinates
# Active if in set
# buffer set too

# it doesn't matter what order we go in processing the rules
# because it all goes to the back buffer

# Check neighbors derives "X,Y,Z" coords in  set

# ON = '#'
# OFF = '.'

# MAX_NEIGHBORS = 3
# MIN_NEIGHBORS = 2

# GENESIS_NEIGHBORS = 3

# class TripleConway:
#     def __init__(self, data):
#         self.buffer = []

#         self.buffer.append(set())
#         self.buffer.append(set())

#         self.active = 0
#         self.back = 1

#         self.buffer[0] = self.load_grid(data)
#         # print(self.buffer[0])

#     def load_grid(self, data):
#         # load the grid into the front buffer as strings in a set

#         grid_set = set()

#         z = 0
#         # y first
#         for y in range(len(data)):
#             for x in range(len(data[0])):
#                 if data[y][x] == ON:
#                     coords = f"{x},{y},{z}"
#                     grid_set.add(coords)


#         return grid_set

#     # takes a string cell and looks for neighbors in the set
#     def count_alive_and_get_dead_neighbors(self, cell):
#         coords = cell.split(',')
#         x = int(coords[0])
#         y = int(coords[1])
#         z = int(coords[2])

#         count = 0
#         dead_neighbors = set()

#         for i in range(-1, 2, 1):
#             for k in range(-1, 2, 1):
#                 for m in range(-1, 2, 1):
#                     if i == 0 and k == 0 and m == 0:
#                         continue
#                     else:
#                         coords = f"{x-i},{y-k},{z-m}"
#                         if coords in self.buffer[self.active]:
#                             count += 1
#                         else:
#                             dead_neighbors.add(coords)

#         # print(count)

#         return dead_neighbors, count

#     def step_simulation(self):
#         active_buffer = self.buffer[self.active]
#         # back_buffer = self.buffer[self.back]

#         # print("Active: ", self.active)
#         # print("Back: ", self.back)

#         # this handles killing active
#         # but what about genesis?
#         all_dead_neighbors = set()

#         for cell in active_buffer:
#             dead, count = self.count_alive_and_get_dead_neighbors(cell)
#             all_dead_neighbors.update(dead)

#             if count >= MIN_NEIGHBORS and count <= MAX_NEIGHBORS:
#                 self.buffer[self.back].add(cell)
#             # else it is dead now, no action needed

#         # genesis
#         for dead in all_dead_neighbors:
#             # don't need dead neighbors here, optimize?
#             dead_list, count = self.count_alive_and_get_dead_neighbors(dead)

#             if count == GENESIS_NEIGHBORS:
#                 self.buffer[self.back].add(dead)

#         # swap buffers at end
#         if self.active == 0:
#             self.active = 1
#             self.back = 0
#         else:
#             self.active = 0
#             self.back = 1

#         # clear the back buffer because it doesn't get overwritten
#         # like it would with an array!

#         self.buffer[self.back] = set()

#         # print("Active Count:", len(active_buffer))
#         # print("Back Count: ", len(back_buffer))
#         # print("self.back count: ", len(self.buffer[self.back]))

#     def iterate_n_times_and_return_alive(self, n):

#         for i in range(n):
#             # print(i, len(self.buffer[self.active]))
#             self.step_simulation()

#             print("Count", len(self.buffer[self.active]))

#         return len(self.buffer[self.active])

# instance = TripleConway(data)
# # dead, count = instance.count_alive_and_get_dead_neighbors('2,1,0')

# # print(dead, count)

# print("Result", instance.iterate_n_times_and_return_alive(6))


# Old work

# class Grid:

#     def __init__(self, data, size):
#         row = ['.']
#         grid = [[[]]]
#         # offset to put things in the middle
#         z = 0
#         # y first
#         for y in range(len(data)):
#             for x in range(len(data[0])):
#                 if data[y][x] == '#':
#                     coords = f"{x},{y},{z}"
#                     grid.add(coords)

# class TripleConway:
#     def __init__(self, data):
#         self.buffer = []

#         self.buffer[0] = Grid(data, len(data[0] * 2))
#         self.buffer[1] = Grid(data, len(data[0] * 2))

#         self.active = 0
#         self.back = 1

#     def count_neighbors(self, cell):
#         coords = cell.split(',')
#         x = int(coords[0])
#         y = int(coords[1])
#         z = int(coords[2])

#         count = 0

#         for i in range(-1, 2, 1):
#             for k in range(-1, 2, 1):
#                 for m in range(-1, 2, 1):
#                     if i == 0 and k == 0 and m == 0:
#                         continue
#                     else:
#                         coords = f"{i},{k},{m}"
#                         if coords in self.buffer[self.active]:
#                             count += 1

#         return count


#     def cycle(self):
#         for cell in self.buffer[self.active]:
#             # do stuff

#             pass

#         if self.buffer == 0:
#             self.buffer = 1
#         else:
#             self.buffer = 0










# Try old-fashioned array method, just make enough space for 6 iterations

# This is much slower!!!

# class QuadConwayArray:
#     def __init__(self, data, iterations):

#         # hardcode 4d

#         four_d_matrix = [[[[]]]]

#         size = START_WIDTH + (iterations * 2) + 2 # probably don't need extra

#         self.buffer = []

#         self.buffer.append([[[ ['.'] * size for i in range(size)] for k in range(size)] for m in range(size)])
#         self.buffer.append([[[ ['.'] * size for i in range(size)] for k in range(size)] for m in range(size)])

#         # print(self.buffer[0])

#         middle = int(size / 2)

#         write_start = middle - int(START_WIDTH / 2)

#         self.active = 0
#         self.back = 1

#         self.load_grid(data, write_start)
#         # print(self.buffer[0])

#     def load_grid(self, data, write_start):
#         debug_count = 0
#         z = 0
#         w = 0
#         # y first
#         for y in range(len(data)):
#             for x in range(len(data[0])):
#                 if data[y][x] == ON:
#                     debug_count += 1
#                     # REVERSING HERE to deal with expected xyzw
#                     # offset to put in the middle
#                     self.buffer[self.active][x + write_start][y + write_start][z + write_start][w + write_start] = ON


#         print("Starting count: ", debug_count)


#     # takes a string cell and looks for neighbors in the grid
#     def count_neighbors(self, cell):
#         x = cell[0]
#         y = cell[1]
#         z = cell[2]
#         w = cell[3]

#         # print("Coords: ", x, y, z, w)

#         count = 0
#         limit = len(self.buffer[self.active])

#         for i in range(-1, 2, 1):
#             for k in range(-1, 2, 1):
#                 for m in range(-1, 2, 1):
#                     for p in range(-1, 2, 1):
#                         if i == 0 and k == 0 and m == 0 and p == 0:
#                             continue
#                         elif x-i < 0 or y-k < 0 or z-m < 0 or w-p < 0:
#                             continue
#                         elif x-i >= limit or y-k >= limit or z-m >= limit or w-p >= limit:
#                             continue
#                         else:
#                             coords = (x-i, y-k, z-m, w-p)
#                             if self.buffer[self.active][x-i][y-k][z-m][w-p] == ON:
#                                 count += 1

#         # print(count)

#         return count

#     def step_simulation(self):
#         print("Active: ", self.active)
#         active_buffer = self.buffer[self.active]
#         # back_buffer = self.buffer[self.back]

#         count_this_step = 0

#         # add still alive to back buffer
#         for i in range(len(active_buffer)):
#             for k in range(len(active_buffer)):
#                 for m in range(len(active_buffer)):
#                     for p in range(len(active_buffer)):
#                         count = self.count_neighbors((i, k, m, p))

#                         if active_buffer[i][k][m][p] == ON:
#                             if count >= MIN_NEIGHBORS and count <= MAX_NEIGHBORS:
#                                 self.buffer[self.back][i][k][m][p] = ON
#                                 count_this_step += 1
#                             else:
#                                 self.buffer[self.back][i][k][m][p] = OFF
#                         else: # == OFF
#                             if count == GENESIS_NEIGHBORS:
#                                 self.buffer[self.back][i][k][m][p] = ON
#                                 count_this_step += 1


#         # swap buffers at end
#         if self.active == 0:
#             self.active = 1
#             self.back = 0
#         else:
#             self.active = 0
#             self.back = 1

#         return count_this_step

#     def iterate_n_times_and_return_alive(self, n):

#         final_count = 0

#         for i in range(n):
#             # print(i, len(self.buffer[self.active]))
#             final_count = self.step_simulation()

#             print("Count", final_count)

#         return final_count


# instance2 = QuadConwayArray(data, 6)
# instance2.iterate_n_times_and_return_alive(6)
