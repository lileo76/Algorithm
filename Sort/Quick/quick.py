def partition(left, right, arr):
	pivot = arr[left]
	i = left + 1
	j = right
	
	while True:
		while (i < j and arr[i] <= pivot):
			i += 1
		
		while (left < j and arr[j] >= pivot):
		    j -= 1
		
		if (i >= j):
			break
			
		arr[i], arr[j] = arr[j], arr[i]	
	
	arr[left], arr[j] = arr[j], arr[left]
	return j

def random_partiton(left, right, arr):
	from random import randint
	i = randint(left, right)
	arr[left], arr[i] = arr[i], arr[left]
	
	return partition(left, right, arr)
	
def quick_sort(left, right, arr):
	if left < right:
		# center = partition(left, right, arr)
		center = random_partiton(left, right, arr)
		quick_sort(left, center-1, arr)
		quick_sort(center+1, right, arr)
		
if __name__ == '__main__':
	l1 = [4,1,8,2,7,6,3]
	l2 = [0,1,4,5,8,2,7,9]
	l3 = [9,2,5,3,5,5,6,2,1,8,9]
	
	print l1
	quick_sort(0, len(l1)-1, l1)
	print l1
	print

	print l2
	quick_sort(0, len(l2)-1, l2)
	print l2
	print
	
	print l3
	quick_sort(0, len(l3)-1, l3)
	print l3
	print
