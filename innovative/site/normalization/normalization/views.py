from django.shortcuts import render
import pandas as pd
import numpy as np
import itertools

# example - 1
# att = 'abcdefgh'
# key = ['ab', 'd', 'fg', 'a']
# value = ['cd', 'efg', 'h', 'h']

def index(request):
    fd = {}
    data = {}   # this contains all data that is to be rendered on home page

    key = []
    value = []
    if request.method == 'POST':
        attributes = request.POST['attributes']

        # Creating All Fd's Dynamically
        count = request.POST['count']
        for i in range(int(count)):
            a = "key" + str(i+1)
            b = "value" + str(i+1)
            k = request.POST[a]
            v = request.POST[b]
            key.append(k)
            value.append(v)
            fd[k] = v
        closures = {}
        for i in attributes:
            att_closure = closure(key, value, i, -1)
            closures[i] = att_closure

        data['closure'] = closures

        candidate_keys, super_keys = findCandidateKey(attributes, key, value)       # it returns list of all candidate keys
        data["candidate_keys"] = candidate_keys

        check1 = check_1_NF(attributes)     # returns a boolean value
        data["check1"] = check1

        # NOTE: To check for 2nd NF candidate keys should passed in form of string seperated by space
        ck = " ".join(candidate_keys)
        check2 = check_2_NF(fd, ck, attributes)     # check2 is check for 2nd Normal Form
        data["check2"] = check2

        check3 = check_3_NF(fd, ck, attributes)
        data["check3"] = check3

        # MINIMAL COVER
        key, value = step1(key, value)
        key, value = step2(key, value)
        key, value = step3(key, value)
        key, value = removeTrnas(key, value)
        minimal_cover = merge(key, value)
        data["minimal_cover"] = minimal_cover

        # Normalizing to 2nd Normal Form
        if not check2:
            relation_2nf = normalize_2nf(key, value, candidate_keys, attributes)
            data['relation_2nf'] = relation_2nf

        # Normalizing to 3rd Normal Form
        if not check3:
            relation_3nf = normalize_3nf(minimal_cover, super_keys, candidate_keys, attributes)
            data['relation_3nf'] = relation_3nf


    return render(request, 'index.html', data)


def find_PA_and_NPA(ck, attributes):
    keys = ck.replace(" ", "")
    PA = set(keys)
    attributes = set(attributes)
    NPA = attributes.difference(PA)
    return PA, NPA


# ---------- 1nd NORMAL FORM CHECK ----------       (Requirements : attributes)
def check_1_NF(attributes):
    len1 = len(attributes)
    result = set(attributes)
    len2 = len(result)
    if len1 != len2:
        return False
    return True

# ---------- 2nd NORMAL FORM CHECK ----------       (Requirements : fd, ck, attributes)
def check_2_NF(fd, ck, attributes):
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
                            return False
    return True


# ---------- 3rd NORMAL FORM CHECK ----------       (Requirements : fd, attributes, ck)
def check_3_NF(fd, ck, attributes):
    ck_keys = ck.split(" ")
    PA, NPA = find_PA_and_NPA(ck, attributes)
    prime_attributes = "".join(PA)

    for i, j in fd.items():
        if not i in ck_keys:
            if not j in prime_attributes:
                return False
    return True


# ----------- CLOSURE -----------            (Requirements : keys list , values list , attributes string)
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



# ---------- Candidate key ----------
def subsets(string):
    if string == []:
        return [[]]
    x = subsets(string[1:])
    return x + [[string[0]] + y for y in x]


def findCandidateKey(att, keys, values):
    subset = subsets(list(set(att)))
    superkeys = []
    candidatekeys = []
    for i in subset:
        closureSub = closure(keys, values, "".join(sorted(i)), -1)
        if len(closureSub) == len(att):
            superkeys.append("".join(sorted(i)))
    n = len(superkeys)
    extra = []
    for i in superkeys:
        for j in range(n):
            if set(i).issubset(list(superkeys[j])) and len(superkeys[j]) != len(i):
                extra.append(superkeys[j])
    candidatekeys = set(superkeys).difference(extra)
    return list(candidatekeys), superkeys



# ---------- Normalize to 2nd Normal Form ----------
def normalize_2nf(keys, values, candidatekeys, att):
    partial = []
    check = True
    for i in range(len(keys)):
        for j in candidatekeys:
            if set(keys[i]).issubset(set(j)) and len(keys[i]) != len(j):
                check = False
                partial.append(i)
                break
    if not check:
        relation = []
        str1 = ""
        for i in partial:
            relation.append(keys[i] + values[i])
            str1 += values[i]
        removeAtt = list(set(str1))
        str2 = att
        for i in removeAtt:
            str2 = str2.replace(i, "")
        relation.append(str2)
        return relation


# ---------- Normalize to 3nd Normal Form ----------
def normalize_3nf(cover, sk, ck, att):
    check = True
    partical = {}
    for i in cover:
        if i not in sk:
            for j in ck:
                if not set(cover[i]).issubset(j):
                    check = False
                    partical[i] = cover[i]
                    break
    if not check:
        str1 = att
        relation = []
        for i in partical:
            str1 = str1.replace(partical[i], '')
            relation.append(i + partical[i])
        relation.append(str1)
        return relation



# ---------- Minimal Cover ----------
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
