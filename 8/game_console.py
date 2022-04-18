# should be using with...
with open('data.txt', 'r') as file:
    boot_code = file.read().split('\n')

# cut trailing newline
boot_code.pop(-1)


# Part 1

# accumulator = 0

# # Instructions

# # 'acc' - accumulator += 1, call next
# # 'jmp' - jumps to new instruction by offset
# # 'nop' - does nothing, call next

# run_instructions = set()
# cursor = 0

# while cursor not in run_instructions:
#     run_instructions.add(cursor)
#     split_ins = boot_code[cursor].split(' ')
#     instruction = split_ins[0]
#     multiplier = None

#     # if split_ins[1][0] == '+':
#     #     multiplier = 1
#     # else:
#     #     multiplier = -1

#     value = int(split_ins[1])

#     # switch(instruction): no switch in python
#     # print(f'cursor: {cursor}')
#     # print(run_instructions)
#     if instruction == 'acc':  # TODO: Constants
#         accumulator += value
#         # print(f'cursor: {cursor}')
#         # print(boot_code[cursor])
#         cursor += 1
#     elif instruction == 'jmp':
#         cursor += value
#     elif instruction == 'nop':
#         cursor += 1

# print(accumulator)

# Part 2


# Instructions

# 'acc' - accumulator += 1, call next
# 'jmp' - jumps to new instruction by offset
# 'nop' - does nothing, call next

def test_boot_code(boot_code, to_swap):
    accumulator = 0
    run_instructions = set()
    cursor = 0

    while cursor not in run_instructions:
        print(cursor)
        if cursor == len(boot_code):
            print("PROGRAM BOOT SUCCESSFUL")
            print(accumulator)
            return True, accumulator

        if cursor > len(boot_code):
            print("PROGRAM FAILED: OUT OF BOUNDS")
            return False, accumulator

        run_instructions.add(cursor)
        split_ins = boot_code[cursor].split(' ')
        instruction = split_ins[0]

        # swap if needed
        if cursor == to_swap:
            print(f"swapping: {instruction}")
            if instruction == 'jmp':
                instruction = 'nop'  # = != == >:(
            elif instruction == 'nop':
                instruction = 'jmp'

        print(instruction)
        value = int(split_ins[1])

        if instruction == 'acc':  # TODO: Constants
            accumulator += value
            cursor += 1
        elif instruction == 'jmp':
            cursor += value
        elif instruction == 'nop':
            cursor += 1

    print("PROGRAM FAILED: INFINITE LOOP")
    return False, accumulator


# iterate through and test each jmp and nop
for i in range(0, len(boot_code)):
    # don't need unmodifed run, we know it's broken, but doing anyway
    print(f'swapping instruction {i}')
    result, accumulator = test_boot_code(boot_code, i)
    if result:
        print(accumulator)
        break
