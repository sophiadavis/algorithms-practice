def insertion_sort(int_array):
    # Advantages (thanks wiki!)
    for i in range(len(int_array)):
        j = i
        while j > 0 and int_array[j - 1] > int_array[j]:
            # print "--swapping %i and %i" % (int_array[j - 1], int_array[j])
            int_array[j], int_array[j - 1] = int_array[j - 1], int_array[j]
            j -= 1
        print "---- %s" % str(int_array)
    return int_array

def bubble_sort(int_array):
    while True:
        swapped = False
        print "starting with %s" % str(int_array)
        for i in range(1, len(int_array)):
            print "--comparing %i and %i" % (int_array[i], int_array[i - 1])
            if int_array[i] <= int_array[i - 1]:
                print "--swapping"
                int_array[i], int_array[i - 1] = int_array[i - 1], int_array[i]
                swapped = True
            print "--%s" % str(int_array)
        if not swapped:
            return int_array

def selection_sort(int_array):
    smallest_unsorted_index = 0
    last_index = len(int_array)
    print " --- Sorting..."
    while smallest_unsorted_index < last_index:
        print "     %s -- %s" % (str(int_array[:smallest_unsorted_index]), str(int_array[smallest_unsorted_index:]))
        current_min = int_array[smallest_unsorted_index]
        swap_index = None
        for i in range(smallest_unsorted_index, last_index):
            if int_array[i] < current_min:
                current_min = int_array[i]
                swap_index = i
        if swap_index:
            int_array[smallest_unsorted_index], int_array[swap_index] = int_array[swap_index], int_array[smallest_unsorted_index]
        smallest_unsorted_index += 1
    return int_array



if __name__ == "__main__":
    # # from pudb import set_trace; set_trace()
    # eight_element_list = [8, 0, 12, 2, 5, 7, 3, 10]
    # print eight_element_list
    # print insertion_sort(eight_element_list)
    # print
    #
    # odd_number_element_list = [-10, 5, 2, 7, 6, 4.4, 3.75]
    # print odd_number_element_list
    # print insertion_sort(odd_number_element_list)
    # print
    #
    # list_w_dups = [8, 8, 3, 3, 3, 4, 4, 0]
    # print list_w_dups
    # print insertion_sort(list_w_dups)
    # print
    #
    # sorted_list = [1, 1, 3, 3, 6, 6, 9, 9, 1000, 1000, 5000, 5000, 100000000]
    # print sorted_list
    # print insertion_sort(sorted_list)
    # print
    #
    # rev_sorted_list = [10, 9, 8, 7, 6, 0, -5, -10]
    # print rev_sorted_list
    # print insertion_sort(rev_sorted_list)
    # print
    #
    # wiki_ex = [6, 5, 3, 1, 8, 7, 2, 4]
    # print wiki_ex
    # print insertion_sort(wiki_ex)
    # print

############# bubble sort tests

    # wiki_ex = [6, 5, 3, 1, 8, 7, 2, 4]
    # print wiki_ex
    # print bubble_sort(wiki_ex)
    # print

############# selection sort tests

    # from pudb import set_trace; set_trace()
    eight_element_list = [8, 0, 12, 2, 5, 7, 3, 10]
    print eight_element_list
    print selection_sort(eight_element_list)
    print

    odd_number_element_list = [-10, 5, 2, 7, 6, 4.4, 3.75]
    print odd_number_element_list
    print selection_sort(odd_number_element_list)
    print

    list_w_dups = [8, 8, 3, 3, 3, 4, 4, 0]
    print list_w_dups
    print selection_sort(list_w_dups)
    print

    sorted_list = [1, 1, 3, 3, 6, 6, 9, 9, 1000, 1000, 5000, 5000, 100000000]
    print sorted_list
    print selection_sort(sorted_list)
    print

    rev_sorted_list = [10, 9, 8, 7, 6, 0, -5, -10]
    print rev_sorted_list
    print selection_sort(rev_sorted_list)
    print

    wiki_ex = [6, 5, 3, 1, 8, 7, 2, 4]
    print wiki_ex
    print selection_sort(wiki_ex)
    print

    wiki_ex = []
    print wiki_ex
    print selection_sort(wiki_ex)
    print

    wiki_ex = [-2]
    print wiki_ex
    print selection_sort(wiki_ex)
    print
