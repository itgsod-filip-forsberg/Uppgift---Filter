def filter(array, value):
    return [i for i in array if i == value]

def exclude(array, value):
    return [i for i in array if i != value]

def unique(array):
    unique_list = []
    for i in array:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


