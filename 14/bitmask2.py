with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)


def parse_mask(line):
    split = line.split(' ')
    return split[2]

def parse_memory(line):
    split = line.split(' ')
    value = split[-1]
    address = split[0].split('[')[-1][:-1]
    # breakpoint()
    return address, value

def apply_mask(address, mask):
    # easiest to use a string here, probably not best
    # actually, that's just how bin() works
    bin_number = bin(int(address))
    bin_number = bin_number[2:]

    # expand bin number to 36 digits
    bin_number = '0' * (36 - len(bin_number)) + bin_number

    # breakpoint()

    masked = ""
    exes = []

    for i in range(len(mask)):
        # breakpoint()
        if mask[i] == 'X':
            masked = masked + 'X'
            exes.append(i)
        elif mask[i] == '0':
            masked = masked + bin_number[i]
        elif mask[i] == '1':
            masked = masked + '1'


    # max is 36, just do the permutations for all
    # I think I can do some clever binary to count up
    addresses = []

    binary_counter = '0' * len(exes)
    binary_max = '1' * len(exes)

    while (int(binary_counter, 2) <= int(binary_max, 2)):
        new_address_list = list(masked)
        for i in range(len(binary_counter)):
            # print(i)
            # breakpoint()
            new_address_list[exes[i]] = binary_counter[i]

        binary_address = "".join(new_address_list)
        addresses.append(int(binary_address, 2))

        # increment the binary counter
        # dealing with the 0b and keeping the same number of digits
        counter = int(binary_counter, 2)
        counter += 1
        binary_counter = bin(counter)
        binary_counter = binary_counter[2:]
        binary_counter = '0' * (len(binary_max) - len(binary_counter)) + binary_counter
        # breakpoint()

    # breakpoint()
    return addresses



def process_data(data):
    current_mask = None
    mem = dict()

    for line in data:
        if line[:3] == 'mem':
            address, value = parse_memory(line)
            addresses = apply_mask(address, current_mask)

            for address in addresses:
                mem[address] = value

        if line[:4] == 'mask':
            current_mask = parse_mask(line)

    total = 0
    for key, value in mem.items():
        # breakpoint()
        total += int(value)

    return(total)



print(process_data(data))
