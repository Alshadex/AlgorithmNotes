'''
Selection sort is a sorting algorithm

This implementation does an in place sort.

$ python3 selectionSort.py --list 32 1 24 -4 12
Array to sort: [32, 1, 24, -4, 12]
Sorted Array: [-4, 1, 12, 24, 32]

'''


def selectionSort(lst):
	for x in range(len(lst)-1, 0, -1):
		pos = 0
		for location in range(1, x + 1):
			if lst[location] > lst[pos]:
				pos = location
		lst[x], lst[pos] = lst[pos], lst[x]

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
	selectionSort(args.list)
	print(f'Sorted Array: {args.list}')
