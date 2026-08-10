import json

p = r'e:\github\learn-algorithm\Untitled-1.ipynb'
with open(p, encoding='utf-8') as f:
    nb = json.load(f)

cell = nb['cells'][1]
cell['execution_count'] = None
cell['outputs'] = []

with open(p, 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print('cleared stale outputs')
