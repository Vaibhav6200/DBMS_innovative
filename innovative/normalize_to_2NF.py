fd = {
    'AB' : 'C',
    'C' : 'D',
    'C' : 'E',
    'E' : 'F',
    'F' : 'A',
}
ck = "AB FB EB CB"
attributes = "ABCDEF"


def find_PA_and_NPA(ck, attributes):
    keys = ck.replace(" ", "")
    PA = set(keys)
    
    attributes = set(attributes)
    NPA = attributes.difference(PA)
    return PA, NPA


def check_2_NF(ck):
    PA, NPA = find_PA_and_NPA(ck, attributes)
    ck_keys = ck.split(" ")

    for c in ck_keys:  
        ck_set = set(c)
        for item in NPA:
            for i, j in fd.items():
                if item in j:
                    x = set(i)      
                    if x.issubset(ck_set):
                        if not x == ck_set:
                            return True, i


def decompose(x):
    fd2={}
    fd2[x] = fd[x]
    fd1 = fd.copy()
    del fd1[x]
    print(fd)   
    print(fd1)    
    print(fd2)    

# x is that fd which is creating problem
flag, x = check_2_NF(ck)
decompose(x)

if flag==True:
    print("Not in 2nd NF")
else:
    print("Table is in 2nd NF")

