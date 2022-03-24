input_string = '''
A-BC, BC-DE, D-F, CF-G
'''

function_dependencies_dict = {}

for fd in input_string.split(","):
    fd = fd.strip()
    el_fd = fd.split("-")
    function_dependencies_dict[el_fd[0]] = el_fd[1]

print(function_dependencies_dict)

closure_set = {}

set_of_attributes = set()

for key in function_dependencies_dict:
    for ch in key:
        set_of_attributes.add(ch)
    for ch in function_dependencies_dict[key]:
        set_of_attributes.add(ch)

# print(set_of_attributes)

for x in set_of_attributes:
    fd_x = set((x))  # x+ = {x}
    for fd_left in function_dependencies_dict:  # for each FD: Y --> Z in F Do
        fd_left_set = set()
        fd_right_set = set()
        for i in fd_left:
            fd_left_set.add(i)
        for i in function_dependencies_dict[fd_left]:
            fd_right_set.add(i)
        if fd_left_set.issubset(fd_x):  # if Y is subset of x+
            fd_x = fd_x.union(fd_right_set)  # x+ = x+ U Z
    closure_set[x] = fd_x

print(closure_set)
