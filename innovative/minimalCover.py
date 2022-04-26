import itertools

def closure(keys, values, att, isWith):
    X = set(att)
    if(isWith == -1):
        for i in range(len(keys)):
            if att == keys[i]:
                for j in values[i]:
                    X.add(j)

        for k in range(len(keys)):
            for i in range(len(keys)):
                if set(keys[i]).issubset(X):
                    for j in values[i]:
                        X.add(j)

        return X

    for i in range(len(keys)):
        if i == isWith:
            continue
        if att == keys[i]:
            for j in values[i]:
                X.add(j)

    for k in range(len(keys)):
        for i in range(len(keys)):
            if i == isWith:
                continue
            if set(keys[i]).issubset(X):
                for j in values[i]:
                    X.add(j)
    return X

def findsubsets(s, n):
    subset = []
    for j in range(1, n):
        for i in itertools.combinations(s, j):
            subset.append(list(i))
    return subset

def step1(keys, values):
    k = []
    v = []

    for i in range(len(keys)):
        if len(values[i]) > 1:
            for j in values[i]:
                k.append(keys[i])
                v.append(j)
        else:
            k.append(keys[i])
            v.append(values[i])
    return k, v

def step2(k, v):
    keys = k
    values = v
    count = 0
    for i in k:
        withFD = sorted(closure(keys, values, keys[count], -1))
        withoutFD = sorted(closure(keys, values, keys[count], count))

        if withFD == withoutFD:
            keys[count] = 0
            values[count] = 0
            keys.remove(0)
            values.remove(0)
        else:
            count += 1
    return keys, values

def step3(keys, values):
    count = 0
    for i in keys:
        if len(i) > 1:
            closureFD = sorted(closure(keys, values, i, -1))
            subset = findsubsets(i, len(i))
            for i in subset:
                key = "".join(i)
                closureSub = sorted(closure(keys, values, key, -1))

                if closureSub == closureFD:
                    keys[count] = key
                    break
        count += 1

    return keys, values


def removeTrnas(keys, values):
    count = 0
    n = len(keys)
    k = keys
    v = values
    for i in range(n):
        if values.__contains__(keys[i]) and keys[i] != "":
            indx = values.index(keys[i])

            Tkey = keys[indx]
            Tvalue = values[i]

            for i in range(n):
                if keys[i] == Tkey and values[i] == Tvalue:
                    k[i] = ""
                    v[i] = ""
                    count += 1

    for i in range(count):
        k.remove('')
        v.remove('')

    return keys, values


def merge(keys, values):
    cover = {}
    for i in range(len(keys)):
        if keys[i] in cover:
            cover[keys[i]] = cover[keys[i]] + values[i]
        else:
            cover[keys[i]] = values[i]
    return cover

def canonical_cover(request):
    pass
    # key value array

# creating a function dependency for any relational schema
# using dictionary where x is key and y is values

#Example-1
# key = ['a', 'ac', 'e']
# value = ['c', 'd', 'adh']
# ['a', 'a', 'e', 'e'] ['c', 'd', 'a', 'h']

# Example-2
# key = ['a', 'a', 'b', 'ab']
# value = ['bc', 'b', 'c', 'c']
# ['a', 'b']
# ['b', 'c']

# Example-3
# key = ['x', 'wz', 'y']
# value = ['w', 'xy', 'wxz']
# ['x', 'wz', 'y', 'y']
# ['w', 'y', 'x', 'z']

# Example-4
# key = ['a', 'cd', 'b', 'e']
# value = ['bc', 'e', 'd', 'a']
# ['a', 'a', 'cd', 'b', 'e']
# ['b', 'c', 'e', 'd', 'a']

# Example-5
# key = ['v', 'vw', 'y']
# value = ['w', 'x', 'vxz']
# ['v', 'v', 'y', 'y']
# ['w', 'x', 'v', 'z']


key, value = step1(key, value)
key, value = step2(key, value)
key, value = step3(key, value)
key, value = removeTrnas(key, value)