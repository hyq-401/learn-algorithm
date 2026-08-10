import json

with open('Untitled-1.ipynb', encoding='utf-8') as f:
    data = json.load(f)

for i, c in enumerate(data['cells']):
    print(f'=== Cell {i} (type={c["cell_type"]}) ===')
    src = ''.join(c['source'])
    for ln, line in enumerate(src.split('\n'), 1):
        print(f'{ln}: {line!r}')
    nonascii = [(j, hex(ord(ch))) for j, ch in enumerate(src) if ord(ch) > 127]
    print('non-ascii:', nonascii)
    print()
