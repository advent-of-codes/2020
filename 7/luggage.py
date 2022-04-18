# should be using with...
with open('data.txt', 'r') as file:
    luggage_rules_data = file.read().split('\n')

# cut trailing newline
luggage_rules_data.pop(-1)


# need to parse the rules into a logical data structure

# all bags have adjective, then color

# Some cleanup needed

# rule format is bag, word "contains", either comma separated
# or "contain no other bags"

# dictionary with list of bags contained:

# or dict of dicts, because we have quantities

# sample = {
#     "light red": {
#         "bright white": 1,
#         "muted yellow": 2
#     }
# }

# do this then use to figure out permutations.  or is it combinations?

rules_dict = dict()

for rule in luggage_rules_data:
    new_rule = dict()
    rule = rule.strip('.')
    # breakpoint()
    split = rule.split(' contain ')
    outer_bag = split[0][:-5]

    contained_bags_string = split[1]

    if contained_bags_string != 'no other bags':
        contained_bags_list = contained_bags_string.split(', ')
        for contained in contained_bags_list:
            # only single digit numbers of bags so easy to parse
            # first digit is amount
            amount = int(contained[0])
            # account for bag or bags
            # No ternary in  python :(
            bag_length = None
            if contained[-1] == 's':
                bag_length = -5
            else:
                bag_length = -4
            name = contained[2:bag_length]
            new_rule[name] = amount

    rules_dict[outer_bag] = new_rule

# print(rules_dict)


# Now to find how many colors can eventually carry a gold bag.

# Rules list for colors is also the list of colors, so iterate through that

# counter
# For each rule in rules_dict
# Continue if shiny gold, needs to be in a bag
# if rule contains shiny gold bag, + 1 and continue

# This should/could be recursive.  Or can use while rule not empty

# This might have infinite loops.  Continue when we get there
# could be a recursive base case

# DFS???
# Or probably BFS.   This could go very deep, but it's not that broad
# Build at tree basically.  BFS, stop when you hit gold.

# Can memoize this to be more efficient.
# Might as well make a function for any color

# recursive.  Or maybe hybrid?
# external because doing this hybrid
cached = set()
# caching this way is only finding 1 layer anyway
def bag_can_hold_color(color, target_color, rules_dict):
    # print(color)
    if color in cached:
        return True

    if color == target_color:
        print("color is gold")
        return True

    # print(rules_dict[color])
    # Empty dict means bag can't hold bags
    # if rules_dict[color] == {}:
    #     # print("empty rules dict")
    #     # print(rules_dict[color])
    #     return False

    # if target_color in rules_dict[color]:
    #     # breakpoint()
    #     # print(color)

    #     print(f"adding first layer to cache: {color}")
    #     cached.add(color)
    #     # print(len(cached))
    #     return True

    for held_color in rules_dict[color]:
        # print(rules_dict[color])
        # print(held_color)
        result = bag_can_hold_color(held_color, target_color, rules_dict)
        if result == True:
            # print(f"adding second layer to cache: {color}")
            cached.add(color)
            return result

        # All variants of return false were breaking the stack, not needed
        # Return False




# Part 1
# count = 0
# for bag, contained_bags in rules_dict.items():
#     # we want in one layer of bags, skip gold
#     if bag == 'shiny_gold':
#         continue

#     if bag_can_hold_color(bag, 'shiny_gold', rules_dict, set()):
#         count += 1

# preserving the above, because I've commonly seen students abandon
# their plan at this stage, when they don't get the result, because
# they assume the were wrong about how to do it and try something different
# because they didn't completely debug their code to confirm things.

# In this case, it looks like it's working perfectly, just not giving me
# the result I want because I've been typing too many python vars
# and accidentally put an underscore in shiny_gold.

# This still isn't quite right, debugging continues!
# problem was in recursion
count = 0
for bag, contained_bags in rules_dict.items():
    # we want in one layer of bags, skip gold
    if bag == 'shiny gold':
        continue

    # this resets the cache, moving external
    if bag_can_hold_color(bag, 'shiny gold', rules_dict):
        count += 1


# print(len(cached))


# print(count)


# part 2

# Another search, recursive BFS again, this time count total
# def bag_must_contain(color, rules_dict, total):
#     for bag in rules_dict[color]:
#         total += bag_must_contain(bag, rules_dict, total)

#     return total

# print(bag_must_contain('shiny gold', rules_dict, 0))

# Doing the dumb way first, actually simpler to do iterative
# TODO: CACHE RESULTS OF A BAG
# HAHA THIS IS SO INEFFICIENT
# Assuming loops not possible from what we learned earlier

# def count_total_bags(color):
#     count = 0
#     stack = []
#     stack.append(color)

#     while (len(stack) > 0):
#         count += 1
#         current = stack.pop()
#         for held_color in rules_dict[color]:
#             stack.append(held_color)

#     return count

# Time complexity is horrible.  Doesn't work need to refactor
# Leaving because this is a fun example

# PLAN

# NO!!! 1 actually use the results of part 1 to trim the tree
# Actually, part 1 is unrelated, need to cache bags held

# 2 If need be, cached the total held per bag type

# running it above just to get cached full, should refactor later

# REMEMBER WHAT YOU JUST SAID ABOUT CONFIRMING YOUR PLAN IS ACTUALLY
# WORKING BEFORE ABANDONING IT BRIAN!?!?!?!?!?!?!?!?

# Though I am very distracted today.

# This is not working and not accounting for extra bags

# Works fine enough, but very inefficient.  Should cache

def count_total_bags(color):
    count = 0
    stack = []
    stack.append(color)

    while (len(stack) > 0):
        count += 1
        current = stack.pop()
        # print(f"Current is: {current}")
        for held_color in rules_dict[current]:
            for _ in range(0, rules_dict[current][held_color]):
                stack.append(held_color)

    return count - 1 # Don't count the gold bag in the beginning

print(count_total_bags('shiny gold'))
