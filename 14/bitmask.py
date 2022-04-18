with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)


# mask = 11X01X101X10000110110101X100000011XX
# mem[30904] = 804
# mem[25640] = 58672415
# mem[44254] = 829902099
# mask = 0100X100101000X0X01100X011100X000011
# mem[16446] = 3614672


# mem commands work like dicts -> mem[30904] = 804 is write 804 in address 30904

# bitmask is always 36 chars or bits

# most significant on left, least on right
# current bitmask is applied to values before written

# value:  000000000000000000000000000000001011  (decimal 11)
# mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# result: 000000000000000000000000000001001001  (decimal 73)

def parse_mask(line):
    split = line.split(' ')
    return split[2]

def parse_memory(line):
    split = line.split(' ')
    value = split[-1]
    address = split[0].split('[')[-1][:-1]
    # breakpoint()
    return address, value

def apply_mask(value, mask):
    print(f'before: {value}')
    # easiest to use a string here, probably not best
    # actually, that's just how bin() works
    bin_number = bin(int(value))
    # if bin_number[0] == 'b':
    #     breakpoint()
    # breakpoint()
    bin_number = bin_number[2:]

    # expand bin number to 36 digits

    bin_number = '0' * (36 - len(bin_number)) + bin_number

    # breakpoint()

    masked = ""

    for i in range(len(mask)):
        # breakpoint()
        if mask[i] == 'X':
            masked = masked + bin_number[i]
        elif mask[i] == '0':
            masked = masked + '0'
        elif mask[i] == '1':
            masked = masked + '1'

    # breakpoint()
    final = int(masked, 2)

    print(f'after: {final}')
    # breakpoint()
    return final



def process_data(data):
    current_mask = None
    mem = dict()

    for line in data:
        if line[:3] == 'mem':
            address, value = parse_memory(line)
            mem[address] = apply_mask(value, current_mask)

        if line[:4] == 'mask':
            current_mask = parse_mask(line)

    total = 0
    for key, value in mem.items():
        # breakpoint()
        total += int(value)

    return(total)



print(process_data(data))
