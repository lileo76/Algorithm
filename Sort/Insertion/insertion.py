# Reference: http://www.algolist.net/Algorithms/Sorting/Insertion_sort
#
def insert(sorted_list, right, value):
    """
        sorted_list: sorted list
        right: the right index of sorted list
        value: need to be inserted to proper postion to sorted list
    """
    # sorted_list[right+1] = sorted_list[right] 
    for i in xrange(right, -1, -1): # for downloop from right to 0
        if sorted_list[i] > value:
            sorted_list[i+1] = sorted_list[i]  # shift
            if i == 0:  # if each element of soreted list is bigger than value, then insert postion is 0
                sorted_list[0] = value
        else:
            sorted_list[i+1] = value # find the insert postion
            break

def insertion_sort(unsorted_list):
    for i in xrange(1, len(unsorted_list)):  # for loop from 2 to end, and sorted list init is first element
        if unsorted_list[i] < unsorted_list[i-1]: # need to be insert unsorted_list[i] to sorted_list
            insert(unsorted_list, i-1, unsorted_list[i])

        print '%s: %s' %(str(i), unsorted_list[0:i+1])


if __name__ == '__main__':
    l1 = [1,2,3,4,5,6,7]
    l2 = [7,6,5,4,3,2,1]
    l3 = [3,8,3,5,8,5,2]

    print l1
    insertion_sort(l1)
    print l1
    print

    print l2
    insertion_sort(l2)
    print l2
    print

    print l3
    insertion_sort(l3)
    print l3
    print
