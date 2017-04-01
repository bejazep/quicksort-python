# Quicksort using list comprehension

# sorts list a between index values lo, hi
def quicksort(a,lo,hi):

	if lo < hi:
		p = partition(a,lo,hi)	# partitions the list
		quicksort(a,lo,p-1)		# quicksorts smaller lists
		quicksort(a,p+1,hi)		
		
# partitions the list at indexes lo, hi in list a
def partition(a,lo,hi):

	pivot = a[hi]				# pivot value is last in list
	i = lo - 1					# points to start of sublist
	for j in xrange(lo,hi):		# loops through sublist
		if a[j] <= pivot:		# if element is less than pivot
			i = i + 1			# 	imcrement pointer
			swap(a,i,j)			#	swap current element and pointer value
	swap(a,i+1,hi)				# swap the end value and largest element
	return i+1					# return the pointer location
	
# swaps the values at indexes n, m in list a	
def swap(a,n,m):

	temp = a[m]					# save value for m
	a[m] = a[n]
	a[n] = temp

# test values
# before:	[64, 23, 98, 3, 12, 54, 1, 34, 105, 42, 77]
# after:	[1, 3, 12, 23, 34, 42, 54, 64, 77, 98, 105]

a = [64,23,98,3,12,54,1,34,105,42,77]
print 'before:\t' + str(a)
quicksort(a,0,len(a)-1)
print 'after:\t' + str(a)
