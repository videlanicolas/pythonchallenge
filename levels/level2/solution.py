#!/usr/bin/python3
import collections, itertools, enchant

data = open('challenge.txt').read()

freq = collections.Counter(data)

print(freq)

rarevalues = ''.join([k for k,v in freq.items() if v == 1])

print("Rare letters: {0}".format(rarevalues))

combinations = [''.join(x) for x in itertools.permutations(rarevalues)]

print("There are {0} possible permutations.".format(len(combinations)))

d = enchant.Dict("en_US")

valid_english = [x for x in combinations if d.check(x)]

print("Valid english words: {0}".format(' '.join(valid_english)))

for x in valid_english:
	print("http://www.pythonchallenge.com/pc/def/{0}.html".format(x))