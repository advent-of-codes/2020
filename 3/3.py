from functools import reduce

# Planning

# This is a graph problem.  Or maybe not?

# The graph wraps

# Start top left reach bottom right

# How many trees at 3 right 1 down???

tree_data = list(open('data.txt'))

# strip newlines

for i in range(0, len(tree_data)):
    tree_data[i] = tree_data[i].strip()


# Solution Part 1
# position = dict(x=0, y=0)
# tree_count = 0

# while (position['y'] < len(tree_data)):

#     if tree_data[position['y']][position['x']] == '#':
#         tree_count += 1

#     position['x'] += 3
#     if position['x'] >= len(tree_data[position['y']]):
#         position['x'] = position['x'] - len(tree_data[position['y']])
#     position['y'] += 1

# print(tree_count)

def test_slope(x_delta, y_delta):
    position = dict(x=0, y=0)
    tree_count = 0

    while (position['y'] < len(tree_data)):

        if tree_data[position['y']][position['x']] == '#':
            tree_count += 1

        position['x'] += x_delta
        if position['x'] >= len(tree_data[position['y']]):
            position['x'] = position['x'] - len(tree_data[position['y']])
        position['y'] += y_delta

    return tree_count

test_inputs = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
tree_results = []

for slope in test_inputs:
    tree_results.append(test_slope(slope[0], slope[1]))


print(reduce((lambda x, y: x*y), tree_results))
