'''

Insertion sort is a sorting algorithm.

This implementation does an in place sort.

$ python3 insertionSort.py --list 30 1 421 -2
Array to sort: [30, 1, 421, -2]
Sorted Array: [-2, 1, 30, 421]

'''


def insertionSort(lst):
	for index in range(1, len(lst)):

		currentValue = lst[index]
		position = index

		while position > 0 and lst[position - 1] > currentValue:
			lst[position] = lst[position - 1]
			position -= 1
		lst[position] = currentValue


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
	insertionSort(args.list)
	print(f'Sorted Array: {args.list}')
