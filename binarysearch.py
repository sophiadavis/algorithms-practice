import quicksort

def binary_search(lst, key):
    l = len(lst)

    if l == 0:
        print "Not there."
        return False

    middle = int(l/2)
    median = lst[middle]

    if key == median:
        print "Found it!"
        return True
    elif l < 2:
        print "Not there."
        return False
    elif key > median:
        return binary_search(lst[middle:], key)
    else:
        return binary_search(lst[:middle], key)

if __name__ == "__main__":
    easy = [1,2,3,4,5,6,7,8]
    print easy
    for item in easy:
        print binary_search(easy, item)
    print
    print binary_search(easy, 0)
    print binary_search(easy, 100)

    print "\n----------------\n"

    even_length = [8,5,6,2,4,-10,3,100]
    even_length = quicksort.quick_sort(even_length)
    print even_length
    for item in even_length:
        print binary_search(even_length, item)
    print
    print binary_search(even_length, 0)
    print binary_search(even_length, 1000)

    print "\n----------------\n"

    odd_length = [2.3, 1.1, 6.5, 3.2, 9.9]
    odd_length = quicksort.quick_sort(odd_length)
    print odd_length
    for item in odd_length:
        print binary_search(odd_length, item)
    print
    print binary_search(odd_length, 0)
    print binary_search(odd_length, 1000)

    print "\n----------------\n"

    no_elements = []
    no_elements = quicksort.quick_sort(no_elements)
    print no_elements
    for item in no_elements:
        print binary_search(no_elements, item)
    print
    print binary_search(no_elements, 0)
    print binary_search(no_elements, 1000)

    print "\n----------------\n"

    one_elements = [3]
    one_elements = quicksort.quick_sort(one_elements)
    print one_elements
    for item in one_elements:
        print binary_search(one_elements, item)
    print
    print binary_search(one_elements, 0)
    print binary_search(one_elements, 1000)

    print "\n----------------\n"

    two_elements = [3, 0]
    two_elements = quicksort.quick_sort(two_elements)
    print two_elements
    for item in two_elements:
        print binary_search(two_elements, item)
    print
    print binary_search(two_elements, 2)
    print binary_search(two_elements, 1000)
