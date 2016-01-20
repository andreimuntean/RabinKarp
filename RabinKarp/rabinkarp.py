#!/usr/bin/python3

"""rabinkarp.py: A simple implementation of the Rabin-Karp string searching algorithm."""

__author__ = 'andrei.muntean.dev@gmail.com (Andrei Muntean)'

from sys import maxsize


# Raises x to the specified power. Must specify a mod as well.
def pow(x, exponent, mod):
	if exponent == 0:
		return 1
	elif exponent % 2 == 0:
		return pow(x * x % mod, exponent / 2, mod)
	else:
		return x * pow(x, exponent - 1, mod) % mod


# Maps the specified lowercase character to a value between 0 and 25.
def to_num(character):
	return ord(character) - 97


# Computes a hash value (a positive integer) for the specified string.
def get_hash(string, mod = None):
	if mod == None:
		mod = maxsize

	hash = 0

	for index in range(0, len(string)):
		value = to_num(string[index])
		hash += value * pow(26, len(string) - index - 1, mod)

	return hash


# Determines whether a string contains the specified substring.
def rabin_karp(string, substring):
	if len(string) < len(substring):
		return False

	target_hash = get_hash(substring)
	
	for index in range(0, len(string) - len(substring) + 1):
		hash = get_hash(string[index : index + len(substring)])	

		if hash == target_hash:
			return True

	return False


# Tests the algorithm. This implementation only works for lowercase characters.
print(rabin_karp('abcd', 'abcd'))
print(rabin_karp('abcdefg', 'a'))
print(rabin_karp('abcdefg', 'abc'))
print(rabin_karp('abcdefg', 'cde'))
print(rabin_karp('abcdefg', 'efg'))
print(rabin_karp('abcdefg', 'abcdefg'))
print(rabin_karp('x', 'abc'))
print(rabin_karp('abcdefg', 'acd'))
print(rabin_karp('abcdefg', 'efgg'))
print(rabin_karp('abcdefg', 'abcx'))