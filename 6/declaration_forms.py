# should be using with...
with open('data.txt', 'r') as file:
    customs_data = file.read().split('\n\n')

# cut trailing newline
customs_data[-1] = customs_data[-1].rstrip('\n')


# Part 1 solution
# tallied_responses = []

# for group in customs_data:
#     # convert newline to space then separate
#     organized_list = group.replace('\n', ' ').split(' ')
#     group_responses = set()
#     for person in organized_list:
#         for char in person:
#             group_responses.add(char)

#     tallied_responses.append(group_responses)



# total = 0

# for response in tallied_responses:
#     total += len(response)

# print(total)


# Misread the spec.  It's not all yes across the board, it's by group

# It will be more efficient to go by letter, check the responses
# then continue and delete the letter the first time not found

# questions = set('abcdefghijklmnopqrstuvwxyz'.split(''))

# for letter in questions:
#     for group in tallied_responses:
#         if letter not in group:
#             questions.remove(letter)
#             break


# Part 2 solution
tallied_responses = []

for group in customs_data:
    # convert newline to space then separate
    organized_list = group.replace('\n', ' ').split(' ')
    # start with a filled set of responses and remove those missing
    possible_responses = set('abcdefghijklmnopqrstuvwxyz')
    # It doesn't like me removing from the set while iterating
    missing_responses = set()
    for char in possible_responses:
        # print(person)
        for person in organized_list:
            if char not in person:
                # breakpoint()
                missing_responses.add(char)
                # breakpoint()
                break


    tallied_responses.append(possible_responses - missing_responses)



total = 0

for response in tallied_responses:
    total += len(response)

print(total)
