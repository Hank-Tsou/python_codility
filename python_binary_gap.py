import json
import re

"""
題目：BinaryGap
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.
"""

N = 328

"""
使用 Regular Expression 的簡易方法
"""
def solution(N):
	return len(max(re.findall('(0*)1', bin(N)[2:]))) if N > 0 else 0

print("regex step 1 = " + bin(N)[2:])
print("regex step 2 = " + json.dumps(re.findall('(0*)1', bin(N)[2:])))
print("regex step 3 = " + max(re.findall('(0*)1', bin(N)[2:])))
print("regex result = " + json.dumps(solution(N)))

"""
使用 strip 和 split 的簡易方法
"""
def solutionBySplit(N):
	return len(max(bin(N)[2:].strip('0').strip('1').split('1')))

print("split step 1 = " + bin(N)[2:])
print("split step 2 = " + bin(N)[2:].strip('0'))
print("split step 3 = " + bin(N)[2:].strip('0').strip('1'))
print("split step 4 = " + json.dumps(bin(N)[2:].strip('0').strip('1').split('1')))
print("split result = " + json.dumps(solutionBySplit(N)))