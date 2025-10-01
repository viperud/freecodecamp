import numpy as np

def calculate(mylist):
    #Checking size of the list
    if len(mylist) != 9:
        raise ValueError("List must contain nine numbers.")

    #Converting size 9 list to 3x3 array in numpy
    nparray = np.array(mylist).reshape(3, 3)

    #Output dictionary
    output = {}

    #Calculating and adding mean to output dictionary
    mean = []
    mean.append(nparray.mean(axis = 0).tolist())
    mean.append(nparray.mean(axis = 1).tolist())
    mean.append(nparray.mean().tolist())
    output['mean'] = mean

    #Calculating and adding variance to output dictionary
    var = []
    var.append(nparray.var(axis = 0).tolist())
    var.append(nparray.var(axis = 1).tolist())
    var.append(nparray.var().tolist())
    output['variance'] = var

    #Calculating and adding Standard deviation to output dictionary
    std = []
    std.append(nparray.std(axis = 0).tolist())
    std.append(nparray.std(axis = 1).tolist())
    std.append(nparray.std().tolist())
    output['standard deviation'] = std

    #Calculating and adding maximum value to output dictionary
    max = []
    max.append(nparray.max(axis = 0).tolist())
    max.append(nparray.max(axis = 1).tolist())
    max.append(nparray.max().tolist())
    output['max'] = max

    #Calculating and adding minimum value to output dictionary
    min = []
    min.append(nparray.min(axis = 0).tolist())
    min.append(nparray.min(axis = 1).tolist())
    min.append(nparray.min().tolist())
    output['min'] = min

    #Calculating and adding sum to output dictionary
    sum = []
    sum.append(nparray.sum(axis = 0).tolist())
    sum.append(nparray.sum(axis = 1).tolist())
    sum.append(nparray.sum().tolist())
    output['sum'] = sum

    return output

results = calculate([0,1,2,3,4,5,6,7,8])
print(results)