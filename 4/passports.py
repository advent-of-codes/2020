# should be using with...
with open('data.txt', 'r') as file:
    passport_data = file.read().split('\n\n')

# # Git rid of last newline added by tool
# passport_data.pop(len(passport_data)-1)

# Above gets rid of the last entry, not last extra \n
# this will correctly, and I just remembered how lists work in python

passport_data[-1] = passport_data[-1].rstrip('\n')

# Splitting by two newlines to group

# strip newlines

# might not need this

# for i in range(0, len(tree_data)):
#     tree_data[i] = tree_data[i].strip()


# Data is a mess, out of order,

# Separated by newlines, could split that way

# Read as a string, then split by newline
organized_dict_list = []
required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
count = 0

# part 1 solution
# for group in passport_data:
#     # convert newline to space then separate
#     organized_list = group.replace('\n', ' ').split(' ')

#     organized_dict = dict()
#     for pair in organized_list:
#         split_pair = pair.split(':')
#         organized_dict[split_pair[0]] = split_pair[1]

#     organized_dict_list.append(organized_dict)

# for passport in organized_dict_list:
#     if all(k in passport for k in required_keys):
#         count += 1

# print(count)


#validation ranges [0] is min, [1] is max, [2]
# except it's not that simple

birth_year = [1920, 2002]
issue_year = []

for group in passport_data:
    # convert newline to space then separate
    organized_list = group.replace('\n', ' ').split(' ')

    organized_dict = dict()
    for pair in organized_list:
        split_pair = pair.split(':')
        organized_dict[split_pair[0]] = split_pair[1]

    organized_dict_list.append(organized_dict)

for passport in organized_dict_list:
    if not all(k in passport for k in required_keys):
        # no need to validate if missing fields
        continue
    else:
        # hardcoding validation for first pass
        # TODO: FIX HARDCODING
        # validate birth year
        if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
            continue

        # validate issue year
        if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
            continue

        # validate expiration year
        if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
            continue

        # validate height
        unit = passport['hgt'][-2:]
        amount = int(passport['hgt'][:-2])
        if unit == 'in':
            if amount < 59 or amount > 76:
                continue

        elif unit == 'cm':
            if amount < 150 or amount > 193:
                continue

        else:
            continue

        # print(passport['hgt'])

        # validate hair color
        # check for #
        left = passport['hcl'][0]
        right = passport['hcl'][1:]
        if left != '#':
            continue
        if len(right) != 6:
            continue
        try:
            # valid hexadecimal can be converted to int
            # NEEDS THE 16 OR IT WILL WORK WITH ANY STRING!
            int(right, 16)
        except:
            continue

        # print(passport['hcl'])

        # validate eye color
        valid_eyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if passport['ecl'] not in valid_eyes:
            continue
        # else:
        #     print(passport['ecl'])

        # validate passport id
        # TODO: IF WRONG< MIGHT NOT BE ALL NUMBERS HERE, int() again
        if len(passport['pid']) != 9:
            continue
        # else:
        #     print(passport['pid'])

        # validate country
        # ignored per spec

        # all validations pass, count this one
        count += 1

print(count)
