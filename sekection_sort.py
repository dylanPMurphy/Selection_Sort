def selectionSort(input_array):
    min = inf
    sorted = 0
    for i in range(0,len(input_array)):
        if min>input_array[i]:
            min = input_array[i]