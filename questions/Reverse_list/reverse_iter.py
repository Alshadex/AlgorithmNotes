'''

Reverse loop algorithm.

$ python3 reverse_iter.py --list 14 2 3 40 23
Array to reverse: [14, 2, 3, 40, 23]
reversed: [2, 3, 14, 23, 40]

'''

def reverse_iter(lst):
    if len(lst) <= 1:
        return lst[:]
    res = []
    i = len(lst)-1
    while i >= 0:
        res.append(lst[i])
        i -= 1
    return res


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
	Sorted = reverse_iter(args.list)
	print(f'reversed Array: {Sorted}')
