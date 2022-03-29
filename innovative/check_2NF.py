# Example 1: Table is in 2nd NF
# fd = {
#     'AB' : 'CD',
#     'C' : 'D'
# }
# ck = "AB"
# attributes = "ABCD"

# Example 2 : Not 2nd Normal Form
fd = {
    'AB' : 'CDE',
    'B' : 'D'
}
ck = "AB"
attributes = "ABCDE"


# Find Prime and Non Prime Attributes
def find_PA_and_NPA(ck, attributes):
    keys = ck.replace(" ", "")
    PA = set(keys)
    
    attributes = set(attributes)
    NPA = attributes.difference(PA)
    return PA, NPA


# Checking if LHS is proper subset of candidate key
def check_2_NF(ck):
    PA, NPA = find_PA_and_NPA(ck, attributes)
    ck_keys = ck.split(" ")

    # NOTE: if it returns true then the table is not in 2nd normal form (its having PD)

    for c in ck_keys:   # for each candidate key we will be checking 2 conditions
        ck_set = set(c)

        # Checking RHS side Condition: if its a non prime attribute then we are having partial Dependency and its not in 2nd NF
        for item in NPA:
            for i, j in fd.items():
                if item in j:
                    x = set(i)      
                    if x.issubset(ck_set):      # Now Checking LHS is a propers subset of Candidate key or not
                        if not x == ck_set:
                            return True


flag = check_2_NF(ck)
if flag==True:
    print("Not in 2nd NF")
else:
    print("Table is in 2nd NF")

