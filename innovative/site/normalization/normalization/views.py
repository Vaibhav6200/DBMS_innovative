from django.shortcuts import render
import pandas as pd
import numpy as np


def check_1_NF(data):
    df = pd.DataFrame(data)
    lens = list(map(len, df['Subjects'].values))
    n = 0
    for i in lens:
        if i > 1:
            print("Not in 1st NF")
            n = int(input("Do You Want to convert Table in 1st NF (1/0) : "))
            break
    if (n == 1):
        res = pd.DataFrame({
            'Name': np.repeat(df['Name'], lens),
            'Subject': np.concatenate(df['Subjects'].values)
        })
        return res

def check_1NF():
    data = {
        'Name': ['David', 'Glenn', 'Steve'],
        'Subjects': [['English', 'Math'], ['Math'], ['Science', 'English']]
    }
    result = check_1_NF(data)
    print(result)


def index(request):
    # if request.method == 'POST':
    #     key1 = request.POST['key1']
    #     key2 = request.POST['key2']
    #     value1 = request.POST['value1']
    #     value2 = request.POST['value2']

    return render(request, 'index.html')
