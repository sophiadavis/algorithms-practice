import random

def quick_sort(int_array):
    if len(int_array) == 0:
        return []
    if len(int_array) == 1:
        return int_array
    else:
        partitioned, pivot_index = partition(int_array)
        return quick_sort(partitioned[:pivot_index]) + [int_array[pivot_index]] + quick_sort(partitioned[(pivot_index + 1):])

def partition(int_array):
    # pivot_index = int((len(int_array) - 1) / 2)
    pivot_index = random.randint(0, len(int_array) - 1)
    pivot = int_array[pivot_index]

    swap(int_array, pivot_index, -1)
    store_index = 0

    for i in range(len(int_array) - 1):
        if int_array[i] < pivot:
            swap(int_array, i, store_index)
            store_index += 1
    swap(int_array, store_index, -1)
    return int_array, store_index

def quick_sort_in_place(int_array, low_index = 0, high_index = None):

    if high_index == None:
        high_index = len(int_array) - 1

    if low_index < high_index:
        pivot_index = partition_in_place(int_array, low_index, high_index)
        quick_sort_in_place(int_array, low_index, pivot_index - 1)
        quick_sort_in_place(int_array, pivot_index + 1, high_index)
    return int_array

def partition_in_place(int_array, low_index, high_index):
    # pivot_index = int((high_index + low_index) / 2)
    pivot_index = random.randint(low_index, high_index)
    pivot = int_array[pivot_index]

    swap(int_array, pivot_index, high_index)

    store_index = low_index

    for i in range(low_index, high_index):
        if int_array[i] <= pivot:
            swap(int_array, i, store_index)
            store_index += 1

    swap(int_array, store_index, high_index)

    return store_index

def swap(l, index1, index2):
    temp = l[index1]
    l[index1] = l[index2]
    l[index2] = temp

if __name__ == "__main__":
    # from pudb import set_trace; set_trace()

    # eight_element_list = [8, 0, 12, 2, 5, 7, 3, 10]
    # print eight_element_list
    # print quick_sort(eight_element_list)
    # print
    #
    # odd_number_element_list = [-10, 5, 2, 7, 6, 4.4, 3.75]
    # print odd_number_element_list
    # print quick_sort(odd_number_element_list)
    # print
    #
    # list_w_dups = [1, 234234, 2]#, 3, 3, 4, 4, 0]
    # print list_w_dups
    # print quick_sort(list_w_dups)
    # print
    #
    # list_w_dups = [1, 4, 6]#, 3, 3, 4, 4, 0]
    # print list_w_dups
    # print quick_sort(list_w_dups)
    # print
    #
    # list_w_dups = [5, 5, 1]#, 3, 3, 4, 4, 0]
    # print list_w_dups
    # print quick_sort(list_w_dups)
    # print
    #
    # list_w_dups = [8, 8, 3]#, 3, 3, 4, 4, 0]
    # print list_w_dups
    # print quick_sort(list_w_dups)
    # print
    #
    #
    # list_w_dups = [8, 8, 3, 3, 3, 4, 4, 0]
    # print list_w_dups
    # print quick_sort(list_w_dups)
    # print
    #
    # sorted_list = [1, 1, 3, 3, 6, 6, 9, 9, 1000, 1000, 5000, 5000, 100000000]
    # print sorted_list
    # print quick_sort(sorted_list)
    # print
    #
    # rev_sorted_list = [10, 9, 8, 7, 6, 0, -5, -10]
    # print rev_sorted_list
    # print quick_sort(rev_sorted_list)
    # print



    eight_element_list = [8, 0, 12, 2, 5, 7, 3, 10]
    print eight_element_list
    print quick_sort_in_place(eight_element_list)
    print

    odd_number_element_list = [-10, 5, 2, 7, 6, 4.4, 3.75]
    print odd_number_element_list
    print quick_sort_in_place(odd_number_element_list)
    print

    list_w_dups = [1, 234234, 2]#, 3, 3, 4, 4, 0]
    print list_w_dups
    print quick_sort_in_place(list_w_dups)
    print

    list_w_dups = [1, 4, 6]#, 3, 3, 4, 4, 0]
    print list_w_dups
    print quick_sort_in_place(list_w_dups)
    print

    list_w_dups = [5, 5, 1]#, 3, 3, 4, 4, 0]
    print list_w_dups
    print quick_sort_in_place(list_w_dups)
    print

    list_w_dups = [8, 8, 3]#, 3, 3, 4, 4, 0]
    print list_w_dups
    print quick_sort_in_place(list_w_dups)
    print

    sorted_list = [1, 1, 3, 3, 6, 6, 9, 9, 1000, 1000, 5000, 5000, 100000000]
    print sorted_list
    print quick_sort_in_place(sorted_list)
    print

    # inf rec
    rev_sorted_list = [10, 9, 8, 7, 6, 0, -5, -10]
    print rev_sorted_list
    print quick_sort_in_place(rev_sorted_list)
    print
