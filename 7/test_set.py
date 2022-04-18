my_set = set()
my_set.add(0)

def add_to(a_set):
    a_set.add(len(a_set))
    if len(a_set) < 10:
        add_to(a_set)

add_to(my_set)

print(my_set)

# so I've confirmed I'm not crazy sets pass by reference...
