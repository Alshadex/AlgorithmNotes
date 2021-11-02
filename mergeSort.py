'''

Merge Sort is a divide and conqure sorting algorithm.

$ python3 mergeSort.py --list 14 2 3 40 23
Array to sort: [14, 2, 3, 40, 23]
Sorted Array: [2, 3, 14, 23, 40]

'''

def mergeSort(lst):
	if len(lst) <= 1:
		return lst[:]
	mid = len(lst) // 2
	left = lst[:mid]
	right = lst[mid:]
	left_s = mergeSort(left)
	right_s = mergeSort(right)
	return merge(left_s, right_s)

def merge(lst1, lst2):
	lst = []
	i = 0
	j = 0
	while i < len(lst1) and j < len(lst2):
		if lst1[i] < lst2[j]:
			lst.append(lst1[i])
			i += 1
		else:
			lst.append(lst2[j])
			j += 1
	lst.extend(lst1[i:])
	lst.extend(lst2[j:])
	return lst


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
	Sorted = mergeSort(args.list)
	print(f'Sorted Array: {Sorted}')
