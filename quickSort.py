# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot


def partition(bucket, low, high):
	p = (low-1)		 # index of smaller element
	pivot = bucket[high]	 # pivot
  
	for q in range(low, high):

		# If current element is smaller than or
		# equal to pivot
		
		if ((bucket[q][0] < pivot[0]) or (bucket[q][0] == pivot[0] and bucket[q][1] <= pivot[1])):
			
			# increment index of smaller element
			p += 1
			bucket[p], bucket[q] = bucket[q], bucket[p]

	bucket[p+1], bucket[high] = bucket[high], bucket[p+1]
	return (p+1)

# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index

# Function to do Quick sort

# Fungsi quickSort dengan menggunakan rekursi
def quickSort(bucket, low, high):
	if len(bucket) == 1:
		return bucket
	if low < high:
		i = partition(bucket, low, high)
    # memanggil quickSort untuk kedua partisi
		quickSort(bucket, low, i-1)
		quickSort(bucket, i+1, high)

'''
# Driver code to test above
arr = [10, 7, 8, 9, 1, 5,5,2,25,64,8,23,2,57,23,45,8,3,2,6,67,24,2]
arr1 = [[1,1], [1,2], [3,3], [10,9], [-1,0]]
arr = [[ 4.9 , 2.5 ],[ 5.6 , 2.8 ],[ 5.6 , 2.8 ],[ 5.6 , 2.8 ],[ 5.8 , 2.7 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.6 , 2.8 ],[ 5.6 , 2.8 ],[ 5.8 , 2.7 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.6 , 2.8 ],[ 5.6 , 2.8 ],[ 5.8 , 2.7 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.6 , 2.8 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.6 , 2.8 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.8 , 2.7 ],[ 5.9 , 3.0 ],[ 5.9 , 3.0 ],[ 5.9 , 3.0 ],[ 5.9 , 3.0 ],[ 5.9 , 3.0 ],[ 5.9 , 3.0 ],[ 5.9 , 3.0 ],[ 5.9 , 3.0 ]]

n = len(arr)
quickSort(arr, 0, n-1)
print("Sorted array is:")
for i in range(n):
	print(arr[i])
'''