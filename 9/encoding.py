# should be using with...
with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)


# 0-24 are preamble.

# 25 +, each number should be sum of any two in prev 25

# find the first number in which is NOT the sum of two of
# the first 25 numbers


# Brute force:
# For each number,
# for the 25 before, add all values in pairs until finding a match


# Better?:
# Sort previous 25 numbers, or just put in set, do like 2 number sum
# Part 1
# for i in range(25, len(data)):
#     test_set = set(data[i - 25:i])
#     # for this small of a sample size, sorting and adding to a set
#     # might be more expensive.  But it's more fun so :shrug:

#     # could only do half here, i think
#     not_found = True
#     for value in test_set:
#         # breakpoint()
#         other_half = int(data[i]) - int(value)

#         if str(other_half) in test_set:
#             # print("Found other half")
#             not_found = False
#             break

#     # Yet again, making sure code is executing plan is key
#     if not_found:
#         print(data[i])
#         breakpoint() lazy :p

# Part 2

magic_number = 21806024
magic_index = 511

# need to find contiguous numbers that add up to this
# says at least two.  More than one possibility?

# maybe go backwards.  Start at magic number?

# brute force: go backwards from magic_index
# Add each number in series
# might be slow, but lets try it

def find_weakness():
    for i in range(magic_index - 1, -1, -1):
        # print(i)
        weakness_range = []
        total = 0
        j = i
        while total < magic_number:
            total += int(data[j])
            weakness_range.append(data[j])
            j -= 1
            if total == magic_number:
                return weakness_range

    return "Unable to find weakness"

weakness_range = find_weakness()

# smallest + largest, not first plus last!!!

# print(int(weakness_range[0]) + int(weakness_range[-1]))

# faster to collect these in the function probably
weakness_ints = [int(num) for num in weakness_range]

print(min(weakness_ints) + max(weakness_ints))
