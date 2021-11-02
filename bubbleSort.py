'''

Bubble Sort is a sorting algorithm. O(n^2)

$ python3 bubbleSort.py --list 4 1 2 4 123 
Array to sort: [4, 1, 2, 4, 123]
Sorted Array: [1, 2, 4, 4, 123]

'''


def bubbleSort(lst):
	for x in range(len(lst) -1, 0, -1):
		for i in range(x):
			if lst[i] > lst[i + 1]:
				lst[i], lst[i + 1] = lst[i + 1], lst[i]


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
	bubbleSort(args.list)
	print(f'Sorted Array: {args.list}')
