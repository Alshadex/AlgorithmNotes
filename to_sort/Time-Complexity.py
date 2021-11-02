'''
Complexity
'''

''' Permutations Approach '''
# Start with our word and find all of its permutations

# Step 1: Generate all permutations
# Step 2: Check whether each word is in the English wordlist. Search using Binary Search.
# how fast? n! x w. Where n is the length of the word and w is the number of words in the wordlist.

''' Signature Approach '''
# Start with the word, and rearrange its letters into alphabetical order.
# eg. from "march" we get "achmr".
# We'll this alphabetical version the signature of a word.

# Step 1: Find the signature.
# Step 2: Search the wordlist; find signature of each word in the wordlist, if the signature matches then it's an anagram.
# how fast? total work is w.

#Example, How fast is this function?:
def max_segment_sum(L):
	''' Return maximum segment sum of L:'''
	max_so_far = 0
	for lower in range(len(L)):
		for upper in range(lower, len(L)):
			sum = 0
			for i in range(lower, upper + 1):
				sum = sum + L[i]
			max_so_far = max(max_so_far, sum)
	return max_so_far
'''
How many steps does it take?
2 steps outside of the loops; first assignment statement and return.

Let's compute the number of times this occurs: sum = sum + L[i]

The lower loop runs n times; n is length of the list.
For each iteration of the lower loop,the upper loop runs at most n times.
For each iteration of upper, the i loop runs at most n times.
So we have n * at most n * at most n... that's at most n^3

sum = 0 runs n^2 times

max_so_far = max(max_so_far, sum) runs n^2 time as well.

total = 2 + 2n^2 + n^3

Does the 2 matter? 2 steps...

Suppose n is 10000
n^3 + 2n^2 = 1.0002 * 10^12
2 steps doesn't matte; ignore it.

n^3 + 2n^2

As n increases, 2n^2 is very small compared to n^3.

Types of Algorithm Efficiencies (fastest to slowest):
 - O(1) Constant-time.
 - O(log(n)) Base 2
 - Linear-Time. O(n)
 - O(n log(n))
 - O(n^2)
 - O(n^3)
 - O(2^n)
 As soon as we get to a nonpolynomial, like 2^n or n! or n^n, 
 this isn't useful in practice unless the problem size is really small.

 Slow Sorts:
 - Selection Sort
 - Insertion Sort
 - Bubble Sort

 - Quicksort:
Worst-Case: O(n^2)
Average-Case: O(nlog(n))
How does quicksort work?
[2,1,5,4,3,    8,6,9,7,10]. This is a partition
[8,1,3,9,10,    5,7,6,4,2]. This is not a partition

What a partition does for you is give you two smaller subproblems to solve.
recursion

steps:
1. Partition the list. That gives us two subproblems, left and right.
2. Recursively call the quicksort on the left subproblem.
3. Recursively call quicksort on the right subproblem.

How do you partition?
1. It's very challenging to partition the list perfectly in half.
To do the partition perfectly, we require the median. But computing the median is too much work.
We're going to settle for imperfect partitions. We don't care if its a perfect split or not.

2. Partitioning has to be very fast. This is why we're not goinig to use median.

Overall goal of partitioning:
Quickly get a reasonable split of elements into two partitions.
'''
def partition(lst, left, right, pivot):
	'''(list, int, int, int) -> int
	returns i which is the index at where the list is partitioned.
	'''
	i = left
	j = left
	while j <= right:
		if lst[j] < pivot:
			lst[i], lst[j] = lst[j], lst[i] # This type of code does a swap
			i += 1
		j += 1
	return i

'''
HOw do you choose a pviot element?
Reminder: YOu want the split to be as close as to 50-50 as possible.
'''