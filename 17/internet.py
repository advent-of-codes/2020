# Number 1 result on internet
# https://dev.to/qviper/advent-of-code-2020-python-solution-day-17-g6k

import timeit

start_time = timeit.default_timer()


def part2():
    with open("data.txt") as fp:
        lines = [fline.rstrip() for fline in fp.readlines()]
    f = lines
    cubes = {(i, j, 0, 0):lines[i][j]
             for i in range(len(lines))
             for j in range(len(lines[0]))}
    for i in range(10):
        cubes = simulate4d(cubes)

    print(f"Part 2 Solution: {list(cubes.values()).count('#')}")


def simulate4d(cubes):
    new = {}
    for c in cubes:
        x = checkNeighbors4d(c, cubes)
        if cubes[c] == '#':
            if x == 2 or x == 3:
                new[c] = '#'
            else:
                new[c] = '.'
            n = findNeighbors4d(c)
            for x in n:
                if x not in cubes:
                    k = checkNeighbors4d(x, cubes)
                    if k == 3:
                        new[x] = '#'
        elif cubes[c] == '.':
            if x == 3:
                new[c] = '#'
            else:
                new[c] = '.'
    return new


def findNeighbors4d(c):
    neighbors = [(c[0]+i, c[1]+j, c[2]+k, c[3]+w)
                 for i in range(-1, 2)
                 for j in range(-1, 2)
                 for k in range(-1, 2)
                 for w in range(-1, 2)
                 if not (i == 0 and j == 0 and k == 0 and w == 0)]
    return neighbors


def checkNeighbors4d(c, cubes):
    n = findNeighbors4d(c)
    neighbors_count = len([x for x in n if cubes.get(x)=="#"])
    return neighbors_count
part2()


print(timeit.default_timer() - start_time)
