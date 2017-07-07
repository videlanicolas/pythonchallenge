#!/usr/bin/python3
import itertools, collections

data = open("challenge.txt").read()

data = data.replace('\n','')

def is_bodyguard(s):
	assert len(s)==7
	return True if s[:3].isupper() and s[4:].isupper() and s[3].islower() else False

def window(a,size):
	return [a[i:i+size] for i in range(len(a)-size-1)]

chunks = [x for x in window(data,7) if is_bodyguard(x)]

print(chunks)

letters = ''.join([x[3] for x in chunks])

freq = collections.Counter([x[3] for x in chunks])

print(freq)

freq = dict(freq)

#Ordered dict
print(''.join([k for k in sorted(freq, key=freq.__getitem__,reverse=True)]))