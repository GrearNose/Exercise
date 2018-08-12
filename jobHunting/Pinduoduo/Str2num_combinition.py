"""
Problem Description
Given a digit string, figure out how many ways
to divide it into two valid numbers and optionally
add radix points to them. A a number is if it does
not start with 0 except that it has only decimal part,
in which case it can at most have one 0; and its decimal
part does not end with zero.
"""

# s = input()
def com_num(s):
	num = []
	if len(s) == 1:
		return [s]
	if s[0] != '0':
		num.append(s)
	# print('s:', s)
	for i in range(1,len(s)):
		s1 = s[:i]
		s2 = s[i:]
		# print('s1,s2:', s1, s2)
		if len(s1) > 1 and s[0] == '0' : continue
		if s2[-1] == '0': continue
		tmp = s[:i] +'.' + s[i:]
		num.append(tmp)
	return num

# s = '00011'
# s = '123'
# s = '00103'
# s = '1201'
# s = '0102'
s = '010'
# s = input()
pairs = set()
for i in range(1,len(s)):
	s1 = s[:i]
	s2 = s[i:]
	# print('s1:',s1, 's2:',s2)
	if len(s1) > 1 and all([c == '0' for c in s1]): continue
	if len(s2) > 1 and all([c == '0' for c in s2]): continue
	num1 = com_num(s1)
	num2 = com_num(s2)
	# print('num1:',num1, 'num2:',num2)
	if len(num1) == 0: continue
	if len(num2) == 0: continue
	for n1 in num1:
		for n2 in num2:
			pairs.add((n1,n2))
			# print(n1,n2)
			# pass

# print(pairs)
print(len(pairs))
