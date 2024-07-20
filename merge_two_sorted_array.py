def merge_sorted_arrays(array1, array2):
    merged_array = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            merged_array.append(array1[i])
            i += 1
        else:
            merged_array.append(array2[j])
            j += 1

    while i < len(array1):
        merged_array.append(array1[i])
        i += 1

    while j < len(array2):
        merged_array.append(array2[j])
        j += 1

    return merged_array

def main():
    array1 = list(map(int, input("Enter first array: ").split()))
    array2 = list(map(int, input("Enter second array: ").split()))
    merged_array = merge_sorted_arrays(array1, array2)
    print(merged_array)
main()
