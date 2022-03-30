import itertools

input_string = '''
A-BC, C-B, D-E, E-D
'''

function_dependencies_dict = {}

for fd in input_string.split(","):
    fd = fd.strip()
    el_fd = fd.split("-")
    function_dependencies_dict[el_fd[0]] = el_fd[1]

# print(function_dependencies_dict)

closure_set = {}

set_of_attributes = set()

for key in function_dependencies_dict:
    for ch in key:
        set_of_attributes.add(ch)
    for ch in function_dependencies_dict[key]:
        set_of_attributes.add(ch)

# print(set_of_attributes)


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


for x in set_of_attributes:
    closure_of_x = set((x))  # x+ = {x}
    closure_of_x = closure_finding_algorithm(
        closure_of_x, function_dependencies_dict)
    closure_of_x = closure_finding_algorithm(
        closure_of_x, function_dependencies_dict)
    closure_set[x] = closure_of_x

# print(closure_set)

essential_attributes = set()
candidate_keys_set = []
side_of_attribute_appearence = {}

for x in set_of_attributes:
    side_of_attribute_appearence[x] = []
    for fd in function_dependencies_dict:
        if x in fd and 'left' not in side_of_attribute_appearence[x]:
            side_of_attribute_appearence[x].append('left')
        if x in function_dependencies_dict[fd] and 'right' not in side_of_attribute_appearence[x]:
            side_of_attribute_appearence[x].append('right')

# print(side_of_attribute_appearence)

for x in side_of_attribute_appearence:
    if 'right' not in side_of_attribute_appearence[x]:
        essential_attributes.add(x)

# print(essential_attributes)

union_of_essential_attributes = set()


def find_union_of_closures(source_set, closure_set):
    union_of_closures_of_source_set = set()
    for x in source_set:
        union_of_closures_of_source_set = union_of_closures_of_source_set.union(
            closure_set[x])
    return union_of_closures_of_source_set


union_of_essential_attributes = find_union_of_closures(
    essential_attributes, closure_set)

# print(union_of_essential_attributes)

if union_of_essential_attributes == set_of_attributes:
    candidate_keys_set.append(essential_attributes)
else:
    non_essential_attributes = set_of_attributes.difference(
        essential_attributes)
    list_of_all_combinations = []
    for L in range(0, len(non_essential_attributes) + 1):
        for comb in itertools.combinations(non_essential_attributes, L):
            if comb != ():
                list_of_all_combinations.append(set(comb))
    for comb in list_of_all_combinations:
        possible_ck = essential_attributes.union(comb)
        if find_union_of_closures(possible_ck, closure_set) == set_of_attributes:
            candidate_keys_set.append(possible_ck)

print("Closure of all attributes:\n", closure_set)
print("All possible candidate keys:\n", candidate_keys_set)
