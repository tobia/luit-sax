#!/usr/bin/python

from math import log, floor, ceil

sax_01 = 0x236e

sax_10_1a = [
	0x250c, 0x252c, 0x2510, 0x251c, 0x253c, 0x2524, 0x2514, 0x2534,
	0x2518, 0x2502, 0x2500
]

sax_a0_ff = [
	0, 0xa8, 0xaf, 0, 0x2264, 0, 0x2265, 0,
	0x2260, 0x2228, 0, 0xd7, 0x236a, 0x2360, 0x2235, 0x233f,
	0x2372, 0xa1, 0x20ac, 0xa3, 0xa5, 0, 0xac, 0,
	0, 0x2371, 0, 0x233b, 0x2342, 0x2261, 0x2337, 0xbf,
	0, 0x237a, 0x22a5, 0x2229, 0x230a, 0x220a, 0, 0x2207,
	0x2206, 0x2373, 0x2218, 0, 0x2395, 0x7c, 0x22a4, 0x25cb,
	0, 0, 0x2374, 0x2308, 0, 0x2193, 0x222a, 0x2375,
	0x2283, 0x2191, 0x2282, 0x22a2, 0x2340, 0x22a3, 0, 0xf7,
	0x2336, 0x2296, 0x234e, 0x235d, 0, 0x2377, 0x236b, 0x2352,
	0x234b, 0x2378, 0x2364, 0, 0x235e, 0, 0x2355, 0x2365,
	0x235f, 0, 0, 0, 0x2349, 0, 0x2363, 0x233d,
	0, 0, 0xa2, 0x2190, 0x2359, 0x2192, 0x22c4, 0
]

uni2sax = {sax_01: 1}
for i, u in enumerate(sax_10_1a):
	uni2sax[u] = i + 0x10
for i, u in enumerate(sax_a0_ff):
	if u != 0:
		uni2sax[u] = i + 0xa0

def make_tree(lst):
	"""Return a binary search tree for the ordered list of integers lst.
	This is either None or a tuple (key, left, right)
	The tree is filled in such a way that its breadth-first array representation is space-optimal.
	"""
	if not lst:
		return None
	n = len(lst)
	sub_n = (n - 1) / 2. # avg. nodes in each subtree
	# a complete tree of height h has n nodes: n = 2^(h+1) - 1  <=>  h = log_2(n + 1) - 1
	sub_h = log(sub_n + 1, 2) - 1 # avg. height in each subtree
	floor_n = 2 ** (floor(sub_h) + 1) - 1 # nodes in a complete tree of height floor(sub_h)
	ceil_n = 2 ** (ceil(sub_h) + 1) - 1 # nodes in a complete tree of height ceil(sub_h)
	if n <= 1 + ceil_n + floor_n:
		# bottom level stops in left subtree: pivot is just before the rightmost floor_n
		pivot = int(n - floor_n - 1)
	else:
		# bottom level stops in right subtree: pivot is just after the leftmost ceil_n
		pivot = int(ceil_n)
	return (lst[pivot], make_tree(lst[:pivot]), make_tree(lst[pivot + 1:]))

uni = uni2sax.keys()
uni.sort()
tree = make_tree(uni)

# convert linked tree into breadth-first array representation
tree_array = []
queue = [tree]
end = False
while True:
	try:
		n = queue.pop(0)
	except IndexError:
		break
	tree_array.append(n[0])
	for sub in n[1:]:
		if sub is None:
			end = True
		elif end:
			raise Exception('Tree is not left-filled')
		else:
			queue.append(sub)

print len(tree_array)
for i, u in enumerate(tree_array):
	print '0x%06x,' % ((u << 8) | uni2sax[u],),
	if i % 7 == 6:
		print
