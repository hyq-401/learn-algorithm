import json

path = 'Untitled-1.ipynb'
with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Fix cell 1: normalize NBSP (U+00A0) -> regular space, then rebuild with clean
# indentation and a top-level import (best practice).
cell = data['cells'][1]
src = ''.join(cell['source']).replace('\xa0', ' ')

clean = (
    "from collections import Counter\n"
    "\n"
    "\n"
    "class Solution(object):\n"
    "    def isAnagram(self, s: str, t: str) -> bool:\n"
    "        a_count = Counter(s)\n"
    "        b_count = Counter(t)\n"
    "        return a_count == b_count"
)

# Repack as notebook source list (lines keep trailing \n except the last).
lines = clean.split('\n')
cell['source'] = [ln + '\n' for ln in lines[:-1]] + [lines[-1]]

with open(path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=1, ensure_ascii=False)
    f.write('\n')

print('Fixed. Verifying...')

# Verify no NBSP remains and code compiles.
with open(path, encoding='utf-8') as f:
    data = json.load(f)
joined = ''.join(data['cells'][1]['source'])
print('non-ascii chars:', [(i, hex(ord(c))) for i, c in enumerate(joined) if ord(c) > 127])
compile(joined, '<cell>', 'exec')
print('Compiles OK.')
print(joined)
