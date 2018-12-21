# Reference: https://www.geeksforgeeks.org/shellsort
#            https://blog.csdn.net/weixin_37818081/article/details/79202115
#            https://www.tutorialspoint.com/data_structures_algorithms/shell_sort_algorithm.htm
#            https://www.toptal.com/developers/sorting-algorithms/shell-sort

def shell_sort(arr):
    gap = len(arr)
    begin = 0
    end = gap - 1

    while gap > 1:  # until gap == 0
        gap = gap/3+1  # based on Knuth's formula
        for i in xrange(begin+gap, end+1):  # calculator sub list based on gap, each loop for one sub list
            if arr[i] < arr[i-gap]:  # if right < left then do one insert sort
                for j in xrange(i-gap, -1, -gap):  # for i to ( i-gap, i-2gap ... ) to run insertion sort
                    if arr[j+gap] < arr[j]:
                        arr[j+gap], arr[j] = arr[j], arr[j+gap] # swap
        print '%d:%s' %(gap, arr)

if __name__ == '__main__':
    l1 = [1,2,3,4,5,6,7]
    l2 = [7,6,5,4,3,2,1]
    l3 = [3,8,3,5,8,5,2]

    print l1
    shell_sort(l1)
    print l1
    print

    print l2
    shell_sort(l2)
    print l2
    print

    print l3
    shell_sort(l3)
    print l3
    print


                    
     