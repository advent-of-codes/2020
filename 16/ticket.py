from functools import reduce

with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

for i in range(len(data)):
    if data[i] == 'nearby tickets:':
        ticket_index = i + 1

for i in range(len(data)):
    if data[i] == 'your ticket:':
        my_ticket_index = i + 1

my_ticket = data[my_ticket_index]
my_int_ticket = my_ticket.split(',')
my_int_ticket = [int(num) for num in my_int_ticket]

# 25 + are tickets
tickets = data[ticket_index:]
# breakpoint()
# put rules in a dict
rule_dict = dict()

row = 0
while data[row] != "":
    split_rules = data[row].split(': ')
    rule_name = split_rules[0]
    ranges = split_rules[1].split(' or ')
    range0 = ranges[0].split('-')
    range1 = ranges[1].split('-')

    # use nested tuple for rules
    # ((min, max), (min, max))
    rule_dict[rule_name] = ((int(range0[0]), int(range0[1])), (int(range1[0]), int(range1[1])))

    row += 1

# print(rule_dict)

# now need to find all invalid values for any field and add them up

# like frequency queries?  Except not continuous masking
# build a mask?
# small ruleset
# use a set as a mask, 0(1) lookup for validity

filter_set = set()

for rule_name, rule_ranges in rule_dict.items():
    for rng in rule_ranges:
        for i in range(rng[0], rng[1] + 1):
            filter_set.add(i)

# print(filter_set)

# find invalid
# Part 1
# count_valid = 0
# invalid = []

# for ticket in tickets:
#     # get the numbers
#     numbers = ticket.split(',')
#     numbers = [int(num) for num in numbers]

#     valid = True

#     for number in numbers:
#         if number not in filter_set:
#             invalid.append(number)
#             valid = False

#     if valid:
#         count_valid += 1

# print(sum(invalid))
# print(f'Valid: {count_valid}')

# Part 2

# create new list of only valid tickets

def check_ticket(ticket):
    # get the numbers
    numbers = ticket.split(',')
    numbers = [int(num) for num in numbers]

    for number in numbers:
        if number not in filter_set:
            return False

    return True

valid_tickets = []

for ticket in tickets:
    if check_ticket(ticket):
        valid_tickets.append(ticket)

# add my ticket:
valid_tickets.append(my_ticket)

# print(len(tickets))
# print(len(valid_tickets))

# create a list of possible fields for each position then remove them

possible_fields = []

for _ in range(len(rule_dict)):
    possible_fields.append(set(rule_dict.keys()))

# nested for loops go brrrrrrrrrrr!

# I think im missing some, maybe a different order
# could have saved some wasted time checking test data
# both ways worked
counter = 0
for i in range(len(possible_fields)):
    for ticket in valid_tickets:
        counter += 1
        numbers = ticket.split(',')
        number = int(numbers[i])
        # print(number)
        for rule_name, rule_range in rule_dict.items():
            if (number in range(rule_range[0][0], rule_range[0][1] + 1) or
                number in range(rule_range[1][0], rule_range[1][1] + 1)):
                # print(f'{number} is between {rule_range[0]} or {rule_range[1]}')
                continue
            else:
                if rule_name in possible_fields[i]:
                    possible_fields[i].remove(rule_name)
                    # print(f'Removed {rule_name} from position: {i}')

    # breakpoint()


# for ticket in valid_tickets:
#     # get the numbers
#     numbers = ticket.split(',')
#     numbers = [int(num) for num in numbers]

#     for i in range(len(numbers)):
#         number = numbers[i]
#         print(number)
#         for rule_name, rule_range in rule_dict.items():
#             # print(rule_name)
#             # if rule_name == 'type':
#             #     breakpoint()
#             # if the number is not in the range
#             # remove it from possible fields
#             # complicated logic statement incoming!!!
#             # put Python makes it a little better
#             if (number in range(rule_range[0][0], rule_range[0][1] + 1) or
#                 number in range(rule_range[1][0], rule_range[1][1] + 1)):
#                 print(f'{number} is between {rule_range[0]} or {rule_range[1]}')
#                 continue
#             else:
#                 if rule_name in possible_fields[i]:
#                     possible_fields[i].remove(rule_name)
#                     print(f'Removed {rule_name} from position: {i}')
#     breakpoint()

# print(possible_fields)
# for row in possible_fields:
#     print(row)


# AHA!  This process doesn't elimite all possibilities, need further processing.

# Brute force:  find the one with length 1 and remove that value from the others
# just do it the ugly way, again, small dataset


# longest = 0

# for results in possible_fields:
#     if len(results) > longest:
#         longest = len(results)

def process_results(possible_fields):
    confirmed_fields = set()
    while (True):
        all_ones = True
        for i in range(len(possible_fields)):
            if len(possible_fields[i]) == 1:
                # ugly but not sure how else to do it
                for field in possible_fields[i]:
                    confirmed_fields.add(field)
            if len(possible_fields[i]) > 1:
                for confirmed in confirmed_fields:
                    if confirmed in possible_fields[i]:
                        possible_fields[i].remove(confirmed)
            # check again, if still greater than one, need more processing
            if len(possible_fields[i]) > 1:
                all_ones = False

        if all_ones:
            return possible_fields

processed_results = process_results(possible_fields)

for row in processed_results:
    print(row)

departure_indexes = []

for i in range(len(processed_results)):
    field = processed_results[i]
    # results are still in sets containing 1 thing each
    if field.pop()[:len('departure')] == 'departure':
        departure_indexes.append(i)

# total = 0

# breakpoint()

dep_values = []

for i in range(len(departure_indexes)):
    index = departure_indexes[i]
    # total += my_int_ticket[index] // read the spec, multiply, not add
    dep_values.append(my_int_ticket[index])


# print(total)

print(reduce((lambda x, y: x * y), dep_values))


# count_departure_fields = 0
# for field in possible_fields:
#     # hardcode hack
#     dep = set(['departure location', 'departure station', 'departure platform', 'departure track', 'departure date', 'departure time'])

#     for rule in field:
#         if rule in dep:
#             count_departure_fields += 1
#             break

# print(count_departure_fields)
# breakpoint()
