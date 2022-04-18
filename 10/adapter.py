with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

# go ahead and turn it into number for this one

adapters = [int(num) for num in data]

# Also added this very late:
# Add 0 to the list to represent the plug
# do it before sorting to avoid o(n) insert
adapters.append(0)

# go ahead and sort them

adapters = sorted(adapters)


# Well this is a complicated description

# Device joltage is max in data

device_jolts = max(adapters) + 3

# Note: I added this after writing 70 lines of code and comments
# Add the device to be counted
adapters.append(device_jolts)

# print(device_jolts)

# adapters can connect 1-3 lowere

# find a chain that uses all devices

# is that just sorted?  Why wouldn't it be?

# example is just sorted

# find numbere of 1 difference and 3 difference

difference_list = []

ones = 0
threes = 0
for i in range(1, len(adapters)):
    # just do it the easy way
    dif = adapters[i] - adapters[i - 1]
    if dif == 1:
        ones += 1
    if dif == 3:
        threes += 1
    difference_list.append(dif)


# not working, maybe need to include device and seat?



print(difference_list)
print(ones)
print(threes)
print(ones * threes)

# print(len([num == 1 for num in difference_list]) * len([num == 3 for num in difference_list]))

# would be easier to just do a for loop but trying to learn fancy python tricks

# ones = filter(lambda num: num == 1, difference_list)

# def find_ones(num):
#     if num == 1:
#         return True
#     else:
#         return False

# ones = filter(filter_difference, (difference_list, dif))

# print(ones)
# print(len(difference_list))



# ______________________PART 2___________________________

# This one is definitely combinations and/or permutations
# "more than a trillion" .... yup

# knapsack?
# or another tree problem?  Can probably do trees with cacheing
# probably not knapsack, the order matters
# graph problem?  Count valid paths?  Would need to cache still

# find graph connections in place
# def find_connections(adapter_index, adapters):
#     connections = []  # no point in set, traversing all

#     i = adapter_index + 1
#     while (True):
#         # print(f'i: {i}  ,  adapter_i: {adapter_index}')
#         if i == len(adapters):
#             return connections
#         diff = adapters[i] - adapters[adapter_index]
#         if diff <= 3:
#             connections.append(i)
#             i += 1
#         else:
#             return connections

# print(find_connections(7, adapters))

# brute force is just to traverse the tree and count
# might as well try it
# assuming no bugs, this is taking forever
# with test data, there are bugs


# already worried about time finding graph in place
# if I need to lookup the index of values, will take even longer

# instead just build the adjacency list.  Graph is small anyway


# however, brute force still takes forever

# going to need to use a cache for sure



graph = dict()

for i in range(0, len(adapters)):
    graph[adapters[i]] = []

    k = i + 1

    while k < len(adapters):
        diff = adapters[k] - adapters[i]
        if diff <= 3:
            graph[adapters[i]].append(adapters[k])
            k += 1
        else:
            break

# print(graph)
# breakpoint()

valid_paths = 0

stack = []
stack.append(adapters[0])

print(adapters)

# total number of paths from this number
cache = dict()

# numbers whose paths are complete
completed = set()

# do I need to put this in a tree instead?
# bigger and redundant data set.
# but I can cache and cull whole branches
# or is that not really any different than what I have now?

# depth first will allow me to fill in the cache from the leaves back

# but needs to be recursive or I'd have to use a cursor

def recursive_traversal(total, current, cache, graph):
    if current in cache:
        # print("found cached")
        return total + cache[current]
    # print("iteration")
    # if graph[current] == []:
    #     return total

    amount = total
    # print(current)
    if current == device_jolts:
        # breakpoint()
        amount += 1

    for child in graph[current]:
        amount += recursive_traversal(total, child, cache, graph)

    cache[current] = amount
    return amount

print("##############################")
print(recursive_traversal(0, 0, dict(), graph))

# while len(stack) > 0:
#     current = stack.pop()
#     print(current)
#     # breakpoint()
#     if current == device_jolts:
#         valid_paths += 1

#     # I'm passing the current value to a function that expects
#     # index.  Rewriting that
#     # stack = stack + find_connections(current, adapters)

#     stack += graph[current]

# print(valid_paths)
