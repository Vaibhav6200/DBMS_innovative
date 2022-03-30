input_string = '''
X-W, WZ-X, WZ-Y, Y-W, Y-X, Y-Z
'''

function_dependencies_dict = {}

for fd in input_string.split(","):
    fd = fd.strip()
    el_fd = fd.split("-")
    if el_fd[0] in function_dependencies_dict.keys():
        function_dependencies_dict[el_fd[0]] += el_fd[1]
    else:
        function_dependencies_dict[el_fd[0]] = el_fd[1]

print(function_dependencies_dict)

closure_set = {}

set_of_left_side = set()

for key in function_dependencies_dict:
    set_of_left_side.add(key)

# print(set_of_left_side)


def closure_finding_algorithm(x_plus, fds_dict):
    for fd_left in fds_dict:  # for each FD: Y --> Z in F Do
        fd_left_set = set()
        fd_right_set = set()
        for i in fd_left:
            fd_left_set.add(i)
        for i in fds_dict[fd_left]:
            fd_right_set.add(i)
        if fd_left_set.issubset(x_plus):  # if Y is subset of x+
            x_plus = x_plus.union(fd_right_set)  # x+ = x+ U Z
    return x_plus


for x in set_of_left_side:
    closure_x = set((x))  # x+ = {x}
    closure_x = closure_finding_algorithm(
        closure_x, function_dependencies_dict)
    closure_x = closure_finding_algorithm(
        closure_x, function_dependencies_dict)

    closure_set[x] = closure_x

print(closure_set)
