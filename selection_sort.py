def selectionSort(input_array):
    for i in range(0,len(input_array)):
        min = i
        for j in range(i,len(input_array)):
            if input_array[min]>input_array[j]:
                min = j
        input_array[i], input_array[min] = input_array[min], input_array[i]
    return input_array
print(selectionSort([23,4,12,34,23,45,653,463,123,4,2435,36,57,45,324,23,63,6,3,53,7,45,74,8,567,465,3,5,235]))