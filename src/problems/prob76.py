# # 2
# 2
# 1 + 1
#
# # 3
# 3
# 2 + 1
#
# 1 + 1 + 1
#
# # 4
# 4
# 3 + 1
# 2 + 2
#
# 2 + 1 + 1
#
# 1 + 1 + 1 + 1
#
#
# # 5
# 5
#
# 4 + 1
# 3 + 2
#
# 3 + 1 + 1
# 2 + 2 + 1
#
# 2 + 1 + 1 + 1
#
# 1 + 1 + 1 + 1 + 1
#
#
# # 6
# 6
#
# 5 + 1
# 4 + 2
# 3 + 3
#
# 4 + 1 + 1
# 3 + 2 + 1
# 2 + 2 + 2
#
# 3 + 1 + 1 + 1
# 2 + 2 + 1 + 1
#
# 2 + 1 + 1 + 1 + 1
#
# 1 + 1 + 1 + 1 + 1 + 1
#
#
# # 7
# 6 + 1
# 5 + 2
# 4 + 3
#
# 5 + 1 + 1
# 4 + 2 + 1
# 3 + 3 + 1
# 3 + 2 + 2
#
# 4 + 1 + 1 + 1
# 3 + 2 + 1 + 1
# 2 + 2 + 2 + 1
#
# 3 + 1 + 1 + 1 + 1
# 2 + 2 + 1 + 1 + 1
#
# 2 + 1 + 1 + 1 + 1 + 1
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1
#
# # 8
# 7 + 1
# 6 + 2
# 5 + 3
# 4 + 4 == countsum(8, 2)
#
# 6 + 1 + 1
# 5 + 2 + 1
# 4 + 3 + 1
# 4 + 2 + 2
# 3 + 3 + 2 == countsum(8, 3) == countsum(7, 2) + countsum(4, 2)
#
# 5 + 1 + 1 + 1
# 4 + 2 + 1 + 1
# 3 + 3 + 1 + 1
# 3 + 2 + 2 + 1
# 2 + 2 + 2 + 2 == countsum(8, 4) == countsum(7, 3) + countsum(3 , 3) = countsum(6, 2) + countsum(3, 2) + countsum(3 , 3)
#
# 4 + 1 + 1 + 1 + 1
# 3 + 2 + 1 + 1 + 1
# 2 + 2 + 2 + 1 + 1 == countsum(8, 5) == countsum(6, 3) = countsum(5, 2) + countsum(2,2)
#
# 3 + 1 + 1 + 1 + 1 + 1
# 2 + 2 + 1 + 1 + 1 + 1 == countsum(8, 6) == countsum(4, 2)
#
# 2 + 1 + 1 + 1 + 1 + 1 + 1 == countsum(8, 7) == countsum(3, 2)
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 == countsum(8, 8)
# # 9
# 8 + 1
# 7 + 2
# 6 + 3
# 5 + 4 == countsum(9, 2)
#
# 7 + 1 + 1
# 6 + 2 + 1
# 5 + 3 + 1
# 4 + 4 + 1
# 5 + 2 + 2
# 4 + 3 + 2  == countsum(9, 3) == countsum(8, 2) + countsum(5, 2)
#
# 5 + 1 + 1 + 1
# 4 + 2 + 1 + 1
# 3 + 3 + 1 + 1
# 3 + 2 + 2 + 1
# 2 + 2 + 2 + 2 == countsum(8, 4) == countsum(7, 3) + countsum(3 , 3) = countsum(6, 2) + countsum(3, 2) + countsum(3 , 3)
#
# 4 + 1 + 1 + 1 + 1
# 3 + 2 + 1 + 1 + 1
# 2 + 2 + 2 + 1 + 1 == countsum(8, 5) == countsum(6, 3) = countsum(5, 2) + countsum(2,2)
#
# 3 + 1 + 1 + 1 + 1 + 1
# 2 + 2 + 1 + 1 + 1 + 1 == countsum(8, 6) == countsum(4, 2)
#
# 2 + 1 + 1 + 1 + 1 + 1 + 1 == countsum(8, 7) == countsum(3, 2)
#
# 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 == countsum(8, 8)



from modeuler.caches import cache

@cache
def combi(n, size):
	if size > n or n < 2:
		return 0
	if size == n or size == n - 1:
		return 1
	if size == 2:
		return n // 2

	return sum(combi(n - 1 - i, size - 1) for i in range(0, n - 1, size))

print(sum(combi(100, i) for i in range(2, 101)))