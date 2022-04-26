# CONDITION FOR 3rd NORMAL FORM:
# 1. Check whether its in 2nd NF or not
# 2. (all LHS attributes in fd's should be CK) or (RHS should Be Prime Attribute)

# Example 1 : Table is in 3rd Nf
# fd = {
#     'AB' : 'C',
#     'C' : 'E',
#     'E' : 'F',
#     'F' : 'A'
# }
# attributes = "ABCDEF"
# ck = "AB FB EB CB"

# Example 2 : Not in 3rd Nf
fd = {
    'AB' : 'C',
    'C' : 'DE',
    'E' : 'F',
    'F' : 'A'
}
attributes = "ABCDEF"
ck = "AB FB EB CB"


def find_PA_and_NPA(ck, attributes):
    keys = ck.replace(" ", "")
    PA = set(keys)

    attributes = set(attributes)
    NPA = attributes.difference(PA)
    return PA, NPA

# If it returns true : means we are having transitive dependency so table is not in 3rd NF
def check_3_NF(ck):
    ck_keys = ck.split(" ")
    PA, NPA = find_PA_and_NPA(ck, attributes)
    prime_attributes = "".join(PA)

    for i, j in fd.items():
        if not i in ck_keys:
            if not j in prime_attributes:
                return False
    return True    # if all above conditions are false then there is no transitive dependency and hence its in 3rd NF


# If it returns true : means we are having transitive dependency so table is not in 3rd NF
flag = check_3_NF(ck)
if flag==True:
    print("Yes! Table is in 3rd NF")
else:
    print("Not in 3rd NF")

