#!/usr/bin/python
# filter a json dataset by keys.
import sys
import json

raw = sys.stdin.read()
dataset = json.loads(raw)

keys = set(sys.argv[1:])
results = map(lambda data: {k: v for (k, v) in data.items() if k in keys}, dataset)

print(results)
