file = open('/Users/Tibo/Documents/python/numbers.txt')
#file = open('/Users/Tibo/Documents/python/mediantest.txt')



def file_iter(file):
	"""create an iterable: 
	take a file with one number per line
	and yield one number at each call"""
	for line in file:
		yield int(line.strip("\n"))

iterable = file_iter(file)

#print [next(iterable)]
#print [next(iterable)]
#print [next(iterable)]
#print [next(iterable)]

def heap_median(iterable):
	""" """ 
	import heapq

	high_heap = []
	low_heap = [-next(iterable)]
	sum = -low_heap[0]

	for number in iterable:
		if number > -low_heap[0]:
			heapq.heappush(high_heap, number )
		else:
			heapq.heappush(low_heap, -number)

		if len(low_heap) > len(high_heap) + 1:
			heapq.heappush(high_heap, -heapq.heappop(low_heap))

		elif len(high_heap) > len(low_heap):
			heapq.heappush(low_heap, -heapq.heappop(high_heap))
		print "median is", -low_heap[0]
		sum += -low_heap[0]
		print sum
	print high_heap
	print low_heap
	return sum % 10000

print heap_median(file_iter(file))
		