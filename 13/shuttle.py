with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# new data format!
# Part II

# discard x's for now, probably part 2

busses = data[1].split(',')

# 7,13,x,x,59,x,31,19

# Dataset is still small, brute forcing it
# Brute force is still too slow.  Not really surprised

# unsure of how to proceed, running down options

# use a cache???

# not sure how to cache this usefully and would run out of memory

# work backwards?

# generate solution sets and check for validity?

# racing to see if I can come up with a new plan before the slow way finds it

# build giant sets of departure times for super fast lookup?

# lets try that

# nope, should have thought this through.
# pretty sure it's taking longer to build the dict
# at least try limiting the dict

# def build_departure_reference(size, start):
#     reference = dict()
#     for i in range(len(busses)):
#         if busses[i] == 'x':
#             continue
#         reference[busses[i]] = set()
#         for k in range(start, size):
#             reference[busses[i]].add(int(busses[i]) * k)

#     return reference


# reference = build_departure_reference(200000000000000, 100000000000000)


# def find_moment_two(start):
#     while True:

#         found_solution = False
#         for i in range(len(busses)):
#             # print(i)
#             if busses[i] == 'x':
#                 continue
#             timestamp = start + i
#             if timestamp not in reference[busses[i]]:
#                 break
#             else:
#                 # there should be a bettere way than calling this
#                 # each time
#                 if i == len(busses) - 1:
#                     found_solution = True

#         if found_solution:
#             return start
#         start += 1


# print(find_moment_two(1000000))

# Brute force method below, too slow

# must need to cache it

# or iterate more cleverly.

# Can increase start by largest, minus it's position?


# No, but once I find each one, it will put me on a cadence
# for that one
# can skip by the biggest

# still way too slow.  Still same complexity just better

# 100,000,000,000,000

# the solution has to be bottom up

# none of the math stuff will work because of the offset
# offsets seem random

# maybe a different approach with modulo
# number where modulo of that number = the offset?

# not repeating work, so nothing to cache

# some kind of divide and conquer?  nothing to divide

# or bottom up.

# sort of like superposition  of several frequencies

# except with an offset


# Chinese remainder theorem!!!!????






def check_magic_moment(start, iterator):
    for i in range(len(busses)):
        # print(i)
        # breakpoint()
        # if i > 0:
        #     breakpoint()
        if busses[i] == 'x':
            continue

        remainder = (i + start) % int(busses[i])
        if remainder != 0:
            return False, iterator
        else:
            if int(busses[i]) > iterator:
                iterator = int(busses[i])
                print(iterator)

    return start, iterator


def find_magic_moment(start, offset):
    iterator = 1
    while True:
        # print(start)
        result, iterator = check_magic_moment(start, iterator)
        if result:
            return result
        else:
            start += iterator



def filter_x(value):
    if value == 'x':
        return False
    return True

buss_nums = data[1].split(',')
buss_nums = filter(filter_x, busses)

buss_nums = [int(num) for num in buss_nums]

largest = max(buss_nums)
print(largest)

offset = largest - busses.index(str(largest))
start = 100000000000000
# start = 0
print(find_magic_moment(start, offset))

## Part 1
# earliest_departure = int(data[0])

# # discard x's for now, probably part 2

# def filter_x(value):
#     if value == 'x':
#         return False
#     return True

# busses = data[1].split(',')
# busses = filter(filter_x, busses)

# busses = [int(num) for num in busses]

# print(busses)


# # all busses started at time 0
# # ID number is roundtrip time, the go constantly
# # Dataset is small, brute forcing it

# departure_times = []
# closest_time = float('inf')
# closest_bus = None
# for i in range(0, len(busses)):
#     time = 0
#     while time < earliest_departure:
#         time += busses[i]

#     departure_times.append(time)
#     if closest_time > time:
#         closest_time = time
#         closest_bus = busses[i]

# print(closest_bus * (closest_time - earliest_departure))
