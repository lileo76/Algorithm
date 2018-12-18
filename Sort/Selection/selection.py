# Reference: http://www.algolist.net/Algorithms/Sorting/Selection_sort
# divide two parts: sorted, and unsorted, first sorted is empty, unsorted is all array
# each step to select minmine one from unsorted and append to sorted one, until unsorted is empty

def selection_sort(arr):
    size = len(arr)
    for i in xrange(size-1):  # outer looper from 0 to n-1, due to after looper the last one is the maxmine one
        index = i
        for j in xrange(i, size):
            if arr[j] < arr[index]:
                index = j

        if i != index:  # if min index is not same as i, the swap else means i is the min
            arr[i],arr[index] = arr[index], arr[i]


if __name__ == '__main__':
    l1 = [1,2,3,4,5,6,7]
    l2 = [7,6,5,4,3,2,1]
    l3 = [3,8,3,5,8,5,2]

    print l1
    selection_sort(l1)
    print l1
    print

    print l2
    selection_sort(l2)
    print l2
    print

    print l3
    selection_sort(l3)
    print l3
    print

