"""
This is not bubble sort, it's a likely selection sort
def bubble_sort(arr):
	size = len(arr)
	for i in xrange(size-1):
		for j in xrange(i+1,size):
			if arr[i] > arr[j]:
				arr[i] ,arr[j] = arr[j],arr[i]


if __name__ == '__main__':
	l1 = [4,1,8,2,7,6,3]
	l2 = [0,1,4,5,8,2,7,9]
	l3 = [9,2,5,3,5,5,6,2,1,8,9]
	
	print l1
	bubble_sort(l1)
	print l1
	print

	print l2
	bubble_sort(l2)
	print l2
	print
	
	print l3
	bubble_sort(l3)
	print l3
	print
"""				

def bubble_sort(arr):
	counter = 0
	size = len(arr)
	for i in xrange(size-1):
		is_swapp = False
		for j in xrange(size-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				is_swapp = True
			counter += 1
		print i, counter,arr
		
		if not is_swapp:
			print i
			break
				
if __name__ == '__main__':
	l1 = [4,1,8,2,7,7,6,3]
	l2 = [8,1,2,3,4,5,6,7]
	
	print 'original list:' + str(l1)
	bubble_sort(l1)
	print
	print 'original list:' + str(l2)
	bubble_sort(l2)