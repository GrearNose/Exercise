from random import randint
def min_adjust_time(s):
	"""
	Given a str consisting of 'b' and 'g', a char can only swap with the
	two adjacent chars, figure out the min swap time to sort out the string
	such that 'b's cluster in one end of the string and 'g's the other end.
	"""
	s = s.lower()
	assert all([c in 'bg' for c in s])
	swap_b,swap_g,ln_b,ln_g,ix = 0,0,0,0,0
	for c in s:
		if 'b' == c:
			swap_b += ix-ln_b # swapping time of the current char 'b'
			ln_b += 1 # length of the substr of 'b'
		else:
			swap_g += ix-ln_g
			ln_g += 1
		ix += 1
	return min(swap_b,swap_g)

def test():
	# s = input()
	ln = 10
	str_base = 'bg'
	s = ''
	for _ in range(ln):
		i = randint(0,len(str_base)-1)
		s += str_base[i]
	print(s,min_adjust_time(s))

if __name__ == '__main__':
	test()

