# should be using with...
with open('data.txt', 'r') as file:
    boarding_data = file.read().split('\n')

# cut trailing newline
boarding_data.pop(-1)



#############AFTER COMPLETION#################

# oh so very dirty, it's just a binary number!?!?!?!?!?

def get_binary_position(seat):
    row_data = seat[:7]
    column_data = seat[7:]

    row_data = row_data.replace('F', '0')
    row_data = row_data.replace('B', '1')

    column_data = column_data.replace('L', '0')
    column_data = column_data.replace('R', '1')

    return [int(row_data, 2), int(column_data, 2)]

##############################################

print(get_binary_position('FBFBBFFRLR'))
