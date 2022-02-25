'''

Reverse divide and conqure is a recursive algorithm.

$ python3 reverse_dc.py --list 14 2 3 40 23
Array to reverse: [14, 2, 3, 40, 23]
reversed: [2, 3, 14, 23, 40]

'''

def reverse_dc(lst):
	if len(lst) <= 1:
		return lst[:]
	mid = len(lst) // 2
	left = lst[:mid]
	right = lst[mid:]
	left_s = reverse_dc(left)
	right_s = reverse_dc(right)
	lst = []
	lst.extend(right_s)
	lst.extend(left_s)
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

	print(f'Array to reverse: {args.list}')
	Sorted = reverse_dc(args.list)
	print(f'reversed Array: {Sorted}')
