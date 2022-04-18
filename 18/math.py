with open('data.txt', 'r') as file:
    data = file.read().split('\n')

# cut trailing newline
data.pop(-1)


# left to right with no precedence
# parens work as normal

# find inner parens, calculate and reduce
# then calculate left to right

# always single digit ints
# doesn't matter, gets bigger

# Evaluate an expression with two or more nums and an operator

# helpers

def math(a, b, op):
    if op == '+':
        return a + b
    # if op == '-':
    #     return a - b
    if op == '*':
        return a * b
    # if op == '%':
    #     return a / b

    print("BAD OPERATOR")

def eval_expression(exp):
    debug_original_exp = exp

    result = 0

    numbers = []
    operations = []

    new_num_str = ""

    while len(exp) > 0:
        char = exp[0]
        exp = exp[1:]

        try:
            int(char) # no idea of speed of this vs ord().  Prob slower
            new_num_str += char

        except ValueError:
            if len(new_num_str) > 0:
                # no division, only ints for now
                numbers.append(int(new_num_str))
                new_num_str = ""
            operations.append(char)


    # we should always end with a number, so append the last one
    numbers.append(int(new_num_str))



    # [1, 2, 3, 4, 5, 6]
    # [+, *, +, *, +]

    # do addition first

    i = 0 # python
    while i < len(operations):
        # breakpoint()
        if operations[i] == '*':
            i += 1
            continue
        else:
            # left operand shares same i
            # add the two numbers
            new_num = math(numbers[i], numbers[i+1], operations[i])
            # replace first operand with new number
            numbers[i] = new_num
            # delete the second
            del numbers[i+1]
            # remover the operator
            del operations[i]
            # short problems so just reset the loop
            i = 0

    result = numbers.pop(0)

    # process multiplication
    while len(numbers) > 0:
        op = operations.pop(0)

        b = numbers.pop(0)

        result = math(result, b, op)

    # print(debug_original_exp, ' == ', result)
    return str(result)



# print(eval_expression('5+5*5'))

def solve_problem(problem):
    stack = problem[0]
    problem = problem[1:]

    while len(problem) > 0:
        # print(problem)
        char = problem[0] # short enough not to matter
        problem = problem[1:]

        if char == ' ': # don't need spaces
            continue

        if char != ')': # only one, no need for dict
            stack = stack + char
        # if it's close parens, roll back and grab the expression
        else:
            exp = ""
            while len(stack) > 0 and stack[-1] != "(":
                # breakpoint()
                exp = stack[-1] + exp
                stack = stack[:-1]

            # get rid of (
            stack = stack[0:-1]

            # add the evaluated expression from in ()
            stack = stack + eval_expression(exp)



    return eval_expression(stack)

# print(solve_problem('1 + 2 * 3 + 4 * 5 + 6'))

total = 0

for problem in data:
    total += int(solve_problem(problem))

print(total)


# Part 1 Evaluate Expression:

# def eval_expression(exp):
#     debug_original_exp = exp

#     result = 0

#     numbers = []
#     operations = []

#     new_num_str = ""

#     while len(exp) > 0:
#         char = exp[0]
#         exp = exp[1:]

#         try:
#             int(char) # no idea of speed of this vs ord().  Prob slower
#             new_num_str += char

#         except ValueError:
#             if len(new_num_str) > 0:
#                 # no division, only ints for now
#                 numbers.append(int(new_num_str))
#                 new_num_str = ""
#             operations.append(char)


#     # we should always end with a number, so append the last one
#     numbers.append(int(new_num_str))

#     result = numbers.pop(0)

#     while len(operations) and len(numbers) > 0:
#         op = operations.pop(0)

#         b = numbers.pop(0)

#         result = math(result, b, op)

#     # print(debug_original_exp, ' == ', result)
#     return str(result)
