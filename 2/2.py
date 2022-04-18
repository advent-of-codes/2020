import re

password_data = list(open('data.txt'))



# Plan

# For each entry


# split parts rules (Regex?)


# Get min/max


# Get letter

# Python magic to count in string str.count(var)

# += to counter if valid

count = 0

# Part 1 solution
# for password_string in password_data:

#     # amount_match = re.match(r'(\d)+-(\d)+', password.strip('\n'))
#     # min_max = amount_match.match.split('-')
#     # breakpoint()

#     split_password = password_string.split(' ')

#     min = int(split_password[0].split('-')[0])
#     max = int(split_password[0].split('-')[1])

#     char = split_password[1][0]

#     password = split_password[2]

#     num_char = password.count(char)

#     if num_char >= min and num_char <= max:
#         count += 1


# print(count)

for password_string in password_data:

    # amount_match = re.match(r'(\d)+-(\d)+', password.strip('\n'))
    # min_max = amount_match.match.split('-')
    # breakpoint()

    split_password = password_string.split(' ')

    position_1 = int(split_password[0].split('-')[0])
    position_2 = int(split_password[0].split('-')[1])

    char = split_password[1][0]

    password = split_password[2]

    value_position_1 = password[position_1 - 1]
    value_position_2 = password[position_2 - 1]


    # possibly need valid index check

    # doing dumb way because can't remember how to do not and

    if value_position_1 == char or value_position_2 == char:
        if value_position_1 != value_position_2:
            count += 1


print(count)
