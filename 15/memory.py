with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)

numbers = data[0].split(',')
numbers = [int(num) for num in numbers]

print(numbers)

spoken = set() # not sure I even need two
last_spoken = dict()

last_number = None
turn = 1
# speak the numbers in the list first and add them to dicts

for i in range(len(numbers) - 1):
    spoken.add(numbers[i])
    last_spoken[numbers[i]] = turn
    turn += 1
    last_number = numbers[i]
    print(last_number)

# bridge between two modes of operation
last_number = numbers[-1]
print(last_number)

while turn < 30000000:
    # process new last spoken number
    if last_number not in spoken:
        spoken.add(last_number)
        last_spoken[last_number] = turn
        last_number = 0
    else:
        # breakpoint()
        new_number = turn - last_spoken[last_number]
        last_spoken[last_number] = turn
        last_number = new_number

    turn += 1



print(last_number)
