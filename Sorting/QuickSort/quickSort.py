'''
Quicksort is a sorting algorithm.

This implementation does an in place sort.

$ python3 quickSort.py --list 14 2 3 40 23
Array to sort: [14, 2, 3, 40, 23]
Sorted Array: [2, 3, 14, 23, 40]

'''

def quickSort(lst, left, right):
	'''
	args:
		lst: list to sort in place
		left: index of most left element in lst
		right: index of most right element in lst
	'''
	if left < right:

		pivot = lst[right]
		i = partition(lst, left, right, pivot)
		lst[i], lst[right] = lst[right], lst[i]
		quickSort(lst, left, i - 1)
		quickSort(lst, i + 1, right)

def partition(lst, left, right, pivot):
	i = left
	j = left
	while j <= right:
		if lst[j] < pivot:
			lst[i], lst[j] = lst[j], lst[i]
			i += 1
		j += 1
	return i


if __name__ == "__main__":
	import argparse
	CLI=argparse.ArgumentParser()
	CLI.add_argument(
		"--list",
		nargs="*",
		type=int,
		default=[3,2,1]
	)
	args = CLI.parse_args()

	print(f'Array to sort: {args.list}')
	quickSort(args.list, 0, len(args.list)-1)
	print(f'Sorted Array: {args.list}')
